from journal_names_getter import get_journal_names
from path_creator import get_paths
from project_rows_creator import create_project_sheets, distribute_values_to_sheets, remove_empty_rows, add_last_row
from projects_rows_creator import get_all_rows
from config import get_paths_for, INDEX, get_personal_of, get_sheetnames_of
from id_reader import get_all_ids_from
from date_creator import get_year, get_sheet_name, get_date_from
from project_costs_calculator import calculate
from costs_splitter import split
from projects_rows_creator import get_all_rows
from workbook_writer import write

from data_reader import reader

project_sheets = {}

def get_available_project_staff_ids(project_staff_ids, all_ids_from_journal):
    ids = []
    for id in project_staff_ids:
        if int(id) in all_ids_from_journal:
            ids.append(int(id))
    return ids


def create_result_file_for(project_id):
    paths = get_paths_for(project_id)
    journal_data_path = paths.get('JOURNAL_DATA_PATH')
    year_dirs =  get_journal_names(journal_data_path)
    journal_names = []
    for year_dir in year_dirs:
        journal_names.extend(get_journal_names(journal_data_path + f'/{year_dir}/'))
    project_sheets = create_project_sheets(get_sheetnames_of(project_id))

    # hier ist der Gedanke, dass einfach alle Lohnjournale verarbeitet werden, die da sind; perspektivisch wäre es cool, einen Auswertungszeitraum angeben zu können
    # und hier beißt die Katze in den Schwanz: eigentlich müsste ich für jeden auszuwertenden Monat den path_creator nutzen
    # aber hole mir vorher alle journal_names, um zu wissen, was ausgewertet werden soll
    # ich müsste mir eigentlich da Zeitraum holen und dann für jeden Monat des Zeitraums die Dateien
    # LÖSUNG: per GUI die auszuwertenden Dateien auswählen (siehe auch: Notizen path_creator.py)
    for journal_name in journal_names:
        year = get_year(journal_name)
        sheet_name = year_month_prefix = get_sheet_name(journal_name)
        journal_data_file, employee_data_file, provisions_data_file, additional_costs_file, result_file_path = get_paths(project_id, year, journal_name, year_month_prefix)
        date = get_date_from(journal_name)
        index = INDEX
        project_staff_ids = get_personal_of(project_id)
        all_ids_from_journal = get_all_ids_from(journal_data_file, "first_sheet")
        ids = get_available_project_staff_ids(project_staff_ids, all_ids_from_journal)

        employee_data = reader.get_list_of_dicts(employee_data_file, sheet_name, index, ids)
        # TODO nächste Zeile führt zu Problemen bei "23_02_21 Lohnjournal Februar 2023.xlsx", wenn Tabellenblatt "Februar 2023" nicht an erster Stelle
        journal_data = reader.get_list_of_dicts(journal_data_file, "first_sheet", index, ids)
        provision = reader.get_list_of_dicts(provisions_data_file, sheet_name, index, ids)
        additional_costs = reader.get_list_of_dicts(additional_costs_file, sheet_name, index, ids)

        project_list = calculate(employee_data, journal_data, provision, additional_costs)
        splitted_values_list = split(project_list, projects=False)
        distribute_values_to_sheets(splitted_values_list, project_id, date, project_sheets)
    project_sheets =  remove_empty_rows(project_sheets)
    add_last_row(project_sheets)
    border = True
    result_file_path = paths.get('RESULT_FILE_PATH') + f'{project_id}'
    write(result_file_path, border, project_sheets)


def create_result_file_for_all_projects(journal_name):
    year = get_year(journal_name)
    sheet_name = year_month_prefix = get_sheet_name(journal_name)
    journal_data_file, employee_data_file, provisions_data_file, additional_costs_file, result_file_path = get_paths('', year, journal_name, year_month_prefix)
    date = get_date_from(journal_name)
    index = INDEX
    ids = get_all_ids_from(journal_data_file, "first_sheet")

    employee_data = reader.get_list_of_dicts(employee_data_file, sheet_name, index, ids)
    # TODO nächste Zeile führt zu Problemen bei "23_02_21 Lohnjournal Februar 2023.xlsx", wenn Tabellenblatt "Februar 2023" nicht an erster Stelle
    journal_data = reader.get_list_of_dicts(journal_data_file, "first_sheet", index, ids)
    provision = reader.get_list_of_dicts(provisions_data_file, sheet_name, index, ids)
    additional_costs = reader.get_list_of_dicts(additional_costs_file, sheet_name, index, ids)

    project_list = calculate(employee_data, journal_data, provision, additional_costs)
    splitted_values_list = split(project_list, projects=True)
    all_rows = []
    all_rows = get_all_rows(splitted_values_list, date, all_rows)
    border = False
    write(result_file_path, border, all_rows)
    #TODO Fehler abfangen, wenn hinter -i der Dateiname nicht in Anführungszeichen kommt (dann sollte nur das Datum hier ankommmen und es müsste eine Fehler entstehen)

def create_result_file_for_project_with(journal, project_id):
    print("Die Auswertung eines einzelnen Projekts in Zusammenhang mit einem einzelnen Lohnjournal ist noch nicht implementiert.")