from operator import itemgetter
from date_creator import get_date_object
from workbook_writer import write
import config

#TODO ziel muss es sein, eine Methode zu haben, die alle Sheets in folgender Form zurückgibt, also als dict:
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
    row.append((date, config.DATE_FORMAT))
    row.append((project.get('staff_id'), config.TEXT_FORMAT))
    row.append((f'{job_share} Haustarif',  config.TEXT_FORMAT))
    row.append((project.get('Gehalt'), config.CURRENCY_FORMAT_PROJECT))
    row.append((project.get('Sozialv.'), config.CURRENCY_FORMAT_PROJECT))
    row.append((project.get('bAV'), config.CURRENCY_FORMAT_PROJECT))
    row.append((f'=SUM(D{row_num}:F{row_num})',  config.CURRENCY_FORMAT_PROJECT))
    return row


def distribute_to_surcharges_sheet(project, date):
    row = []
    row.append((date, config.DATE_FORMAT))    
    row.append((project.get('staff_id'), config.TEXT_FORMAT))
    row.append((project.get('U1'), config.CURRENCY_FORMAT_PROJECT))
    row.append((project.get('U2'), config.CURRENCY_FORMAT_PROJECT))
    row.append((project.get('InsoU'), config.CURRENCY_FORMAT_PROJECT))
    return row


def distribute_to_ride_costs_sheet(project, date):
    row = []
    if project.get('HVV') != None:
        row.append((date, config.DATE_FORMAT))
        id = project.get('staff_id')
        row.append((f'HVV Stellennr. {id}', config.TEXT_FORMAT_PROJECTS))
        row.append((project.get('HVV'), config.CURRENCY_FORMAT_PROJECT))
    return row


def distribute_to_phone_sheet(project, date):
    row = []
    id = project.get('staff_id')
    contract_num = config.get_contract_num_of(id)
    if project.get('1&1') != None:
        row.append((date, config.DATE_FORMAT))        
        row.append((f'1&1 Handy {id} {contract_num}', config.TEXT_FORMAT_PROJECTS))
        row.append((project.get('1&1'), config.CURRENCY_FORMAT_PROJECT))
    if project.get('Wetell') != None:
        row.append((date, config.DATE_FORMAT))
        row.append((f'Wetell Handy {id} {contract_num}', config.TEXT_FORMAT_PROJECTS))
        row.append((project.get('Wetell'), config.CURRENCY_FORMAT_PROJECT))
    return row


def distribute_to_accounting_sheet(project, date):
    row = []
    row.append((date, config.DATE_FORMAT))
    row.append(('interne Buchhaltung', config.TEXT_FORMAT_PROJECTS))
    row.append((project.get('Gehalt'), config.CURRENCY_FORMAT_PROJECT))
    return row


def distribute_to_cleaning_coast_sheet(project, date):
    row = []
    row.append((date, config.DATE_FORMAT))
    row.append(('Reinigung', config.TEXT_FORMAT_PROJECTS))
    row.append((project.get('Gehalt'), config.CURRENCY_FORMAT_PROJECT))
    return row


def append_table_head_rows(project_sheets):
    append_row_to('SURCHARGES_RETURN_SHEET', project_sheets, (config.TABLE_HEAD_OF_SURCHARGES_RETURN))
    append_row_to('COSTS_SHEET_PROJECT', project_sheets, (config.TABLE_HEAD_OF_COSTS))
    append_row_to('SURCHARGES_SHEET', project_sheets, (config.TABLE_HEAD_OF_SURCHARGES))
    append_row_to('RIDE_COST_SHEET', project_sheets, (config.TABLE_HEAD_OF_DEFAULT_SHEET))
    append_row_to('PHONE_SHEET', project_sheets, (config.TABLE_HEAD_OF_DEFAULT_SHEET))
    append_row_to('ACCOUNTING_SHEET', project_sheets, (config.TABLE_HEAD_OF_DEFAULT_SHEET))
    append_row_to('CLEANING_COAST_SHEET', project_sheets, (config.TABLE_HEAD_OF_DEFAULT_SHEET))
    return project_sheets


