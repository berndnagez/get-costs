INDEX = "Pers.Nr."

OF_INTEREST = [
    'ID',
    'Name',
    'Wochenstd',
    'St.Brutto - Steuerbrutto',
    'BezPausch - Pauschal versteuerte Bezüge',
    'U1 - Umlage 1',
    'U2 - Umlage 2',
    'InsoU - Insolvenzgeldumlage',
    'KV-AG-Beitrag',
    'RV-AG-Beitrag',
    'AV-AG-Beitrag',
    'PV-AG-Beitrag',
    'bAV AG-Anteil',
    'HVV',
    '1&1',
    'Wetell',
    'Edenred',
    'Urban Sports',
    'AU-Erstattung'
    ]

UNNEEDED_EMPLOYEE_DATA = ['Kontrolle']

# ich mache mir hier super viel Arbeit, um mit verschieden Pfaden arbeiten zu können (siehe auch path_creater.py, der das hier verwendet)
# Idee: hätte ich eine GUI, könnte ich einfach die Auswahl der Dateien erzwingen und müsste mich nicht um die verschiedenen Orte kümmern
# TODO: GUI bauen, file-Auswahl programmieren und diesen Teil ersetzen
def get_paths_for(id):
    paths = {}
    paths[''] = {
        'JOURNAL_DATA_PATH': "../../1036 Siebert und Partner/- 06 Lohnabrechnung _ Journal",
        'RAW_DATA_PATH': "./- 01 Rohdaten Zur Auswertung",
        'RESULT_FILE_PATH': "./- 02 Ergebnisse der Auswertung (Monatsweise)"
    }
    paths['0002'] = {
        'JOURNAL_DATA_PATH': "../../test_data/journal_data",
        'RAW_DATA_PATH': "../../test_data/raw_data",
        'RESULT_FILE_PATH': "../../output/"
    }
    paths['0006'] = {
        'JOURNAL_DATA_PATH': "../../test_data/journal_data",
        'RAW_DATA_PATH': "../../test_data/raw_data",
        'RESULT_FILE_PATH': "../../output/"
    }
    paths['0026'] = {
        'JOURNAL_DATA_PATH': "../../test_data/journal_data",
        'RAW_DATA_PATH': "../../test_data/raw_data",
        'RESULT_FILE_PATH': "../../output/"
    }
    paths['0054'] = {
        'JOURNAL_DATA_PATH': "../../test_data/journal_data",
        'RAW_DATA_PATH': "../../test_data/raw_data",
        'RESULT_FILE_PATH': "../../output/"
    }
    if id in paths:
        return paths.get(id)
    else:
        print(f"FEHLER: 'Für die Projekt-ID '{id}' konnten keine Pfade gefunden werden. Bitte ergänze die Pfadangeben in der Funktion 'get_paths_for' in der config.py.")
        exit('Programmabbruch.')


