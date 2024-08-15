# main.py
import requests
import csv
import os
from datetime import datetime

from blizzard_api import BlizzardAPI
from csv_handler import CSVHandler
from db_handler import DatabaseHandler
from player import Player

def player_info(api_client, db_handler):
    # Read players from CSV
    csv_handler = CSVHandler()
    players = csv_handler.read_csv("input/tww-uproar.csv")
    if not players:
        return

    player_data = []
    for player in players:
        p = Player(player['player_name'], player['realm'], player['class'], player['role'])
        p.update_from_api(api_client)
        player_data.append({
            'player_name': p.player_name,
            'realm': p.realm,
            'class': p.player_class,
            'item_level': p.item_level,
            'level': p.level,
            'faction': p.faction,
            'role': p.role,
            'specialisation': p.specialisation,
            'race': p.race,
            'creation_datetime': p.creation_datetime
        })

    # Write data to CSV
    output_file_path = "output/player_data.csv"
    csv_handler.write_csv(output_file_path, player_data)

    # Write data to MariaDB
    db_handler.write_to_database(player_data)
    # player_id = Player.get_player_id(player_data['player_name'])

    print('Output process completed!')

def player_items():
    return True

def main():
    # Load environment variables
    client_id = os.environ.get('bnet_client_id')
    client_secret = os.environ.get('bnet_client_secret')

    # Instantiate API client
    api_client = BlizzardAPI(client_id, client_secret)

    # Grab player information
    db_handler = DatabaseHandler(host='192.168.1.10', user='dbgrabber', password='DBgrabber123!', database='tww-data')
    player_info(api_client, db_handler)
    db_handler.close_connection()

    

if __name__ == "__main__":
    main()
