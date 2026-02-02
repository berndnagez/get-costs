from operator import itemgetter
from .date_creator import get_date_object
from .workbook_writer import write
from .config import DATE_FORMAT, CURRENCY_FORMAT_PROJECT, TEXT_FORMAT, TEXT_FORMAT_PROJECTS, TABLE_HEAD_OF_SURCHARGES, TABLE_HEAD_OF_SURCHARGES_RETURN, ID_OF_ACCOUNTING_PERSON, ID_OF_CLEANING_PERSON, TABLE_HEAD_OF_COSTS, TABLE_HEAD_OF_SURCHARGES, TABLE_HEAD_OF_DEFAULT_SHEET, TABLE_FOOTER_OF_COSTS, TABLE_FOOTER_OF_SURCHARGES_SHEET, TABLE_FOOTER_OF_RIDE_COST_SHEET, TABLE_FOOTER_OF_PHONE_SHEET, TABLE_FOOTER_OF_ACCOUNTING_SHEET, TABLE_FOOTER_OF_CLEANING_COAST_SHEET, TABLE_FORMAT_HEAD, get_personal_of, get_contract_num_of, get_sheetnames_of

# TODO ziel muss es sein, eine Methode zu haben, die alle Sheets in folgender Form zurückgibt, also als dict:
# ZIEL:
# project_sheets
# darin müssen alle Zeilen mit den gewünschten Werten sein
# dieses Modul muss die splitted_values_list durchgehen, schauen, ob das gewünschte Projekt dabei ist und die Informationen zum Projekt auf die Sheets verteilen
# dafür erstelle ich erst mal pro Sheet eine Liste
# diese Liste enthält Tuple aus (row_num, cells)
# cells ist wieder eine Liste, die cell-Tuple enthält, die aus (content, format) bestehen
# mit append wird die row an die rows der sheets gehängt

#   EE: vom Ende her aufbauen, bspw. davon ausgehen, dass rows pro Sheet fertig sind und ins Dict packen
# alten Code unten nur zur Orientierung nehmen = alle Methoden neu schreiben

# mit row, rows, cell und cells als Variablennamen arbeiten


def get_job_share(hours):
    job_share = hours/40
    if not int(str(job_share).split('.')[1]) > 9:
        job_share_string = f"{job_share:0,.2f}".replace('.', ',')
    else:
        job_share_string = f"{job_share}".replace('.', ',')
    return job_share_string


def distribute_to_costs_sheet(project, date, row_num):
    row = []
    job_share = get_job_share(float(project.get('project_hours')))
    row.append((date, DATE_FORMAT))
    row.append((project.get('staff_id'), TEXT_FORMAT))
    row.append((f'{job_share} Haustarif',  TEXT_FORMAT))
    row.append((project.get('Gehalt'), CURRENCY_FORMAT_PROJECT))
    row.append((project.get('Sozialv.'), CURRENCY_FORMAT_PROJECT))
    row.append((project.get('bAV'), CURRENCY_FORMAT_PROJECT))
    row.append((f'=SUM(D{row_num}:F{row_num})',  CURRENCY_FORMAT_PROJECT))
    return row


def distribute_to_surcharges_sheet(project, date):
    row = []
    row.append((date, DATE_FORMAT))
    row.append((project.get('staff_id'), TEXT_FORMAT))
    row.append((project.get('U1'), CURRENCY_FORMAT_PROJECT))
    row.append((project.get('U2'), CURRENCY_FORMAT_PROJECT))
    row.append((project.get('InsoU'), CURRENCY_FORMAT_PROJECT))
    return row


def distribute_to_ride_costs_sheet(project, date):
    row = []
    if project.get('HVV') != None:
        row.append((date, DATE_FORMAT))
        id = project.get('staff_id')
        row.append((f'HVV Stellennr. {id}', TEXT_FORMAT_PROJECTS))
        row.append((project.get('HVV'), CURRENCY_FORMAT_PROJECT))
    return row


def distribute_to_phone_sheet(project, date):
    row = []
    id = project.get('staff_id')
    contract_num = get_contract_num_of(id)
    if project.get('1&1') != None:
        row.append((date, DATE_FORMAT))
        row.append((f'1&1 Handy {id} {contract_num}', TEXT_FORMAT_PROJECTS))
        row.append((project.get('1&1'), CURRENCY_FORMAT_PROJECT))
    if project.get('Wetell') != None:
        row.append((date, DATE_FORMAT))
        row.append((f'Wetell Handy {id} {contract_num}', TEXT_FORMAT_PROJECTS))
        row.append((project.get('Wetell'), CURRENCY_FORMAT_PROJECT))
    return row


def distribute_to_accounting_sheet(project, date):
    row = []
    row.append((date, DATE_FORMAT))
    row.append(('interne Buchhaltung', TEXT_FORMAT_PROJECTS))
    row.append((project.get('Gehalt'), CURRENCY_FORMAT_PROJECT))
    return row


def distribute_to_cleaning_coast_sheet(project, date):
    row = []
    row.append((date, DATE_FORMAT))
    row.append(('Reinigung', TEXT_FORMAT_PROJECTS))
    row.append((project.get('Gehalt'), CURRENCY_FORMAT_PROJECT))
    return row


