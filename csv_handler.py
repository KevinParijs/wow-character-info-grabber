# csv_handler.py

import csv
import os

class CSVHandler:
    def read_csv(self, file_path):
        player_info = []
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    player_info.append(row)
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
        return player_info

    def write_csv(self, file_path, data):
        fieldnames = ['player_name', 'realm', 'class', 'item_level', 'level', 'faction', 'role', 'specialisation', 'race', 'creation_datetime']
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