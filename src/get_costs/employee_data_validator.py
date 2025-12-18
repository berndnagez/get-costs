import config

def err_mess(employee, sum_project_hours, sheet_name):
    print(f'Bei Mitarbeiter*in {employee.get("name")} (ID: {employee.get("id")}) passt die Summe der Projektstunden nicht zu den Gesamtstunden.')
    print(f'Gesamtstunden: {employee.get("hours")} Stunden.')
    print(f'Summe der Projektstunden: {sum_project_hours} Stunden.')
    print(f'Bitte korrigiere das im Tabellenblatt "{sheet_name}" der Datei: "{config.EMPLOYEE_DATA_PATH}" und starte das Programm neu.')

def validate(employee_data, sheet_name):
    for employee in employee_data:
        sum_project_hours = 0
        hours = float(employee.get("hours"))
        for key, value in employee.items():
            if key not in ["id", "name", "hours"]:
                sum_project_hours += float(employee.get(key))
        if hours != sum_project_hours:
            err_mess(employee, sum_project_hours, sheet_name)
            exit('Programmabbruch.')            

def show_debug_infos():
    validate([{'id': '1004', 'name': 'Björn Nagel', 'hours': '26.5', '0026': '20', '0054': '2.0', '0005': '4.5'}, {'id': '1032', 'name': 'Alan Roberts', 'hours': '39', '0026': '23', '0005': '17.0'}], "24_01")

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()