def append_table_head_rows(project_sheets):
    append_row_to('SURCHARGES_RETURN_SHEET', project_sheets,
                  (TABLE_HEAD_OF_SURCHARGES_RETURN))
    append_row_to('COSTS_SHEET_PROJECT', project_sheets, (TABLE_HEAD_OF_COSTS))
    append_row_to('SURCHARGES_SHEET', project_sheets,
                  (TABLE_HEAD_OF_SURCHARGES))
    append_row_to('RIDE_COST_SHEET', project_sheets,
                  (TABLE_HEAD_OF_DEFAULT_SHEET))
    append_row_to('PHONE_SHEET', project_sheets, (TABLE_HEAD_OF_DEFAULT_SHEET))
    append_row_to('ACCOUNTING_SHEET', project_sheets,
                  (TABLE_HEAD_OF_DEFAULT_SHEET))
    append_row_to('CLEANING_COAST_SHEET', project_sheets,
                  (TABLE_HEAD_OF_DEFAULT_SHEET))
    return project_sheets


def distribute_values_to_sheets(splitted_values_list, project_id, date, project_sheets):
    # damit nur der Tabellenkopf geschrieben wird, wenn es noch keinen gibt
    if not project_sheets['COSTS_SHEET_PROJECT']:
        append_table_head_rows(project_sheets)

    for project in splitted_values_list:
        if project_id in project.get('project_id'):
            row_num = get_last_row_num_of(
                project_sheets['COSTS_SHEET_PROJECT']) + 1
            if project.get('staff_id') in get_personal_of(project_id) and project.get('staff_id') != ID_OF_ACCOUNTING_PERSON and project.get('staff_id') != ID_OF_CLEANING_PERSON:
                # 'SURCHARGES_RETURN_SHEET'
                # TODO noch mal ansehen, wie das mit den Erstattungen ist, es kann mehrere pro Monat geben
                # evt. als Überbrückung als Dict in die additional_costs schreiben und später hier verteilen?
                append_row_to('COSTS_SHEET_PROJECT', project_sheets,
                              distribute_to_costs_sheet(project, date, row_num))
                append_row_to('SURCHARGES_SHEET', project_sheets,
                              distribute_to_surcharges_sheet(project, date))
                append_row_to('RIDE_COST_SHEET', project_sheets,
                              distribute_to_ride_costs_sheet(project, date))
                append_row_to('PHONE_SHEET', project_sheets,
                              distribute_to_phone_sheet(project, date))
            if project.get('staff_id') == ID_OF_ACCOUNTING_PERSON:
                append_row_to('ACCOUNTING_SHEET', project_sheets,
                              distribute_to_accounting_sheet(project, date))
            if project.get('staff_id') == ID_OF_CLEANING_PERSON:
                append_row_to('CLEANING_COAST_SHEET', project_sheets,
                              distribute_to_cleaning_coast_sheet(project, date))


def create_project_sheets(sheet_names):
    project_sheets = {}
    for sheet_name in sheet_names:
        project_sheets[sheet_name] = []
    return project_sheets


def append_row_to(sheet_name, project_sheets, row):
    project_sheets.get(sheet_name).append(row)
    return project_sheets


def remove_empty_rows(project_sheets):
    corrected_project_sheets = {}
    for sheet_name, data in project_sheets.items():
        data = [i for i in data if i]
        corrected_project_sheets[sheet_name] = data
    return corrected_project_sheets


def get_last_row_num_of(sheet):
    last_row_num = len(sheet)
    return last_row_num


def add_last_row(project_sheets):
    last_row_num = get_last_row_num_of(project_sheets['COSTS_SHEET_PROJECT'])
    TABLE_FOOTER_OF_COSTS.append(
        (f'=SUM(G2:G{last_row_num})', TABLE_FORMAT_HEAD))

    last_row_num = get_last_row_num_of(project_sheets['SURCHARGES_SHEET'])
    TABLE_FOOTER_OF_SURCHARGES_SHEET.extend([
        (f'=SUM(C2:C{last_row_num})', TABLE_FORMAT_HEAD),
        (f'=SUM(D2:D{last_row_num})', TABLE_FORMAT_HEAD),
        (f'=SUM(E2:E{last_row_num})', TABLE_FORMAT_HEAD)
    ])

    last_row_num = get_last_row_num_of(project_sheets['RIDE_COST_SHEET'])
    TABLE_FOOTER_OF_RIDE_COST_SHEET.append(
        (f'=SUM(C2:C{last_row_num})', TABLE_FORMAT_HEAD))

    last_row_num = get_last_row_num_of(project_sheets['PHONE_SHEET'])
    TABLE_FOOTER_OF_PHONE_SHEET.append(
        (f'=SUM(C2:C{last_row_num})', TABLE_FORMAT_HEAD))

    last_row_num = get_last_row_num_of(project_sheets['ACCOUNTING_SHEET'])
    TABLE_FOOTER_OF_ACCOUNTING_SHEET.append(
        (f'=SUM(C2:C{last_row_num})', TABLE_FORMAT_HEAD))

    last_row_num = get_last_row_num_of(project_sheets['CLEANING_COAST_SHEET'])
    TABLE_FOOTER_OF_CLEANING_COAST_SHEET.append(
        (f'=SUM(C2:C{last_row_num})', TABLE_FORMAT_HEAD))

    append_row_to('COSTS_SHEET_PROJECT', project_sheets, TABLE_FOOTER_OF_COSTS)
    append_row_to('SURCHARGES_SHEET', project_sheets,
                  TABLE_FOOTER_OF_SURCHARGES_SHEET)
    append_row_to('RIDE_COST_SHEET', project_sheets,
                  TABLE_FOOTER_OF_RIDE_COST_SHEET)
    append_row_to('PHONE_SHEET', project_sheets, TABLE_FOOTER_OF_PHONE_SHEET)
    append_row_to('ACCOUNTING_SHEET', project_sheets,
                  TABLE_FOOTER_OF_ACCOUNTING_SHEET)
    append_row_to('CLEANING_COAST_SHEET', project_sheets,
                  TABLE_FOOTER_OF_CLEANING_COAST_SHEET)
