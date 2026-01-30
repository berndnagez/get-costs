from .config import OF_INTEREST, UNNEEDED_EMPLOYEE_DATA, INDEX
from .path_creator import get_paths
from .date_creator import get_sheet_name
from .data_merger import merge_dicts
from data_reader import reader

def erase_unneeded_data(data):
    clean_employee_list = []
    for employee in data:
        clean_employee_dict = {}
        for key, value in employee.items():
            
            #TODO Exception abfangen, falls sich Spaltennamen geändert haben
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



def extract_projects(employee_data):
    projectlist = []
    for employee in employee_data:
        for key, value in employee.items():
            project_dict = {}
            if key not in OF_INTEREST:
                if value != 'nan' and value != '0.0':
                    project_dict['project_id'] = key
                    project_dict['project_hours'] = value
                    add_values_of_interest(project_dict, employee)
                    projectlist.append(project_dict)
    return projectlist


def create_projectlist(employee_data, journal_data, provision, additional_costs):
    clean_journal_data = erase_unneeded_data(journal_data)
    clean_provision = erase_unneeded_data(provision)
    clean_additional_costs = erase_unneeded_data(additional_costs)
    employee_data = erase_unneeded_employee_data(employee_data)
    employee_data = merge_dicts(employee_data, clean_journal_data)
    employee_data = merge_dicts(employee_data, clean_additional_costs)
    employee_data = merge_dicts(employee_data, clean_provision)
    projectlist = extract_projects(employee_data)
    return projectlist


def show_debug_infos():
    journal_data_file, employee_data_file, provisions_data_file, additional_costs_file, result_file_path = get_paths('', '25', '25_09_11 Lohnjournal September 2025.xlsx', '25_09')
    index = INDEX
    sheet_name= get_sheet_name('25_09_11 Lohnjournal September 2025.xlsx')
    ids = [1004, 1156]
    
    journal_data = reader.get_list_of_dicts(journal_data_file, "first_sheet", index, ids)    
    employee_data = reader.get_list_of_dicts(employee_data_file, sheet_name, index, ids)
    provision = reader.get_list_of_dicts(provisions_data_file, sheet_name, index, ids)
    additional_costs = reader.get_list_of_dicts(additional_costs_file, sheet_name, index, ids)

    print(create_projectlist(employee_data, journal_data, provision, additional_costs))

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()