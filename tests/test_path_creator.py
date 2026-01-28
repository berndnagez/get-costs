from src.get_costs import path_creator
import pytest

def test_get_JOURNAL_DATA_PATH():
    expected_path = "../../1036 Siebert und Partner/- 06 Lohnabrechnung _ Journal/2024/- 01 Lohnjournale/24_07_24 Lohnjournal Mai 2024.xlsx"
    key = ""
    year = "24"
    journal_name = "24_07_24 Lohnjournal Mai 2024.xlsx"
    returned_path = path_creator.get_JOURNAL_DATA_PATH(key, year, journal_name)
    assert expected_path == returned_path

    expected_path = "./test_data/journal_data/2025/25_05_21 Lohnjournal Mai 2025.xlsx"
    key = "0026"
    year = "25"
    journal_name = "25_05_21 Lohnjournal Mai 2025.xlsx"
    returned_path = path_creator.get_JOURNAL_DATA_PATH(key, year, journal_name)
    assert expected_path == returned_path

def test_get_EMPLOYEE_DATA_PATH():
    expected_path = "./- 01 Rohdaten Zur Auswertung/2025/employee_data_2025.xlsx"
    key = ""
    year = "25"
    returned_path = path_creator.get_EMPLOYEE_DATA_PATH(key, year)
    assert expected_path == returned_path

    expected_path = "./test_data/raw_data/2025/employee_data_2025.xlsx"
    key = "0026"
    year = "25"
    returned_path = path_creator.get_EMPLOYEE_DATA_PATH(key, year)
    assert expected_path == returned_path

def test_get_ADDITIONAL_COSTS_PATH():
    expected_path = "./- 01 Rohdaten Zur Auswertung/2025/additional_costs_2025.xlsx"
    key = ""
    year = "25"
    returned_path = path_creator.get_ADDITIONAL_COSTS_PATH(key, year)
    assert expected_path == returned_path

    expected_path = "./test_data/raw_data/2025/additional_costs_2025.xlsx"
    key = "0026"
    year = "25"
    returned_path = path_creator.get_ADDITIONAL_COSTS_PATH(key, year)
    assert expected_path == returned_path

def test_get_PROVISIONS_DATA_PATH():
    expected_path = "./- 01 Rohdaten Zur Auswertung/2025/provisions_data_2025.xlsx"
    key = ""
    year = "25"
    returned_path = path_creator.get_PROVISIONS_DATA_PATH(key, year)
    assert expected_path == returned_path

    expected_path = "./test_data/raw_data/2025/provisions_data_2025.xlsx"
    key = "0026"
    year = "25"
    returned_path = path_creator.get_PROVISIONS_DATA_PATH(key, year)
    assert expected_path == returned_path

def test_get_RESULT_FILE_PATH():
    expected_path = "./- 02 Ergebnisse der Auswertung (Monatsweise)/25_01_Kosten_aller_MA_innen"
    key = ""
    year_month_prefix = "25_01"
    returned_path = path_creator.get_RESULT_FILE_PATH(key, year_month_prefix)
    assert expected_path == returned_path

    expected_path = "./output//0026"
    key = "0026"
    year_month_prefix = "25_01"
    returned_path = path_creator.get_RESULT_FILE_PATH(key, year_month_prefix)
    assert expected_path == returned_path

def test_validate_path_exists():
    with pytest.raises(path_creator.PathNotFoundError):
        path_creator.validate_path_exists(["../../test_data/raw_data/2024/24_01_24 MIST Januar 2024.xlsx"])

    path_creator.validate_path_exists(["main.py"])


def test_get_paths():
    expected_journal_data_file = "./test_data/journal_data/2025/25_01_22 Lohnjournal Januar 2025.xlsx"
    expected_employee_data_file = "./test_data/raw_data/2025/employee_data_2025.xlsx"
    expected_provisions_data_file = "./test_data/raw_data/2025/provisions_data_2025.xlsx"
    expected_additional_costs_file = "./test_data/raw_data/2025/additional_costs_2025.xlsx"
    expected_result_file_path = "./output//0026"

    journal_data_file, employee_data_file, provisions_data_file, additional_costs_file, result_file_path = path_creator.get_paths('0026', '25', "25_01_22 Lohnjournal Januar 2025.xlsx", "25_01")
    assert expected_journal_data_file == journal_data_file
    assert expected_employee_data_file == employee_data_file
    assert expected_provisions_data_file == provisions_data_file
    assert expected_additional_costs_file == additional_costs_file
    assert expected_result_file_path == result_file_path