from .path_creator import get_EMPLOYEE_DATA_PATH


class ProjectHoursValidationError(Exception):
    def __init__(self, employee, sum_project_hours, path_key, year, sheet_name):
        employee_data_path = get_EMPLOYEE_DATA_PATH(path_key, year)
        message = (
            f'\n\nBei Mitarbeiter*in {employee.get("name")} (ID: {employee.get("id")}) passt die Summe der Projektstunden nicht zu den Gesamtstunden.\n'
            f'Gesamtstunden: {employee.get("hours")} Stunden.\n'
            f'Summe der Projektstunden: {sum_project_hours} Stunden.\n'
            f'Bitte korrigiere das im Tabellenblatt "{sheet_name}" der Datei: "{employee_data_path}" und starte das Programm neu.'
        )
        self.message = message
        super().__init__(self.message)
    pass


def validate_project_hours(employee_data, path_key, year, sheet_name):
    for employee in employee_data:
        sum_project_hours = 0
        hours = float(employee.get("hours"))
        for key, value in employee.items():
            if key not in ["id", "name", "hours"]:
                sum_project_hours += float(employee.get(key))
        if hours != sum_project_hours:
            raise ProjectHoursValidationError(
                employee, sum_project_hours, path_key, year, sheet_name)
