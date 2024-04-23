import requests
import csv
import os

# Create client on https://develop.battle.net/access/clients and create 2 enviroment variables with your client_id & client_secret
client_id = os.environ.get('bnet_client_id')
client_secret = os.environ.get('bnet_client_secret')

url = 'https://eu.battle.net/oauth/token'

def generate_access_token():
    # Prepare the data to be sent in the request body
    data = {
        'grant_type': 'client_credentials'
    }

    # Include client ID and client secret in the request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    # Include client ID and client secret in the request
    auth = (client_id, client_secret)

    # Make the request
    response = requests.post(url, data=data, headers=headers, auth=auth)

    # Check response status code
    if response.status_code == 200:
        data = response.json()
        # Extract and print the access token
        access_token = data['access_token']
        print("Access Token:", access_token)
        return access_token
    else:
        print("Error:", response.status_code)


# Function to retrieve player item level
def get_player_item_level(player_name, realm, region, api_key):
    url = f"https://{region}.api.blizzard.com/profile/wow/character/{realm.lower()}/{player_name.lower()}?namespace=profile-{region}&locale=en_GB&access_token={api_key}"
    #print(f"Sending request to: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        #print(data)
        # Iterate through equipment slots to find item level
        item_lvl = data['equipped_item_level']
        return item_lvl
    else:
        return "Player not found or error in API request"

# Read CSV file
def read_csv(file_path):
    player_info = []
    with open(file_path, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_info.append(row)
    return player_info

def main():
    # Read API key from a file or from environment variable
    region = "eu"  # Change this to your region

    access_token = generate_access_token()
    
    players = read_csv("heroic-roster.csv")  # Path to your CSV file
    for player in players:
        player_name = player['player_name']
        realm = player['realm']
        realm_cleaned = realm.replace("'", "").replace(" ", "-")
        player_class = player['class']
        item_level = get_player_item_level(player_name, realm_cleaned, region, access_token)
        print(f"Player: {player_name}, Realm: {realm_cleaned}, Class: {player_class}, Item Level: {item_level}")

if __name__ == "__main__":
    main()
