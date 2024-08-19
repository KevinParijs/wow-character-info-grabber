# player.py
from db_handler import DatabaseHandler
from datetime import datetime

class Player:
    def __init__(self, player_name, realm, player_class, role):
        self.id = '0'
        self.item_level = '0'
        self.level = '0'
        self.faction = 'N/A'
        self.specialisation = 'N/A'
        self.race = 'N/A'
        self.mythic_score = '0'

        self.player_name = player_name
        self.realm = realm.replace("'", "").replace(" ", "-")
        self.player_class = player_class
        self.role = role
        self.creation_datetime = datetime.today()

        self.equipment = []
        self.item_sets = []

    def update_from_api(self, api_client):
        if self.player_class != 'TBD':
            self.id, self.item_level, self.level, self.faction, self.specialisation, self.race = api_client.get_player_item_level(self.player_name, self.realm)
            self.mythic_score = api_client.get_player_mythic_keystone_rating(self.player_name, self.realm)
        else:
            print(f"Skipping Profile API call for {self.player_name}. Class not set.")

    def grab_player_equipment(self, api_client):
        if self.player_class != 'TBD':
            self.equipment = api_client.get_player_equipment(self.player_name, self.realm)
            # print(self.equipment)
        else:
            print(f"Skipping Equipment API call for {self.player_name}. Class not set.")

    def grab_player_item_sets(self, api_client):
        if self.player_class != 'TBD':
            self.item_sets = api_client.get_player_item_sets(self.player_name, self.realm)
        else:
            print(f"Skipping Equipment API call for {self.player_name}. Class not set.")