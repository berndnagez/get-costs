from .data_reader import get_sheet_data
from math import isnan
import get_costs.config

def get_dataframe(file, sheet_name):
    df = get_sheet_data(file, sheet_name, get_costs.config.INDEX)
    return df

def get_all_ids_from(file, sheet_name):
    df = get_dataframe(file, sheet_name)
    all_ids = list(df.index.values)
    return all_ids


def get_project_ids_from(file, sheet_name, project):
    project_ids = []
    df = get_dataframe(file, sheet_name)
    dicts = df.to_dict('dict')

    for column_name, column_values in dicts.items():
        if project in column_name:
            for id, hours in column_values.items():
                if not isnan(hours):
                    project_ids.append(id)    
    return project_ids

def show_debug_infos():
    sheet_name = "24_01"
    file = "employee_data_2024.xlsx"
    print(get_all_ids_from(file, sheet_name))
    print(get_project_ids_from(file, sheet_name, "0026"))


if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()