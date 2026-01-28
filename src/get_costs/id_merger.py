from math import isnan
from .id_reader import get_all_ids_from
from .path_creator import get_paths

def merge_ids(files, sheet_name):
    journal_data_file, employee_data_file, provisions_data_file, additional_costs_file = files

    journal_ids = get_all_ids_from(journal_data_file, "first_sheet")
    employee_ids = get_all_ids_from(employee_data_file, sheet_name)
    provision_ids = get_all_ids_from(provisions_data_file, sheet_name)
    additional_costs_ids = get_all_ids_from(additional_costs_file, sheet_name)

    ids = []
    for id in employee_ids:
        if not isnan(id) and id not in ids:
            ids.append(id)
    for id in journal_ids:
        if not isnan(id) and id not in ids:
            ids.append(id)
    for id in provision_ids:
        if not isnan(id) and id not in ids:
            ids.append(id)
    for id in additional_costs_ids:
        if not isnan(id) and id not in ids:
            ids.append(id)
    ids = [int(x) for x in ids]
    return ids


def show_debug_infos():
    journal_data_file, employee_data_file, provisions_data_file, additional_costs_file, result_file_path = get_paths('', '25', '25_09_11 Lohnjournal September 2025.xlsx', '25_09')
    print(merge_ids(files=(journal_data_file, employee_data_file, provisions_data_file, additional_costs_file), sheet_name='25_09'))

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()