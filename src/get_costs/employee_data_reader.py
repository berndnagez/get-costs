import pandas as pd
import get_costs.config
from datetime import datetime




def get_sheet_data(sheet_name, employee_data_file):
    try:
        df = pd.read_excel(employee_data_file, sheet_name,
                           converters={
                               'Projekt 1':str,
                               'Projekt 2':str,
                               'Projekt 3':str,
                               'Projekt 4':str,
                               'Projekt 5':str
                           }
                           )
    except ValueError:
        print(f"Das Tabellenblatt '{sheet_name}' existiert in '{employee_data_file}' nicht. Bitte lege es an und starte das Programm neu.")
        exit('Programmabbruch.')
    
    try:
        df.set_index('ID', inplace=True)
    except KeyError:
        print(f"FEHLER: ID konnte in '{employee_data_file}' nicht gefunden werden.")
        exit('Programmabbruch. Bitte informiere Björn.')
    return df


def get_all_ids_from(sheet_name):
    df = get_sheet_data(sheet_name, get_costs.config.EMPLOYEE_DATA_PATH + sheet_name.split("_")[0] +  ".xlsx")
    all_ids = list(df.index.values)
    return all_ids


def get_data_for(id, df):
    return df.loc[id].values


def get_data_dict_for(id, df):
    data_dict = {}
    data = get_data_for(id, df)
    data_dict['id'] = str(id)
    data_dict['name'] = str(data[0])
    data_dict['hours'] = str(data[1])
    for x in range(2, len(data), 2):
        if str(data[x]) == 'nan': break
        data_dict[data[x]] = str(data[x+1])
    return data_dict


def get_list_of_dicts(sheet_name, ids):
    df = get_sheet_data(sheet_name, get_costs.config.EMPLOYEE_DATA_PATH + sheet_name.split("_")[0] +  ".xlsx")
    list_of_dicts = list()
    for id in ids:
        list_of_dicts.append(get_data_dict_for(id, df))
    return list_of_dicts


def get_date(sheet_name):
    parts_of_sheet_name = sheet_name.split("_")
    year = parts_of_sheet_name[0]
    month = parts_of_sheet_name[1]
    date_str = f'01-{month}-{year}'
    date_object = datetime.strptime(date_str, '%d-%m-%y').date()
    return date_object


def show_debug_infos():
    print(get_all_ids_from("23_02"))
    print(get_list_of_dicts("23_02", [1004, 1032]))
    print(get_date("23_02"))


if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()