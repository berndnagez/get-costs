from .data_reader import get_list_of_dicts
from .data_merger import merge_dicts
from .file_path_creator import create_file_paths

#TODO in config auslagern
#TODO Exception abfangen, falls sich Spaltennamen geändert haben
OF_INTEREST = [
    'ID',
    'Name',
    'Wochenstd',
    'St.Brutto - Steuerbrutto',
    'BezPausch - Pauschal versteuerte Bezüge',
    'U1 - Umlage 1',
    'U2 - Umlage 2',
    'InsoU - Insolvenzgeldumlage',
    'KV-AG-Beitrag',
    'RV-AG-Beitrag',
    'AV-AG-Beitrag',
    'PV-AG-Beitrag',
    'bAV AG-Anteil',
    'HVV',
    '1&1',
    'Wetell',
    'Edenred',
    'Urban Sports',
    'AU-Erstattung'
    ]
UNNEEDED_EMPLOYEE_DATA = ['Kontrolle']

def erase_unneeded_data(data):
    clean_employee_list = []
    for employee in data:
        clean_employee_dict = {}
        for key, value in employee.items():
            
            if key in OF_INTEREST:
                clean_employee_dict[key] = value

        clean_employee_list.append(clean_employee_dict)
    return clean_employee_list

def erase_unneeded_employee_data(data):
    clean_employee_list = []
    for employee in data:
        clean_employee_dict = {}
        for key, value in employee.items():
            
            if key not in UNNEEDED_EMPLOYEE_DATA:
                clean_employee_dict[key] = value

        clean_employee_list.append(clean_employee_dict)
    return clean_employee_list


def add_values_of_interest(project_dict, employee):
    for key in OF_INTEREST:
        project_dict[key] = employee.get(key)
    return project_dict


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def extract_projects(employee_data):
    project_list = []
    for employee in employee_data:
        for key, value in employee.items():
            project_dict = {}
            if key not in OF_INTEREST:
                if is_float(value) and value != 'nan' and value != '0.0':
                    project_dict['project_id'] = key
                    project_dict['project_hours'] = value
                    add_values_of_interest(project_dict, employee)
                    project_list.append(project_dict)
    return project_list


def calculate(employee_data, journal_data, provision, additional_costs):
    clean_journal_data = erase_unneeded_data(journal_data)
    clean_provision = erase_unneeded_data(provision)
    clean_additional_costs = erase_unneeded_data(additional_costs)
    employee_data = erase_unneeded_employee_data(employee_data)
    employee_data = merge_dicts(employee_data, clean_journal_data)
    employee_data = merge_dicts(employee_data, clean_additional_costs)
    employee_data = merge_dicts(employee_data, clean_provision)
    return extract_projects(employee_data)


def show_debug_infos():
    sheet_name = "25_01"
    year = "25"
    journal_name = "25_01_22 Lohnjournal Januar 2025.xlsx"

    journal_data_file, employee_data_file, provisions_data_file, additional_costs_file = create_file_paths(year, journal_name)
    index = "Pers.Nr."
    ids = [1004, 1032, 1036]
    
    additional_costs = get_list_of_dicts(additional_costs_file, sheet_name, index, ids)
    employee_data = get_list_of_dicts(employee_data_file, sheet_name, index, ids)
    provision = get_list_of_dicts(provisions_data_file, sheet_name, index, ids)
    journal_data = get_list_of_dicts(journal_data_file, "first_sheet", index, ids)

    print(calculate(employee_data, journal_data, provision, additional_costs))

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()