def distribute_values_to_sheets(splitted_values_list, project_id, date, project_sheets):
    # damit nur der Tabellenkopf geschrieben wird, wenn es noch keinen gibt
    if not project_sheets['COSTS_SHEET_PROJECT']:
        append_table_head_rows(project_sheets)

    for project in splitted_values_list:
        if project_id in project.get('project_id'):                
            row_num = get_last_row_num_of(project_sheets['COSTS_SHEET_PROJECT']) +1
            if project.get('staff_id') in config.get_personal_of(project_id) and project.get('staff_id') != config.ID_OF_ACCOUNTING_PERSON and project.get('staff_id') != config.ID_OF_CLEANING_PERSON:
                # 'SURCHARGES_RETURN_SHEET'
                # TODO noch mal ansehen, wie das mit den Erstattungen ist, es kann mehrere pro Monat geben
                # evt. als Überbrückung als Dict in die additional_costs schreiben und später hier verteilen?
                append_row_to('COSTS_SHEET_PROJECT', project_sheets, distribute_to_costs_sheet(project, date, row_num))
                append_row_to('SURCHARGES_SHEET', project_sheets, distribute_to_surcharges_sheet(project, date))
                append_row_to('RIDE_COST_SHEET', project_sheets, distribute_to_ride_costs_sheet(project, date))
                append_row_to('PHONE_SHEET', project_sheets, distribute_to_phone_sheet(project, date))
            if project.get('staff_id') == config.ID_OF_ACCOUNTING_PERSON:
                append_row_to('ACCOUNTING_SHEET', project_sheets, distribute_to_accounting_sheet(project, date))
            if project.get('staff_id') == config.ID_OF_CLEANING_PERSON:
                append_row_to('CLEANING_COAST_SHEET', project_sheets, distribute_to_cleaning_coast_sheet(project, date))


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
    config.TABLE_FOOTER_OF_COSTS.append((f'=SUM(G2:G{last_row_num })', config.TABLE_FORMAT_HEAD))

    last_row_num = get_last_row_num_of(project_sheets['SURCHARGES_SHEET'])
    config.TABLE_FOOTER_OF_SURCHARGES_SHEET.extend([
        (f'=SUM(C2:C{last_row_num})', config.TABLE_FORMAT_HEAD),
        (f'=SUM(D2:D{last_row_num})', config.TABLE_FORMAT_HEAD),
        (f'=SUM(E2:E{last_row_num})', config.TABLE_FORMAT_HEAD)
    ])

    last_row_num = get_last_row_num_of(project_sheets['RIDE_COST_SHEET'])
    config.TABLE_FOOTER_OF_RIDE_COST_SHEET.append((f'=SUM(C2:C{last_row_num})', config.TABLE_FORMAT_HEAD))

    last_row_num = get_last_row_num_of(project_sheets['PHONE_SHEET'])
    config.TABLE_FOOTER_OF_PHONE_SHEET.append((f'=SUM(C2:C{last_row_num})', config.TABLE_FORMAT_HEAD))

    last_row_num = get_last_row_num_of(project_sheets['ACCOUNTING_SHEET'])
    config.TABLE_FOOTER_OF_ACCOUNTING_SHEET.append((f'=SUM(C2:C{last_row_num})', config.TABLE_FORMAT_HEAD))

    last_row_num = get_last_row_num_of(project_sheets['CLEANING_COAST_SHEET'])
    config.TABLE_FOOTER_OF_CLEANING_COAST_SHEET.append((f'=SUM(C2:C{last_row_num})', config.TABLE_FORMAT_HEAD))

    append_row_to('COSTS_SHEET_PROJECT', project_sheets, config.TABLE_FOOTER_OF_COSTS)
    append_row_to('SURCHARGES_SHEET', project_sheets, config.TABLE_FOOTER_OF_SURCHARGES_SHEET)
    append_row_to('RIDE_COST_SHEET', project_sheets, config.TABLE_FOOTER_OF_RIDE_COST_SHEET)
    append_row_to('PHONE_SHEET', project_sheets, config.TABLE_FOOTER_OF_PHONE_SHEET)
    append_row_to('ACCOUNTING_SHEET', project_sheets, config.TABLE_FOOTER_OF_ACCOUNTING_SHEET)
    append_row_to('CLEANING_COAST_SHEET', project_sheets, config.TABLE_FOOTER_OF_CLEANING_COAST_SHEET)


