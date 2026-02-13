from src.get_costs import employee_data_validator


def test_validate_project_hours_error():
    employee_data = [
        {'id': '1004', 'name': 'Björn Nagel', 'hours': '26.5',
            '0026': '20', '0054': '2.0', '0006': '4.5'},
        {'id': '1032', 'name': 'Alan Roberts',
            'hours': '39', '0026': '23', '0006': '17.0'}
    ]
    path_key = ""
    year = "24"
    sheet_name = "24_01"
    try:
        employee_data_validator.validate_project_hours(
            employee_data, path_key, year, sheet_name)
    except employee_data_validator.ProjectHoursValidationError as e:
        assert f'\nBei Mitarbeiter*in Alan Roberts (ID: 1032) passt die Summe der Projektstunden nicht zu den Gesamtstunden.\n' in str(
            e)
        assert f'Gesamtstunden: 39 Stunden.\n' in str(e)
        assert f'Summe der Projektstunden: 40.0 Stunden.\n' in str(e)
        assert f'Bitte korrigiere das im Tabellenblatt "{sheet_name}" der Datei: "./- 01 Rohdaten Zur Auswertung/2024/employee_data_2024.xlsx" und starte das Programm neu.' in str(
            e)
