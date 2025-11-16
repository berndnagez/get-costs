import pandas as pd
import get_costs.config
import numpy as np

# TODO geht z.Z. davon aus, dass sheet_name bekannt ist, wenn nicht, weil evtl. wie beim Lohnjournal wechselnd: siehe journal_data_reader = wie hat Falk es da gemacht (sonst dürfe er sich nicht unterscheiden)
def get_sheet_data(file, sheet_name, index):

    if sheet_name == "first_sheet":
        df = pd.read_excel(file)
    else:
        try:
            df = pd.read_excel(file, sheet_name)
        except ValueError:
            print(f"Das Tabellenblatt '{sheet_name}' existiert in '{file}' nicht. Bitte lege es an und starte das Programm neu.")
            exit('Programmabbruch.')
    
    try:
        df.set_index(index, inplace=True)
    except KeyError:
        print(f"FEHLER: '{index}' konnte in '{file}' nicht gefunden werden.")
        exit('Programmabbruch. Bitte informiere Björn.')
    return df

def get_data_for(file, id, df):
    try:
        values = df.loc[id].values
        return values
    except KeyError:
        print(f'HINWEIS: In der Datei "{file}" konnten für die ID "{id}" keine Werte gefunden werden.')
        print(f'Deshalb wurden alle Werte für diese ID auf 0,00 Euro gesetzt und keine Kosten die ID "{id}" in die Ergebnissetabelle übernommen.\n')
        return np.array([])


def get_column_names(df):
    column_names = []
    for col in df.columns:
        column_names.append(col)
    return column_names

# TODO den ganzen dict-Erstellungskram kann ich viel geilder machen, siehe id_reader und https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary
def get_data_dict_for(file, id, df):
    data_dict = {}
    iterator = 0
    data = get_data_for(file, id, df)
    #data = np.array([])
    data_dict['ID'] = str(id)
    if data.size == 0:
        for key in get_column_names(df):
            data_dict[key] = str(0.00)
    else:
        for key in get_column_names(df):
            data_dict[key] = str(data[iterator])
            iterator += 1
    return data_dict


def get_list_of_dicts(file, sheet_name, index, ids):
    df = get_sheet_data(file, sheet_name, index)
    list_of_dicts = list()
    for id in ids:
        list_of_dicts.append(get_data_dict_for(file, id, df))
    return list_of_dicts


def show_debug_infos():
    sheet_name = "24_01"
    file = get_costs.config.ADDITIONAL_COSTS_PATH + sheet_name.split("_")[0] +  ".xlsx"
    index = "Pers.Nr."
    ids = [1004, 1032]

    #print(get_all_ids_from(file, sheet_name, index))
    #print(get_list_of_dicts(file, sheet_name, index, ids))

    file_employee_data = get_costs.config.EMPLOYEE_DATA_PATH + sheet_name.split("_")[0] + ".xlsx"
    #print(get_list_of_dicts(file_employee_data, sheet_name, index, ids))

    file_provisions_data = get_costs.config.PROVISIONS_DATA_PATH + sheet_name.split("_")[0] + ".xlsx"
    #print(get_list_of_dicts(file_provisions_data, sheet_name, index, ids))

    print("Lohnjournal-Daten:")
    file_journal_data = "data/23_12_20 Lohnjournal Dezember 2023.xlsx"
    print(get_list_of_dicts(file_journal_data, "first_sheet", index, ids))

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()