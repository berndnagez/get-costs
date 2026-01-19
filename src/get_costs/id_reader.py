from data_reader import reader
from math import isnan
import config
from path_creator import get_paths

def get_dataframe(file, sheet_name):
    df = reader.get_sheet_data(file, sheet_name, config.INDEX)
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
    journal_data_file, employee_data_file, provisions_data_file, additional_costs_file, result_file_path = get_paths('', '25', '25_09_11 Lohnjournal September 2025.xlsx', '25_09')
    
    # get all IDs for a project
    sheet_name = "25_09"
    print(get_project_ids_from(employee_data_file, sheet_name, "0026"))

    print("---")

    # get all IDs from journal
    print(get_all_ids_from(journal_data_file, "first_sheet"))

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()