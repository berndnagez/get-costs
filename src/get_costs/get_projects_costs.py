#!/usr/bin/env python3

from choice_getter import get_choice
from sys import argv
import config
from journal_names_getter import get_journal_names
from date_creator import validate, get_year, get_sheet_name, get_date_from
from path_creator import get_paths, PathNotFoundError
from id_reader import get_all_ids_from, get_project_ids_from
from data_reader import get_list_of_dicts
from src.get_costs.projectlist_creater import create_projectlist
from costs_splitter import split_costs
from projects_rows_creator import get_all_rows
from workbook_writer import write

# getopt im choice_getter soll eine Projekt-Id entgegennehmen, wird keine angegeben, wird die Datei für Paul erstellt
# <- diese Unterscheidung muss die main_test.py (die dann main.py wird) können

# der project_row_creator nimmt die Projekt-ID entgegen und verteilt die Daten auf folgende Sheets:
# - Personalkosten
# - Umlagen
# - Fahrtkosten (für HVV)
# - Telefon
# damit werden die gewünschten Tabellen geschrieben, die letzten beiden haben nur 3 Spalten, also kann das selbe Template genommen werden

# der workbook_writer erstellt sheets in einer Schleife – die Sheets sind Klassen – wie können Klassen an eine Funktion weitergegeben werden?

# am Ende: alle alten Dateien löschen und an Paul ausliefern (wie finde ich heraus, welche gebraucht werden? von main_test ausgehen = was wird da importiert + bei den importierten schauen, was die so importieren usw. = Liste erstellen, dann löschen und testen, ob alles noch geht)
# wann merge ich die branches?

# rüste ich dann zu Übung tests nach? was ergibt die Suche zu pandas test(-driven) 


# TODO sys.exit durch Exceptions ersetzen, um den Programmfluss besser zu steuern
# TODO hilft es mir, wenn die Moduale als Packages deklarieren? irgendwie mit __int__ oder so ...

if __name__ == "__main__":
    all_rows = []
    key = ""
    # wichtige Anmerkung von Falk: choice sollte nicht mal string und mal list sein,
    # bei "all" sollte der choice_getter schon get_journal_names() ausführen und auch eine Liste zurückgeben
    # dann müsste der Outputname weiter unten in Abhängigkeit der Listen-Länge erzeugt werden
    choice = get_choice(argv[1:])
    if choice:
        journal_names = choice
        
    else:
        # TODO nutzt den journal_names_getter, der noch im falschen Verzeichnis sucht, muss eigentlich noch eine Jahresopiton entgegennehmen
        journal_names = get_journal_names()

    # Falks Vorschlag: gesamte Schleife in Funktion auslagern und alle gewünschten Exceptions abfangen, nach try können mehrere except-Blöcke kommen
    for journal_name in journal_names:
        validate(journal_name)
        year = get_year(journal_name)
        sheet_name = year_month_prefix = get_sheet_name(journal_name)
        date = get_date_from(journal_name)

        journal_data_file = employee_data_file = provisions_data_file = additional_costs_file = result_file_path = None

        try:
            journal_data_file, employee_data_file, provisions_data_file , additional_costs_file, result_file_path = get_paths(key, year, journal_name, year_month_prefix)
        except PathNotFoundError as err:
            print(f'WARNUNG: {err}')
            all_rows = []
            break
        index = config.INDEX
        ids = get_all_ids_from(employee_data_file, sheet_name)

        employee_data = get_list_of_dicts(employee_data_file, sheet_name, index, ids)
        journal_data = get_list_of_dicts(journal_data_file, "first_sheet", index, ids)
        provision = get_list_of_dicts(provisions_data_file, sheet_name, index, ids)
        additional_costs = get_list_of_dicts(additional_costs_file, sheet_name, index, ids)

        projectlist = create_projectlist(employee_data, journal_data, provision, additional_costs)
        splitted_values_list = split_costs(projectlist, projects=True)
        all_rows = get_all_rows(splitted_values_list, date, all_rows)

    border = False
    if choice:
        workbook_name = result_file_path        
    else:
        workbook_name = "Kosten_aller_MA_innen"
    
    if len(all_rows):
        write(workbook_name, border, all_rows)