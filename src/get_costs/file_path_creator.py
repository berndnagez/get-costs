import os.path
import sys
import get_costs.config

def create_file_paths(year, journal_name):
    journal_data_file = f'{get_costs.config.JOURNAL_DATA_PATH}/20{year}/- 01 Lohnjournale/{journal_name}'
    employee_data_file = f'{get_costs.config.RAW_DATA_PATH}/20{year}/employee_data_20{year}.xlsx'
    provisions_data_file = f'{get_costs.config.RAW_DATA_PATH}/20{year}/provisions_data_20{year}.xlsx'
    additional_costs_file = f'{get_costs.config.RAW_DATA_PATH}/20{year}/additional_costs_20{year}.xlsx'    
    validate_file_exits([journal_data_file, employee_data_file, provisions_data_file, additional_costs_file])
    return journal_data_file, employee_data_file, provisions_data_file, additional_costs_file


def validate_file_exits(list_of_files):
    for path in list_of_files:
        if not os.path.exists(path):
            print(f'Die Datei "{path}" existiert unter dem angegebenen Pfad nicht. Bitte lege sie an oder ändere den Pfad in der config.py. Dann starte das Programm neu.')
            print(f'')
            print(f'Aber velleicht hast Du auch den Terminal im falschen Seafile-Verzeichnis geöffnet?')
            print(f'Bist Du hier: 2000 -> 97?')
            sys.exit()

def show_debug_infos():
    validate_file_exits(["./data/24_01_24 Lohnjournal Januar 2024.xlsx", "./data/24_02_24 Lohnjournal Januar 2024.xlsx"])
    validate_file_exits(["./data/test.txt"])

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()