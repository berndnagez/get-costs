

def merge_dicts(first_dict, second_dict):
    merge_result = []
    for employee in first_dict:
        id = employee.get('ID')
        match = [cost for cost in second_dict if cost.get('ID') == id][0]
        employee.update(match)
        merge_result.append(employee)
    return merge_result
