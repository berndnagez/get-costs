from .path_creator import get_paths
from data_reader import reader

def merge_dicts(first_dict, second_dict):
    merge_result = []
    for employee in first_dict:
        id = employee.get('ID')
        match = [cost for cost in second_dict if cost.get('ID') == id][0]
        employee.update(match)
        merge_result.append(employee)
    return merge_result

def show_debug_infos():
    sheet_name = "24_01"
    journal_data_file, employee_data_file, provisions_data_file, additional_costs_file, result_file_path = get_paths('', '25', '25_09_11 Lohnjournal September 2025.xlsx', '25_09')
    index = "Pers.Nr."
    ids = [1004, 1032]
    
    additional_costs = reader.get_list_of_dicts(additional_costs_file, sheet_name, index, ids)
    
    employee_data = reader.get_list_of_dicts(employee_data_file, sheet_name, index, ids)

    employee_data = merge_dicts(employee_data, additional_costs)

    provision = reader.get_list_of_dicts(provisions_data_file, sheet_name, index, ids)

    employee_data = merge_dicts(employee_data, provision)

    print(employee_data)

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()