TABLE_FORMAT_HEAD = {'bold': True,'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}
TABLE_FORMAT_HEAD_RIGHT = {'bold': True,'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}
TABLE_FORMAT_HEAD_LEFT = {'bold': True,'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'}

COLUMN_WIDTH_VALUES_OF_SURCHARGES_RETURN = [(0, 0, 10), (1, 1, 30), (2, 2, 10)]
TABLE_HEAD_OF_SURCHARGES_RETURN = [
    ("Monat", TABLE_FORMAT_HEAD_RIGHT),
    ("Stellennummer", TABLE_FORMAT_HEAD_LEFT),
    ("Betrag", TABLE_FORMAT_HEAD_LEFT)
    ]

# each tuple contains the first_col, the last_col and the width of the column(s)
COLUMN_WIDTH_VALUES_OF_COSTS = [(0, 1, 10), (2, 2, 24), (3, 3, 12), (4, 4, 22), (5, 6, 18)]
TABLE_HEAD_OF_COSTS = [
    ("Monat", TABLE_FORMAT_HEAD_RIGHT),
    ("Stellennr.", TABLE_FORMAT_HEAD),
    ("Stellenanteil u. Entgeltgr.", TABLE_FORMAT_HEAD),
    ("Entgelt", TABLE_FORMAT_HEAD),
    ("AG-Anteil Sozialv.", TABLE_FORMAT_HEAD),
    ("AG-Anteil bAV", TABLE_FORMAT_HEAD),
    ("AG-Brutto", TABLE_FORMAT_HEAD),
    ]

COLUMN_WIDTH_VALUES_OF_SURCHARGES = [(0, 1, 10), (2, 2, 15), (2, 3, 10)]
TABLE_HEAD_OF_SURCHARGES = [
    ("Monat", TABLE_FORMAT_HEAD_RIGHT),
    ("Stellennr.", TABLE_FORMAT_HEAD),
    ("U1", TABLE_FORMAT_HEAD),
    ("U2", TABLE_FORMAT_HEAD),
    ("insoU", TABLE_FORMAT_HEAD)
    ]

COLUMN_WIDTH_VALUES_OF_RIDE_COSTS = [(0, 0, 10), (1, 1, 30), (2, 2, 10)]
TABLE_HEAD_OF_DEFAULT_SHEET = [
    ("Monat", TABLE_FORMAT_HEAD_RIGHT),
    ("Verwendungszweck", TABLE_FORMAT_HEAD_LEFT),
    ("Betrag", TABLE_FORMAT_HEAD_LEFT)
    ]

COLUMN_WIDTH_VALUES_OF_PHONE = [(0, 0, 10), (1, 1, 35), (2, 2, 10)]


# each tuple contains the first_col, the last_col and the width of the column(s)
COLUMN_WIDTH_VALUES_OF_PROJECTS = [(0, 0, 20), (1, 3, 10)]


DATE_FORMAT = {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}
TEXT_FORMAT = {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}  
CURRENCY_FORMAT = {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'right'}
CURRENCY_FORMAT_PROJECT = {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}

DATE_FORMAT_PROJECTS = {'bold': True, 'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'}
TEXT_FORMAT_PROJECTS = {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}
PROJECT_ID_FORMAT_PROJECTS = {'bold': True,'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'}


TABLE_FORMAT_FOOTER_SUM = {'bold': True,'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}

TABLE_FOOTER_OF_COSTS = [
    ("", TABLE_FORMAT_HEAD),
    ("", TABLE_FORMAT_HEAD),
    ("", TABLE_FORMAT_HEAD),
    ("", TABLE_FORMAT_HEAD),
    ("", TABLE_FORMAT_HEAD),
    ("Summe:", TABLE_FORMAT_FOOTER_SUM)    
    ]

TABLE_FOOTER_OF_SURCHARGES_SHEET = [
    ("", TABLE_FORMAT_HEAD),
    ("Summe:", TABLE_FORMAT_FOOTER_SUM)
    ]

TABLE_FOOTER_OF_RIDE_COST_SHEET = [
    ("", TABLE_FORMAT_HEAD),
    ("Summe:", TABLE_FORMAT_FOOTER_SUM)
    ]

TABLE_FOOTER_OF_PHONE_SHEET = [
    ("", TABLE_FORMAT_HEAD),
    ("Summe:", TABLE_FORMAT_FOOTER_SUM)
    ]

TABLE_FOOTER_OF_ACCOUNTING_SHEET = [
    ("", TABLE_FORMAT_HEAD),
    ("Summe:", TABLE_FORMAT_FOOTER_SUM)
    ]

TABLE_FOOTER_OF_CLEANING_COAST_SHEET = [
    ("", TABLE_FORMAT_HEAD),
    ("Summe:", TABLE_FORMAT_FOOTER_SUM)
    ]

SHEETS_KEYS = {
    'COSTS_SHEET': ('Kosten MA_innen', COLUMN_WIDTH_VALUES_OF_PROJECTS, 'portrait'),
    'SURCHARGES_RETURN_SHEET': ('0.2.1 Einnahmen aus U 1', COLUMN_WIDTH_VALUES_OF_SURCHARGES_RETURN, 'portrait'),
    'COSTS_SHEET_PROJECT': ('1.1 Personalkosten', COLUMN_WIDTH_VALUES_OF_COSTS, 'landscape'),
    'SURCHARGES_SHEET': ('Umlagen', COLUMN_WIDTH_VALUES_OF_SURCHARGES, 'portrait'),
    'RIDE_COST_SHEET': ('3.5 Fahrtkosten', COLUMN_WIDTH_VALUES_OF_RIDE_COSTS, 'portrait'),
    'ACCOUNTING_SHEET': ('3.6 interne Buchhaltung', COLUMN_WIDTH_VALUES_OF_RIDE_COSTS, 'portrait'),
    'CLEANING_COAST_SHEET': ('3.7 Reinigung', COLUMN_WIDTH_VALUES_OF_RIDE_COSTS, 'portrait'),
    'PHONE_SHEET': ('3.11 Telefon Internet', COLUMN_WIDTH_VALUES_OF_PHONE, 'portrait')
}

def get_sheetnames_of(project_id):
    sheet_names = {}
    sheet_names['0002'] = [
        'SURCHARGES_RETURN_SHEET',
        'COSTS_SHEET_PROJECT',
        'SURCHARGES_SHEET',
        'RIDE_COST_SHEET',
        'ACCOUNTING_SHEET',
        'CLEANING_COAST_SHEET',
        'PHONE_SHEET'
    ]
    sheet_names['0006'] = [
        'SURCHARGES_RETURN_SHEET',
        'COSTS_SHEET_PROJECT',
        'SURCHARGES_SHEET',
        'RIDE_COST_SHEET',
        'ACCOUNTING_SHEET',
        'CLEANING_COAST_SHEET',
        'PHONE_SHEET'
    ]
    sheet_names['0026'] = [
        'SURCHARGES_RETURN_SHEET',
        'COSTS_SHEET_PROJECT',
        'SURCHARGES_SHEET',
        'RIDE_COST_SHEET',
        'ACCOUNTING_SHEET',
        'CLEANING_COAST_SHEET',
        'PHONE_SHEET'
    ]
    sheet_names['0054'] = [
        'SURCHARGES_RETURN_SHEET',
        'COSTS_SHEET_PROJECT',
        'SURCHARGES_SHEET',
        'RIDE_COST_SHEET',
        'ACCOUNTING_SHEET',
        'CLEANING_COAST_SHEET',
        'PHONE_SHEET'
    ]
    if project_id in sheet_names:
        return sheet_names.get(project_id)
    else:
        print(f"FEHLER: 'Für die Projekt-ID '{project_id}' konnten keine sheet-names gefunden werden. Bitte ergänze die Pfadangeben in der Funktion 'get_sheetnames_of' in der config.py.")
        exit('Programmabbruch.')

def get_personal_of(project_id):
    personal_ids = {}
    personal_ids['0002'] = [
        '1017',
        '1022',
        '1152'
    ]
    personal_ids['0006'] = [
        '1001',
        '1004',
        '1028',
        '1035'
    ]
    personal_ids['0026'] = [
        '1004',
        '1007',
        '1015',
        '1017',
        '1028',
        '1032',
        '1035',
        '1139',
        '1145',
        '1154'
    ]
    personal_ids['0054'] = [
        '1004',
        '1005',
        '1017',
        '1028',
        '1035',
        '1139'        
    ]
    if project_id in personal_ids:
        return personal_ids.get(project_id)
    else:
        print(f"FEHLER: 'Für die Projekt-ID '{project_id}' konnten keine Personal-IDs gefunden werden. Bitte ergänze die Pfadangeben in der Funktion 'get_personal_of' in der config.py.")
        exit('Programmabbruch.')

# TODO hier oder irgendwo anders: sicherstellen, dass die Stunden für Paul und Birthe (und optional auch für Janek) aus 9998 geholt werden, auch wenn es bspw. um 0026 geht
# eine Idee wäre, bei jedem Projekt auch 9998 mit einzulesen bzw. nur, wenn Paul oder Birthe in den Personal-IDs sind
def get_split_factor_for(project_id):
    factor = {}
    factor['0006'] = '0.74%'
    factor['0026'] = '32.34%'
    return factor.get(project_id)


# TODO hat Wetell wirklich keine Vertragsnummer bzw. was ist die Vertragsnummer von Aurora
def get_contract_num_of(id):
    contract_num = {
        '1001': '',
        '1005': '',
        '1007': '(Vertragsnr. 71351348)',
        '1015': '(Vertragsnr. 64665292)',
        '1017': '(Vertragsnr. 75639431)',
        '1032': '(Vertragsnr. 86117152)',
        '1139': '',
        '1145': '(Vertragsnr. 71351348)',
        '1154': '(Vertragsnr. 86117152)'
    }
    return contract_num.get(id)

ID_OF_ACCOUNTING_PERSON = "1035"
ID_OF_CLEANING_PERSON = "1028"

