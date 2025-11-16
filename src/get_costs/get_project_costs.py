#!/usr/bin/env python3

from .choice_getter import get_file
from sys import argv
import get_costs.config
from .journal_names_getter import get_journal_names
from .date_creator import validate, get_year, get_sheet_name, get_date
from .file_path_creator import create_file_paths
from .id_reader import get_all_ids_from, get_project_ids_from
from .data_reader import get_list_of_dicts
from .project_costs_calculator import calculate
from .costs_spliter import split
from .projects_rows_creator import get_all_rows
from .workbook_writer import write

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


##### WICHTIG FÜR DEPLOY #####
# nur aktualisieren, wenn Pauls Rechner an ist
# weil das x bei Paul bei jedem Update der get_projects_costs.py per Seafile überschrieben wird
# -> ich muss per ssh rauf und das chmod u+x neu machen

#TODO file_dict_validator verallgemeinern, so das Pfad und Name übergeben und geprüft werden

def main():
    all_rows = []

    choice = get_file(argv[1:])
    if choice == "all":
        # TODO nutzt den journal_names_getter, der noch im falschen Verzeichnis sucht, muss eigentlich noch eine Jahresopiton entgegennehmen
        journal_names = get_journal_names()
    else:
        journal_names = choice

    for journal_name in journal_names:
        validate(journal_name)
        year = get_year(journal_name)
        sheet_name = year_month_prefix = get_sheet_name(journal_name)
        date = get_date(journal_name)

        journal_data_file, employee_data_file, provisions_data_file , additional_costs_file = create_file_paths(year, journal_name)
        index = get_costs.config.INDEX
        ids = get_all_ids_from(employee_data_file, sheet_name)

        employee_data = get_list_of_dicts(employee_data_file, sheet_name, index, ids)
        journal_data = get_list_of_dicts(journal_data_file, "first_sheet", index, ids)
        provision = get_list_of_dicts(provisions_data_file, sheet_name, index, ids)
        additional_costs = get_list_of_dicts(additional_costs_file, sheet_name, index, ids)

        project_list = calculate(employee_data, journal_data, provision, additional_costs)
        splitted_values_list = split(project_list, projects=True)
        all_rows = get_all_rows(splitted_values_list, date, all_rows)

    border = False
    if choice == "all":
        workbook_name = "Kosten_aller_MA_innen"
    else:
        workbook_name = f"./- 02 Ergebnisse der Auswertung (Monatsweise)/{year_month_prefix}_Kosten_aller_MA_innen"
    

    write(workbook_name, border, all_rows,)

if __name__ == "__main__":
    main()