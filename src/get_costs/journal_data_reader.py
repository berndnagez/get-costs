import pandas as pd
import config
from pathlib import Path


class SheetNotFoundError(Exception):
    pass


def get_data_frame(filename):
    df = get_sheet(filename)

    try:
        df.set_index('Pers.Nr.', inplace=True)
    except KeyError:
        print(
            f'FEHLER: "Pers.Nr." konnte in "{filename}" nicht gefunden werden.')
        exit('Programmabbruch. Bitte informiere Björn.')
    return df


def get_sheet(filename):
    xl = pd.ExcelFile(filename)
    sheet_names = xl.sheet_names

    filename_parts = Path(filename).stem.split(" ")
    sheet_name = " ".join(filename_parts[len(filename_parts) - 2:])

    if len(sheet_names) > 1:
        if not sheet_name in sheet_names:
            raise SheetNotFoundError(
                f"Sheet '{sheet_name}' not found in document '{filename}'!")
    else:
        if not sheet_name == sheet_names[0]:
            print(f"WARN: In '{filename}' using sheet '{sheet_names[0]}'.")
        sheet_name = sheet_names[0]
    return xl.parse(sheet_name)


def get_cell_value(file, df, personal_num, column_name):
    try:
        cell_value = df.loc[personal_num, column_name]
        if cell_value == 0.0 and column_name == 'St.Brutto - Steuerbrutto':
            cell_value = df.loc[personal_num,
                                'BezPausch - Pauschal versteuerte Bezüge']
        return cell_value
    except KeyError:
        print(
            f'FEHLER: "{personal_num}" oder "{column_name}" konnte in "{file}" nicht gefunden werden.')
        print('Programmabbruch. Bitte informiere Björn.')
        raise


def get_sum_of_social_insurance(file, df, personal_num):
    sum_of_social_insurance = 0
    for column in config.COMPONENTS_OF_SOCIAL_INSURANCE:
        sum_of_social_insurance += get_cell_value(
            file, df, personal_num, column)
    return sum_of_social_insurance


def get_all_values_of_employee(file, df, personal_num, columns):
    all_values = {'id': personal_num}
    for key, value in columns.items():
        all_values[key] = (get_cell_value(file, df, personal_num, value))
        if key == "Entgelt":
            all_values['Sozialvers.'] = (
                get_sum_of_social_insurance(file, df, personal_num))
    return all_values


def get_values_of_all_employees(file, df, nums, column_names_of_interest):
    all_employees = []
    for num in nums:
        all_employees.append(get_all_values_of_employee(
            file, df, num, column_names_of_interest))
    return all_employees

# returns a list of dicts


def get_values_from(file, personal_nums):
    df = get_data_frame(f'{config.JOURNAL_DATA_PATH}/{file}')
    return get_values_of_all_employees(file, df, personal_nums, config.COLUMN_NAMES_OF_INTEREST)


def show_debug_infos():
    print(get_values_from(
        "23_05_24 Lohnjournal Mai 2023.xlsx", [1004, 1007, 1028]))


if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()
