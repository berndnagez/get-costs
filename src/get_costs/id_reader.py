from data_reader import reader
from math import isnan
from .config import INDEX


def get_dataframe(file, sheet_name):
    df = reader.get_sheet_data(file, sheet_name, INDEX)
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
