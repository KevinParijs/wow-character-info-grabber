# csv_handler.py

import csv
import os

class CSVHandler:
    def read_csv(self, file_path, filter_debug):
        player_info = []
        if filter_debug == '0':
            try:
                with open(file_path, 'r', encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        player_info.append(row)
            except FileNotFoundError:
                print(f"Error: File not found - {file_path}")
            return player_info
        else:
            try:
                with open(file_path, 'r', encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['debug'] == '1':
                            player_info.append(row)
            except FileNotFoundError:
                print(f"Error: File not found - {file_path}")
            return player_info


    def write_csv(self, file_path, data):
        fieldnames = ['char_id', 'player_name', 'realm', 'class', 'item_level', 'level', 'faction', 'role', 'specialisation', 'race', 'mythic_keystone_rating', 'creation_datetime', 'run_id']
        file_exists = os.path.isfile(file_path)

        try:
            with open(file_path, 'a', newline='', encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
                for row in data:
                    writer.writerow(row)
            print(f"Data successfully appended to {file_path}")
        except Exception as e:
            print(f"Error writing to CSV file: {e}")
