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
        # print(url)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            char_id = data.get('id')
            item_level = data.get('equipped_item_level', '0')
            char_lvl = data.get('level', '0')
            char_faction = data.get('faction', {}).get('name', 'N/A')
            char_specc = data.get('active_spec', {}).get('name', 'N/A')
            char_race = data.get('race', {}).get('name', 'N/A')
            return char_id, item_level, char_lvl, char_faction, char_specc, char_race
        else:
            print(f"Error fetching data for {player_name} on {realm}. Status code: {response.status_code}")
            return None, None, None, None, None

    def get_player_equipment(self, player_name, realm):
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realm.lower()}/{player_name.lower()}/equipment?namespace=profile-{self.region}&locale=en_GB&access_token={self.access_token}"

        # https://eu.api.blizzard.com/profile/wow/character/stormscale/khaelitha/equipment?namespace=profile-eu&locale=en_GB&access_token=EURSlT35ZKzBIpYVAgIw6rq2VCEGUPjdE1
        
        # print(url)
        
        response = requests.get(url)
        if response.status_code ==200:
            data = response.json()
            char_id = {
                'char_id': data.get('character', {}).get('id', '0')
            }

            equipment = []
            for item in data.get('equipped_items', []):
                item_info = {
                    'item_id': item.get('item', {}).get('id'),
                    'slot_name': item.get('slot', {}).get('name'),
                    'quality_name': item.get('quality', {}).get('name'),
                    'level_value': item.get('level', {}).get('value'),
                    'item_name': item.get('name'),
                    'name_description': item.get('name_description', {}).get('display_string', ''),
                    'sockets': []
                }

                # Get socket information
                for socket in item.get('sockets', []):
                    socket_info = {
                        'socket_type': socket.get('socket_type', {}).get('name'),
                        'socket_item_name': socket.get('item', {}).get('name', ''),
                        'socket_item_id': socket.get('item', {}).get('id', '0'),
                        'socket_display_string': socket.get('display_string', '')
                    }
                    item_info['sockets'].append(socket_info)

                equipment.append(item_info)
            equipment.append(char_id)

            # Return or store the structured data
            # print(equipment)
            return equipment
        else:
            print(f"ERROR: Error fetching equipment for {player_name} on realm {realm}. Status code: {response.status_code}")
            return 0

    def get_player_item_sets(self, player_name, realm):
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realm.lower()}/{player_name.lower()}/equipment?namespace=profile-{self.region}&locale=en_GB&access_token={self.access_token}"

        # https://eu.api.blizzard.com/profile/wow/character/stormscale/khaelitha/equipment?namespace=profile-eu&locale=en_GB&access_token=EURSlT35ZKzBIpYVAgIw6rq2VCEGUPjdE1
        
        response = requests.get(url)
        if response.status_code ==200:
            data = response.json()
            char_id = data.get('character', {}).get('id', '0')

            # Parse equipped item sets
            item_sets = []
            for item_set in data.get('equipped_item_sets', []):
                set_info = {
                    'item_set_id': item_set.get('item_set', {}).get('id', ''),
                    'item_set_name': item_set.get('item_set', {}).get('name', ''),
                    'items': []
                }

                for item in item_set.get('items', []):
                    item_detail = {
                        'item_id': item.get('item', {}).get(id, ''),
                        'item_name': item.get('item', {}).get(name, ''),
                        'is_equipped': item.get('is_equipped', False)
                    }
                    set_info['items'].append(item_detail)

                item_sets.append(set_info)
            item_sets.append(char_id)

            # Return or store the structured data
            return item_sets
        else:
            print(f"Error fetching m+ score for {player_name} on realm {realm}. Status code: {response.status_code}")
            return 0

    def get_player_primary_professions(self, player_name, realm):
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realm.lower()}/{player_name.lower()}/professions?namespace=profile-{self.region}&locale=en_GB&access_token={self.access_token}"

        # https://eu.api.blizzard.com/profile/wow/character/stormscale/khaelitha/professions?namespace=profile-eu&locale=en_GB&access_token=EURSlT35ZKzBIpYVAgIw6rq2VCEGUPjdE1

        response = requests.get(url)
        if response.status_code ==200:
            data = response.json()
            # Complete this functionality
        else:
            print(f"Error fetching m+ score for {player_name} on realm {realm}. Status code: {response.status_code}")
            return 0
    
    def get_player_mythic_keystone_rating(self, player_name, realm):
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realm.lower()}/{player_name.lower()}/mythic-keystone-profile?namespace=profile-{self.region}&locale=en_GB&access_token={self.access_token}"

        response = requests.get(url)
        if response.status_code ==200:
            data = response.json()
            mythic_score = data.get('current_mythic_rating', {}).get('rating', '0')
            return mythic_score
        else:
            print(f"Error fetching m+ score for {player_name} on realm {realm}. Status code: {response.status_code}")
            return 0