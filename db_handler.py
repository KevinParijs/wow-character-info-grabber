# database_handler.py

import mysql.connector
from mysql.connector import Error

class DatabaseHandler:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = self.create_connection()

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=3306,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                print("Connected to MariaDB database")
                return connection
        except Error as e:
            print(f"Error connecting to MariaDB database: {e}")
            return None

    def write_to_database(self, data):
        if not self.connection:
            print("No database connection available")
            return

        try:
            cursor = self.connection.cursor()
            for row in data:
                sql = """
                INSERT INTO players (player_name, realm, class, item_level, level, faction, role, specialisation, race, creation_datetime)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (
                    row['player_name'],
                    row['realm'],
                    row['class'],
                    row['item_level'],
                    row['level'],
                    row['faction'],
                    row['role'],
                    row['specialisation'],
                    row['race'],
                    row['creation_datetime']
                )
                cursor.execute(sql, values)
            self.connection.commit()
            print("Data successfully written to database")
        except Error as e:
            print(f"Error writing to database: {e}")

    def insert_item(conn, item):
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO items (item_id, name, item_class, item_subclass, level, quality, quantity, 
                                modified_appearance_id, transmog_id, creation_timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            item.item_id, item.name, item.item_class, item.item_subclass, item.level, item.quality, 
            item.quantity, item.modified_appearance_id, item.transmog_id, datetime.now()
        ))
        conn.commit()

    def insert_stats(conn, item_id, stats):
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO item_stats (item_id, stat_type, value)
            VALUES (%s, %s, %s)
        ''', [(item_id, stat['type'], stat['value']) for stat in stats])
        conn.commit()

    def insert_enchantments(conn, item_id, enchantments):
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO item_enchantments (item_id, enchantment_display_string, enchantment_source_item_id)
            VALUES (%s, %s, %s)
        ''', [(item_id, enchantment['display_string'], enchantment['source_item_id']) for enchantment in enchantments])
        conn.commit()

    def insert_sockets(conn, item_id, sockets):
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO item_sockets (item_id, socket_type, socket_item_id)
            VALUES (%s, %s, %s)
        ''', [(item_id, socket['type'], socket['socket_item_id']) for socket in sockets])
        conn.commit()

    def insert_sets(conn, item_id, set_info):
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO item_sets (item_id, set_name, set_effects)
            VALUES (%s, %s, %s)
        ''', (item_id, set_info['name'], set_info['effects']))
        conn.commit()

    def insert_player_item(conn, player_id, item_id, equipped):
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO player_items (player_id, item_id, equipped)
            VALUES (%s, %s, %s)
        ''', (player_id, item_id, equipped))
        conn.commit()




    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")
