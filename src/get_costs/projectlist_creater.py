from .config import OF_INTEREST, UNNEEDED_EMPLOYEE_DATA
from .data_merger import merge_dicts


def erase_unneeded_data(data):
    clean_employee_list = []
    for employee in data:
        clean_employee_dict = {}
        for key, value in employee.items():

            # TODO Exception abfangen, falls sich Spaltennamen geändert haben
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
