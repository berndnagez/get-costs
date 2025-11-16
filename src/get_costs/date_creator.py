from datetime import datetime
import re

def validate(journal_name):
    pattern = re.compile(r"\d{2}_\d{2}.*")
    if not re.fullmatch(pattern, journal_name):
        print(f"Die Datei '{journal_name}' hat keinen validen Dateinamen. Der Dateiname muss mit dem Jahr, gefolgt vom Monat anfangen.")
        print(f"Bspw. 24_04 für das Lohnjournal des Aprils 2024.")
        exit('Programmabbruch.')

def split(filename):    
    name_parts = filename.split("_")
    year = name_parts[0]
    month = name_parts[1]
    return year, month

def get_sheet_name(filename):
    year, month = split(filename)
    sheet_name = f'{year}_{month}'
    return sheet_name

def get_date(filename):
    year, month = split(filename)
    date_str = f'01-{month}-{year}'
    date_object = datetime.strptime(date_str, '%d-%m-%y').date()
    return date_object

def get_year(filename):
    return filename.split("_")[0]


def show_debug_infos():
    print(get_year("23_12_20 Lohnjournal Dezember 2023.xlsx"))
    sheet_name = get_sheet_name("23_12_20 Lohnjournal Dezember 2023.xlsx")
    date = get_date("23_12_20 Lohnjournal Dezember 2023.xlsx")
    print(sheet_name)
    print(date)
    validate("23_12_20 Lohnjournal Dezember 2023.xlsx")
    validate("Lohnjournal Dezember 2023.xlsx")


if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()