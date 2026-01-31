from operator import itemgetter
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
