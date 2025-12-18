import config
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
    file = config.ADDITIONAL_COSTS_PATH + sheet_name.split("_")[0] +  ".xlsx"
    index = "Pers.Nr."
    ids = [1004, 1032]
    
    additional_costs = reader.get_list_of_dicts(file, sheet_name, index, ids)
    
    file_employee_data = config.EMPLOYEE_DATA_PATH + sheet_name.split("_")[0] + ".xlsx"
    employee_data = reader.get_list_of_dicts(file_employee_data, sheet_name, index, ids)

    employee_data = merge_dicts(employee_data, additional_costs)

    file_provisions_data = config.PROVISIONS_DATA_PATH + sheet_name.split("_")[0] + ".xlsx"
    provision = reader.get_list_of_dicts(file_provisions_data, sheet_name, index, ids)

    employee_data = merge_dicts(employee_data, provision)

    print(employee_data)

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()