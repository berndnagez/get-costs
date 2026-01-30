from operator import itemgetter
from .date_creator import get_date_object
from .workbook_writer import write
from .config import PROJECT_ID_FORMAT_PROJECTS, DATE_FORMAT_PROJECTS, TEXT_FORMAT_PROJECTS, CURRENCY_FORMAT


def create_new_headline(project_id, date_object, all_rows):
    all_rows.append(([("", TEXT_FORMAT_PROJECTS)]))
    row_data_costs = [
        (project_id, PROJECT_ID_FORMAT_PROJECTS),
        (date_object, DATE_FORMAT_PROJECTS),
        ("", PROJECT_ID_FORMAT_PROJECTS),
        ("", PROJECT_ID_FORMAT_PROJECTS)
    ]
    all_rows.append((row_data_costs))
    return all_rows


def get_row(key, value):
    row = [
        (key, TEXT_FORMAT_PROJECTS),
        ("", TEXT_FORMAT_PROJECTS),
        ("", CURRENCY_FORMAT),
        (value, CURRENCY_FORMAT)
    ]
    return row


def get_all_rows(splitted_values_list, date_object, all_rows):
    splitted_values_list_sorted = sorted(
        splitted_values_list, key=itemgetter('project_id'))
    project_id = ""

    for project in splitted_values_list_sorted:
        if project.get('project_id') != project_id:
            all_rows = create_new_headline(
                project.get('project_id'), date_object, all_rows)
            project_id = project.get('project_id')

        for key, value in project.items():
            if key != 'project_id':
                row = get_row(key, value)
                all_rows.append((row))

    all_rows = {
        "COSTS_SHEET": all_rows
    }
    return all_rows


if __name__ == "__main__":
    splitted_values_list = [
        {'project_id': '0026_comM', 'Gehalt Björn': '=ROUND(-2297.29/24*20.0, 2)', 'Sozialv. Björn': '=ROUND(-469.79/24*20.0, 2)', 'Umlagen Björn': '=ROUND(-65.47/24*20.0, 2)',
         'bAV Björn': '=ROUND(-75.0/24*20.0, 2)', 'Edenred Björn': '=ROUND(-50.0/24*20.0, 2)', 'AU-Erstattung Björn': '=ROUND(237.23/24*20.0, 2)'},
        {'project_id': '0054_comBüse', 'Gehalt Björn': '=ROUND(-2297.29/24*4.0, 2)', 'Sozialv. Björn': '=ROUND(-469.79/24*4.0, 2)', 'Umlagen Björn': '=ROUND(-65.47/24*4.0, 2)',
         'bAV Björn': '=ROUND(-75.0/24*4.0, 2)', 'Edenred Björn': '=ROUND(-50.0/24*4.0, 2)', 'AU-Erstattung Björn': '=ROUND(237.23/24*4.0, 2)'},
        {'project_id': '0005_Präv', 'Gehalt Alan': '=ROUND(-3675.67/40*7.0, 2)', 'Sozialv. Alan': '=ROUND(-749.47/40*7.0, 2)', 'Umlagen Alan': '=ROUND(-142.99/40*7.0, 2)',
         'bAV Alan': '=ROUND(-150.0/40*7.0, 2)', 'HVV Alan': '=ROUND(-46.55/40*7.0, 2)', '1&1 Alan': '=ROUND(-7.99/40*7.0, 2)', 'Edenred Alan': '=ROUND(-50.0/40*7.0, 2)'},
        {'project_id': '0009_Talk about ', 'Gehalt Alan': '=ROUND(-3675.67/40*13.0, 2)', 'Sozialv. Alan': '=ROUND(-749.47/40*13.0, 2)', 'Umlagen Alan': '=ROUND(-142.99/40*13.0, 2)',
         'bAV Alan': '=ROUND(-150.0/40*13.0, 2)', 'HVV Alan': '=ROUND(-46.55/40*13.0, 2)', '1&1 Alan': '=ROUND(-7.99/40*13.0, 2)', 'Edenred Alan': '=ROUND(-50.0/40*13.0, 2)'},
        {'project_id': '0026_comM', 'Gehalt Alan': '=ROUND(-3675.67/40*20.0, 2)', 'Sozialv. Alan': '=ROUND(-749.47/40*20.0, 2)', 'Umlagen Alan': '=ROUND(-142.99/40*20.0, 2)',
         'bAV Alan': '=ROUND(-150.0/40*20.0, 2)', 'HVV Alan': '=ROUND(-46.55/40*20.0, 2)', '1&1 Alan': '=ROUND(-7.99/40*20.0, 2)', 'Edenred Alan': '=ROUND(-50.0/40*20.0, 2)'}
    ]
    all_rows = []
    date = get_date_object("24_01")
    all_rows = get_all_rows(splitted_values_list, date, all_rows)
    border = False
    print(all_rows)
    write("for_Paul", border, all_rows)
