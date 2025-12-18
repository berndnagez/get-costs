import path_creator
import pytest

def test_get_JOURNAL_DATA_PATH():
    expected_path = "../../1036 Siebert und Partner/- 06 Lohnabrechnung _ Journal/2024/- 01 Lohnjournale/24_07_24 Lohnjournal Mai 2024.xlsx"
    key = ""
    year = "24"
    journal_name = "24_07_24 Lohnjournal Mai 2024.xlsx"
    returned_path = path_creator.get_JOURNAL_DATA_PATH(key, year, journal_name)
    assert expected_path == returned_path

    expected_path = "./journal_data/24_07_24 Lohnjournal Mai 2024.xlsx"
    key = "0026"
    year = "24"
    journal_name = "24_07_24 Lohnjournal Mai 2024.xlsx"
    returned_path = path_creator.get_JOURNAL_DATA_PATH(key, year, journal_name)
    assert expected_path == returned_path

def test_get_EMPLOYEE_DATA_PATH():
    expected_path = "./- 01 Rohdaten Zur Auswertung/employee_data_2024.xlsx"
    key = ""
    year = "24"
    returned_path = path_creator.get_EMPLOYEE_DATA_PATH(key, year)
    assert expected_path == returned_path

    expected_path = "./data/employee_data_2024.xlsx"
    key = "0026"
    year = "24"
    returned_path = path_creator.get_EMPLOYEE_DATA_PATH(key, year)
    assert expected_path == returned_path

def test_get_ADDITIONAL_COSTS_PATH():
    expected_path = "./- 01 Rohdaten Zur Auswertung/additional_costs_2024.xlsx"
    key = ""
    year = "24"
    returned_path = path_creator.get_ADDITIONAL_COSTS_PATH(key, year)
    assert expected_path == returned_path

    expected_path = "./data/additional_costs_2024.xlsx"
    key = "0026"
    year = "24"
    returned_path = path_creator.get_ADDITIONAL_COSTS_PATH(key, year)
    assert expected_path == returned_path

def test_get_PROVISIONS_DATA_PATH():
    expected_path = "./- 01 Rohdaten Zur Auswertung/provisions_data_2024.xlsx"
    key = ""
    year = "24"
    returned_path = path_creator.get_PROVISIONS_DATA_PATH(key, year)
    assert expected_path == returned_path

    expected_path = "./data/provisions_data_2024.xlsx"
    key = "0026"
    year = "24"
    returned_path = path_creator.get_PROVISIONS_DATA_PATH(key, year)
    assert expected_path == returned_path


def test_get_RESULT_FILE_PATH():
    expected_path = "./- 02 Ergebnisse der Auswertung (Monatsweise)/24_01_Kosten_aller_MA_innen"
    key = ""
    year_month_prefix = "24_01"
    returned_path = path_creator.get_RESULT_FILE_PATH(key, year_month_prefix)
    assert expected_path == returned_path

    expected_path = "./0026"
    key = "0026"
    year_month_prefix = "24_01"
    returned_path = path_creator.get_RESULT_FILE_PATH(key, year_month_prefix)
    assert expected_path == returned_path

def test_validate_path_exists():
    with pytest.raises(path_creator.PathNotFoundError):
        path_creator.validate_path_exists(["./data/24_01_24 MIST Januar 2024.xlsx"])

    path_creator.validate_path_exists(["get_projects_costs.py"])


def test_get_paths():
    expected_journal_data_file = "./journal_data/23_04_26 Lohnjournal April 2023.xlsx"
    expected_employee_data_file = "./data/employee_data_2024.xlsx"
    expected_provisions_data_file = "./data/provisions_data_2024.xlsx"
    expected_additional_costs_file = "./data/provisions_data_2024.xlsx"
    expected_result_file_path = "./0026"

    journal_data_file, employee_data_file, provisions_data_file , additional_costs_file, result_file_path = path_creator.get_paths('0026', '24', "23_04_26 Lohnjournal April 2023.xlsx", "24_01")
    assert expected_journal_data_file == journal_data_file
    assert expected_employee_data_file == employee_data_file
    assert expected_provisions_data_file == provisions_data_file
    assert expected_additional_costs_file == additional_costs_file
    assert expected_result_file_path == result_file_path