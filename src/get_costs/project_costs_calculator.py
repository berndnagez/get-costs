import config
from data_merger import merge_dicts
from data_reader import reader

def erase_unneeded_data(data):
    clean_employee_list = []
    for employee in data:
        clean_employee_dict = {}
        for key, value in employee.items():
            
            #TODO Exception abfangen, falls sich Spaltennamen geändert haben
            if key in config.OF_INTEREST:
                clean_employee_dict[key] = value

        clean_employee_list.append(clean_employee_dict)
    return clean_employee_list

def erase_unneeded_employee_data(data):
    clean_employee_list = []
    for employee in data:
        clean_employee_dict = {}
        for key, value in employee.items():
            
            if key not in config.UNNEEDED_EMPLOYEE_DATA:
                clean_employee_dict[key] = value

        clean_employee_list.append(clean_employee_dict)
    return clean_employee_list


def add_values_of_interest(project_dict, employee):
    for key in config.OF_INTEREST:
        project_dict[key] = employee.get(key)
    return project_dict



def extract_projects(employee_data):
    project_list = []
    for employee in employee_data:
        for key, value in employee.items():
            project_dict = {}
            if key not in config.OF_INTEREST:
                if value != 'nan' and value != '0.0':
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
    sheet_name = "24_01"
    file = config.ADDITIONAL_COSTS_PATH + sheet_name.split("_")[0] +  ".xlsx"
    index = "Pers.Nr."
    ids = [1004, 1032]
    
    additional_costs = reader.get_list_of_dicts(file, sheet_name, index, ids)
    
    file_employee_data = config.EMPLOYEE_DATA_PATH + sheet_name.split("_")[0] + ".xlsx"
    employee_data = reader.get_list_of_dicts(file_employee_data, sheet_name, index, ids)

    file_provisions_data = config.PROVISIONS_DATA_PATH + sheet_name.split("_")[0] + ".xlsx"
    provision = reader.get_list_of_dicts(file_provisions_data, sheet_name, index, ids)
    
    file_journal_data = "journal_data/24_12_18 Lohnjournal Dezember 2024.xlsx"
    journal_data = reader.get_list_of_dicts(file_journal_data, "first_sheet", index, ids)


    print(calculate(employee_data, journal_data, provision, additional_costs))

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()