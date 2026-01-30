from datetime import datetime
import re

def validate(journal_name):
    pattern = re.compile(r"\d{2}_\d{2}.*")
    if not re.fullmatch(pattern, journal_name):
        print(f"Die Datei '{journal_name}' hat keinen validen Dateinamen. Der Dateiname muss mit dem Jahr, gefolgt von Monat und Tag anfangen.")
        print(f"Bspw. 24_04_23 für das Lohnjournal des Aprils 2024.")
        exit('Programmabbruch.')

def split_year_month(filename):
    name_parts = filename.split("_")
    year = name_parts[0]
    month = name_parts[1]
    return year, month

def get_sheet_name(filename):
    year, month = split_year_month(filename)
    sheet_name = f'{year}_{month}'
    return sheet_name

def get_date_from(filename):
    year, month = split_year_month(filename)
    date_str = f'01-{month}-{year}'
    date_object = datetime.strptime(date_str, '%d-%m-%y').date()
    return date_object

def get_year(filename):
    return filename.split("_")[0]

def get_date_object(sheet_name):
    parts_of_sheet_name = sheet_name.split("_")
    year = parts_of_sheet_name[0]
    month = parts_of_sheet_name[1]
    date_str = f'01-{month}-{year}'
    date_object = datetime.strptime(date_str, '%d-%m-%y').date()
    return date_object