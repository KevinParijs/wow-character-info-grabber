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

    def update_from_api(self, api_client):
        if self.player_class != 'TBD':
            self.id, self.item_level, self.level, self.faction, self.specialisation, self.race = api_client.get_player_item_level(self.player_name, self.realm)
            self.mythic_score = api_client.get_player_mythic_keystone_rating(self.player_name, self.realm)
        else:
            print(f"Skipping API call for {self.player_name}. Class not set.")

    def get_player_id(player_name):
        """Retrieve the player ID from the database based on the player name."""
        db_handler = DatabaseHandler(host='192.168.1.10', user='dbgrabber', password='DBgrabber123!', database='tww-data')
        if connection is None:
            return None
        
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT player_id FROM players WHERE player_name = %s"
            cursor.execute(query, (player_name,))
            result = cursor.fetchone()
            
            if result:
                return result['player_id']
            else:
                print(f"Player not found: {player_name}")
                return None
        except Error as e:
            print(f"Error querying the database: {e}")
            return None
        finally:
            cursor.close()
            connection.close()
