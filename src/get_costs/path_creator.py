import os
from .config import get_paths_for

class PathNotFoundError(Exception):
    pass


def get_JOURNAL_DATA_PATH(key, year, journal_name):
    first_path_part = get_paths_for(key).get('JOURNAL_DATA_PATH')
    if key:
        path = f'{first_path_part}/20{year}/{journal_name}'
    else:        
        path = f'{first_path_part}/20{year}/- 01 Lohnjournale/{journal_name}'
    return path

def get_EMPLOYEE_DATA_PATH(key, year):
    first_path_part = get_paths_for(key).get('RAW_DATA_PATH')
    path = f'{first_path_part}/20{year}/employee_data_20{year}.xlsx'
    return path

def get_ADDITIONAL_COSTS_PATH(key, year):
    first_path_part = get_paths_for(key).get('RAW_DATA_PATH')
    path = f'{first_path_part}/20{year}/additional_costs_20{year}.xlsx'
    return path

def get_PROVISIONS_DATA_PATH(key, year):
    first_path_part = get_paths_for(key).get('RAW_DATA_PATH')
    path = f'{first_path_part}/20{year}/provisions_data_20{year}.xlsx'
    return path

def get_RESULT_FILE_PATH(key, year_month_prefix):
    first_path_part = get_paths_for(key).get('RESULT_FILE_PATH')
    if key:
        path = f'{first_path_part}/{key}'
    else:        
        path = f'{first_path_part}/{year_month_prefix}_Kosten_aller_MA_innen'
    return path

def validate_path_exists(file_list):
    for path in file_list:
        if not os.path.exists(path):
            raise PathNotFoundError(f'Die Datei "{path}" existiert unter dem angegebenen Pfad nicht. Bitte lege sie an oder ändere den Pfad in der config.py. Dann starte das Programm neu.')
    

def get_paths(key, year, journal_name, year_month_prefix):
    journal_data_file = get_JOURNAL_DATA_PATH(key, year, journal_name)
    employee_data_file = get_EMPLOYEE_DATA_PATH(key, year)
    provisions_data_file = get_PROVISIONS_DATA_PATH(key, year)
    additional_costs_file = get_ADDITIONAL_COSTS_PATH(key, year)
    result_file_path = get_RESULT_FILE_PATH(key, year_month_prefix)
    
    validate_path_exists([journal_data_file, employee_data_file, provisions_data_file , additional_costs_file])
    return journal_data_file, employee_data_file, provisions_data_file, additional_costs_file, result_file_path
    

if __name__ == "__main__":
    get_paths('0026', '24', "24_01_24 Lohnjournal Januar 2024.xlsx", "24_01")