if __name__ == "__main__":
    splitted_values_list = [
        {'project_id': '0026_comM', 'staff_id': '1004', 'project_hours': '20.0', 'Gehalt': '=ROUND(2297.29/24*20.0, 2)', 'Sozialv.': '=ROUND(469.79/24*20.0, 2)', 'U1': '=ROUND(55.13/24*20.0, 2)', 'U2': '=ROUND(8.96/24*20.0, 2)', 'InsoU': '=ROUND(1.38/24*20.0, 2)', 'bAV': '=ROUND(75.0/24*20.0, 2)', 'AU-Erstattung': '=ROUND(237.23/24*20.0, 2)'},
        {'project_id': '0054_comBüse', 'staff_id': '1004', 'project_hours': '4.0', 'Gehalt': '=ROUND(2297.29/24*4.0, 2)', 'Sozialv.': '=ROUND(469.79/24*4.0, 2)', 'U1': '=ROUND(55.13/24*4.0, 2)', 'U2': '=ROUND(8.96/24*4.0, 2)', 'InsoU': '=ROUND(1.38/24*4.0, 2)', 'bAV': '=ROUND(75.0/24*4.0, 2)', 'AU-Erstattung': '=ROUND(237.23/24*4.0, 2)'},
        {'project_id': '0005_Präv', 'staff_id': '1032', 'project_hours': '7.0', 'Gehalt': '=ROUND(3675.67/40*7.0, 2)', 'Sozialv.': '=ROUND(749.47/40*7.0, 2)', 'U1': '=ROUND(124.97/40*7.0, 2)', 'U2': '=ROUND(15.81/40*7.0, 2)', 'InsoU': '=ROUND(2.21/40*7.0, 2)', 'bAV': '=ROUND(150.0/40*7.0, 2)', 'HVV': '=ROUND(46.55/40*7.0, 2)', '1&1': '=ROUND(7.99/40*7.0, 2)'},
        {'project_id': '0009_Talk about ', 'staff_id': '1032', 'project_hours': '13.0', 'Gehalt': '=ROUND(3675.67/40*13.0, 2)', 'Sozialv.': '=ROUND(749.47/40*13.0, 2)', 'U1': '=ROUND(124.97/40*13.0, 2)', 'U2': '=ROUND(15.81/40*13.0, 2)', 'InsoU': '=ROUND(2.21/40*13.0, 2)', 'bAV': '=ROUND(150.0/40*13.0, 2)', 'HVV': '=ROUND(46.55/40*13.0, 2)', '1&1': '=ROUND(7.99/40*13.0, 2)'},
        {'project_id': '0026_comM', 'staff_id': '1032', 'project_hours': '20.0', 'Gehalt': '=ROUND(3675.67/40*20.0, 2)', 'Sozialv.': '=ROUND(749.47/40*20.0, 2)', 'U1': '=ROUND(124.97/40*20.0, 2)', 'U2': '=ROUND(15.81/40*20.0, 2)', 'InsoU': '=ROUND(2.21/40*20.0, 2)', 'bAV': '=ROUND(150.0/40*20.0, 2)', 'HVV': '=ROUND(46.55/40*20.0, 2)', '1&1': '=ROUND(7.99/40*20.0, 2)'},
        {'project_id': '0026_comM', 'staff_id': '1028', 'project_hours': '20.0', 'Gehalt': '=899.47*32.34%'},
        {'project_id': '0026_comM', 'staff_id': '1035', 'project_hours': '10.0', 'Gehalt': '=ROUND(4621.6900000000005/20*10, 2)*32.34%'}
        ]
    
    splitted_values_list = [
        {'project_id': '0026_comM', 'staff_id': '1004', 'project_hours': '20.0', 'Gehalt': '=ROUND(2297.29/24*20.0, 2)', 'Sozialv.': '=ROUND(469.79/24*20.0, 2)', 'U1': '=ROUND(55.13/24*20.0, 2)', 'U2': '=ROUND(8.96/24*20.0, 2)', 'InsoU': '=ROUND(1.38/24*20.0, 2)', 'bAV': '=ROUND(75.0/24*20.0, 2)', 'AU-Erstattung': '=ROUND(237.23/24*20.0, 2)'}
        ]
    project_id = workbook_name = '0026'
    project_sheets = create_project_sheets(config.get_sheetnames_of(project_id))
    distribute_values_to_sheets(splitted_values_list, project_id, get_date_object("24_01"), project_sheets)
    print(project_sheets)
    project_sheets = remove_empty_rows(project_sheets)
    add_last_row(project_sheets)
    border = True
    write(workbook_name, border, project_sheets)