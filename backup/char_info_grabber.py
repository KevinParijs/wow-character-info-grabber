import requests
import csv
import os
from datetime import datetime

# Create client on https://develop.battle.net/access/clients and create 2 environment variables with your client_id & client_secret
client_id = os.environ.get('bnet_client_id')
client_secret = os.environ.get('bnet_client_secret')

url = 'https://eu.battle.net/oauth/token'

def generate_access_token():
    if not client_id or not client_secret:
        print("Error: Missing client_id or client_secret in environment variables.")
        return None

    data = {
        'grant_type': 'client_credentials'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    auth = (client_id, client_secret)

    response = requests.post(url, data=data, headers=headers, auth=auth)

    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        return access_token
    else:
        print("Error:", response.status_code, response.json())
        return None

def get_player_item_level(player_name, realm, region, api_key):
    url = f"https://{region}.api.blizzard.com/profile/wow/character/{realm.lower()}/{player_name.lower()}?namespace=profile-{region}&locale=en_GB&access_token={api_key}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        item_lvl = data.get('equipped_item_level', 'N/A')
        char_lvl = data.get('level', 'N/A')
        char_faction = data.get('faction', {}).get('name', 'N/A')
        char_specc = data.get('active_spec', {}).get('name', 'N/A')
        char_race = data.get('race', {}).get('name', 'N/A')
        return item_lvl, char_lvl, char_faction, char_specc, char_race
    else:
        return None, None, None

def read_csv(file_path):
    player_info = []
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                player_info.append(row)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    return player_info

def write_csv(file_path, data):
    fieldnames = ['player_name', 'realm', 'class', 'item_level', 'level', 'faction', 'role', 'specialisation', 'race', 'creation_datetime']
    file_exists = os.path.isfile(file_path)

    try:
        with open(file_path, 'a', newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()  # Only write the header if the file doesn't exist
            for row in data:
                writer.writerow(row)
        print(f"Data successfully appended to {file_path}")
    except Exception as e:
        print(f"Error writing to CSV file: {e}")

def main():
    region = "eu"  # Change this to your region
    access_token = generate_access_token()

    if not access_token:
        return

    players = read_csv("input/tww-uproar.csv")  # Path to your CSV file
    if not players:
        return

    player_data = []

    for player in players:
        player_name = player['player_name']
        realm = player['realm']
        realm_cleaned = realm.replace("'", "").replace(" ", "-")
        player_class = player['class']
        player_role = player['role']

        item_level = 0
        char_lvl = 70
        char_faction = 'Panda'
        char_specc = 'TBD'
        char_race = 'TBD'

        if player_class != 'TBD':
            item_level, char_lvl, char_faction, char_specc, char_race = get_player_item_level(player_name, realm_cleaned, region, access_token)
            if item_level is not None:
                print(f"Player: {player_name}, Realm: {realm_cleaned}, Class: {player_class}, Item Level: {item_level}, Level: {char_lvl}, Faction: {char_faction}, Spec: {char_specc}, Race: {char_race}, Role: {player_role}")
            else:
                print(f"Error fetching data for Player: {player_name}, Realm: {realm_cleaned}")
        else:
            print(f"Player: {player_name}, Realm: {realm_cleaned}, Class: {player_class}, Role: {player_role}, This player did not choose his/her class yet or the char. name is incorrect")

        player_data.append({
            'player_name': player_name,
            'realm': realm_cleaned,
            'class': player_class,
            'item_level': item_level,
            'level': char_lvl,
            'faction': char_faction,
            'role': player_role,
            'specialisation': char_specc,
            'race': char_race,
            'creation_datetime': datetime.today()
        })

    output_file_path = "output/player_data.csv"  # Path to your output CSV file
    write_csv(output_file_path, player_data)
    print('Output file created!')

if __name__ == "__main__":
    main()
