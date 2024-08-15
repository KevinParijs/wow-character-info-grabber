# blizzard_api.py

import requests
import os

class BlizzardAPI:
    def __init__(self, client_id=None, client_secret=None, region='eu'):
        self.client_id = client_id or os.environ.get('bnet_client_id')
        self.client_secret = client_secret or os.environ.get('bnet_client_secret')
        self.region = region
        self.access_token = self.generate_access_token()

    def generate_access_token(self):
        url = 'https://eu.battle.net/oauth/token'
        if not self.client_id or not self.client_secret:
            print("Error: Missing client_id or client_secret in environment variables.")
            return None

        data = {'grant_type': 'client_credentials'}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        auth = (self.client_id, self.client_secret)

        response = requests.post(url, data=data, headers=headers, auth=auth)

        if response.status_code == 200:
            return response.json()['access_token']
        else:
            print("Error:", response.status_code, response.json())
            return None

    def get_player_item_level(self, player_name, realm):
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realm.lower()}/{player_name.lower()}?namespace=profile-{self.region}&locale=en_GB&access_token={self.access_token}"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            item_level = data.get('equipped_item_level', 'N/A')
            char_lvl = data.get('level', 'N/A')
            char_faction = data.get('faction', {}).get('name', 'N/A')
            char_specc = data.get('active_spec', {}).get('name', 'N/A')
            char_race = data.get('race', {}).get('name', 'N/A')
            return item_level, char_lvl, char_faction, char_specc, char_race
        else:
            print(f"Error fetching data for {player_name} on {realm}. Status code: {response.status_code}")
            return None, None, None, None, None

    def get_player_equipment(self, player_name, realm):
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realm.lower()}/{player_name.lower()}/equipment?namespace=profile-{self.region}&locale=en_GB&access_token={self.access_token}"