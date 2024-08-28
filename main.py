# main.py
import requests
import csv
import os
import hashlib
import time
from datetime import datetime

from blizzard_api import BlizzardAPI
from csv_handler import CSVHandler
from db_handler import DatabaseHandler
from player import Player

# Load environment variables
mariadb_user = os.environ.get('mariadb_syno_user')
mariadb_pwd = os.environ.get('mariadb_syno_pwd')
client_id = os.environ.get('bnet_client_id')
client_secret = os.environ.get('bnet_client_secret')

# Current datetime
now = datetime.now()

def player_info(api_client, db_handler):
    run_id = datetime.today().strftime('%Y%m%d%H%M')

    print(f"Collecting player information through Blizzard API...")

    # Read players from CSV
    csv_handler = CSVHandler()
    players = csv_handler.read_csv("input/tww-uproar.csv", '0')
    if not players:
        return

    player_data = []
    for player in players:
        try:
            p = Player(player['player_name'], player['realm'], player['class'], player['role'])
            p.update_from_api(api_client)
            # print(f'char_id: {str(p.id)} !!')
            print(f"--> Grabbing player info for {p.player_name} ({str(p.id)}) !")
            result = hashlib.md5(str(p.id).encode())
            player_data.append({
                'char_id': result.hexdigest(),
                'player_name': p.player_name,
                'realm': p.realm,
                'class': p.player_class,
                'item_level': p.item_level,
                'level': p.level,
                'faction': p.faction,
                'role': p.role,
                'specialisation': p.specialisation,
                'race': p.race,
                'mythic_keystone_rating': p.mythic_score,
                'creation_datetime': p.creation_datetime,
                'run_id': run_id
            })
        except:
            print("An error occured during the API call for player profile: "+ player['player_name'])

    # Write data to CSV
    output_file_path = "output/player_data.csv"
    csv_handler.write_csv(output_file_path, player_data)

    # Write data to MariaDB
    db_handler.insert_player(player_data, now)

    print(f"Collecting player information completed!")

def player_equipment(api_client, db_handler):

    print(f"Collecting player equipment through Blizzard API...")
    # Read players from CSV
    csv_handler = CSVHandler()
    players = csv_handler.read_csv("input/tww-uproar.csv", '0')
    if not players:
        return

    player_equipment = []
    for player in players:
        try:
            p = Player(player['player_name'], player['realm'], player['class'], player['role'])
            p.grab_player_equipment(api_client)

            # Detailed debug information
            # print(f"Player: {player['player_name']}, Equipment: {p.equipment}")

            # print(p.equipment)

            for item in p.equipment:
                if 'char_id' in item:
                    char_id_value = item['char_id']
                    break

            result = hashlib.md5(str(char_id_value).encode())
            print(f"--> Grabbing player equipment for {p.player_name} ({char_id_value})")

            filtered_equipment = [item for item in p.equipment if 'item_id' in item]
            for item in filtered_equipment:
                
                sockets = item.get('sockets')

                if sockets:  # Check if the item has sockets
                    for socket in sockets:
                        player_equipment.append({
                            'char_id': result.hexdigest(),
                            'item_id': item['item_id'],
                            'slot_name': item['slot_name'],
                            'quality_name': item['quality_name'],
                            'level_value': item['level_value'],
                            'item_name': item['item_name'],
                            'name_description': item['name_description'],
                            'socket_type': socket['socket_type'],
                            'socket_item_name': socket['socket_item_name'],
                            'socket_item_id': socket['socket_item_id'],
                            'socket_display_string': socket['socket_display_string']
                        })
                    # print(player_equipment)
                else:
                    # If no sockets, add the item with empty socket fields
                    player_equipment.append({
                        'char_id': result.hexdigest(),
                        'item_id': item['item_id'],
                        'slot_name': item['slot_name'],
                        'quality_name': item['quality_name'],
                        'level_value': item['level_value'],
                        'item_name': item['item_name'],
                        'name_description': item['name_description'],
                        'socket_type': '',  # Empty fields for no socket
                        'socket_item_name': '',
                        'socket_item_id': 0,
                        'socket_display_string': ''
                    })
                    # print(player_equipment)
        except Exception as e:
            print(f"Error details: {str(e)}")
            # print("An error occured during the API call for player equipment: "+ player['player_name'])

    # Write data to MariaDB
    db_handler.insert_item(player_equipment, now)

    print(f"Collecting player equipment completed!")

def main():
    # Instantiate API client
    api_client = BlizzardAPI(client_id, client_secret)

    # Grab player information
    db_handler = DatabaseHandler(host='192.168.1.10', user=mariadb_user, password=mariadb_pwd, database='tww-data')
    player_info(api_client, db_handler)
    player_equipment(api_client, db_handler)
    db_handler.close_connection()

def truncate_tables():
    db_handler = DatabaseHandler(host='192.168.1.10', user=mariadb_user, password=mariadb_pwd, database='tww-data')
    tables = ['players','items']
    db_handler.truncate_tables(tables)
    db_handler.close_connection()

def menu():
    print("What do you want to do?")
    print("1. Grab player & equipment data through the Blizzard API")
    print("2. Truncate players & equipment tables from the database.")
    choice = input("Enter choice: ")
    
    match choice:
        case "1":
            main()
        case "2":
            #print(f"Disabled to prevent oepsies!") 
            truncate_tables()
        case _:
            print(f"This is an invalid choice!")

if __name__ == "__main__":
    menu()
