# COLUMN_NAMES_OF_INTEREST = {
#     'Entgelt': 'St.Brutto - Steuerbrutto',
#     'U1': 'U1 - Umlage 1',
#     'U2': 'U2 - Umlage 2',
#     'U3': 'InsoU - Insolvenzgeldumlage'
# }

# COMPONENTS_OF_SOCIAL_INSURANCE = [
#     'KV-AG-Beitrag',
#     'RV-AG-Beitrag',
#     'AV-AG-Beitrag',
#     'PV-AG-Beitrag'
#     ]

#TODO prüfen, ob das oben weg kann, wird vom journal_data_reader verwendet

INDEX = "Pers.Nr."

# soll perspektivisch weg, wenn journal_names_getter so umgeschrieben ist, dass er aus dem gewünschten Verzeichnis liest
PATH_TO_DATA_FOLDER = "./data"

## nächste Zeile ist zum lokalen testen
#JOURNAL_DATA_PATH = "./data"
JOURNAL_DATA_PATH = "../../1036 Siebert und Partner/- 06 Lohnabrechnung _ Journal"

#TODO bzw. Idee: für meinen Verwendungszweck die gleichen Verzeichnisse nehmen und die Zieldatei nur rauskopieren
# oder: wenn Paul die Dateien nicht mehr pflegt, auf eigene Verzeichnisstruktur umbauen
# oder: Weiche, dass ich beide Optionen habe, quasi jenachdem ob eine Projekt-ID gesetzt ist oder nicht
RAW_DATA_PATH = "./- 01 Rohdaten Zur Auswertung"

# each tuple contains the first_col, the last_col and the width of the column(s)
COLUMN_WIDTH_VALUES_OF_COSTS = [(0, 1, 10), (2, 2, 24), (3, 3, 12), (4, 4, 22), (5, 6, 18)]
TABLE_FORMAT_HEAD = {'bold': True,'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'center'}
TABLE_HEAD_OF_COSTS = [
    ("Monat", TABLE_FORMAT_HEAD),
    ("Stellennr.", TABLE_FORMAT_HEAD),
    ("Stellenanteil u. Entgeltgr.", TABLE_FORMAT_HEAD),
    ("Entgelt", TABLE_FORMAT_HEAD),
    ("AG-Anteil Sozialv.", TABLE_FORMAT_HEAD),
    ("AG-Anteil bAV", TABLE_FORMAT_HEAD),
    ("AG-Brutto", TABLE_FORMAT_HEAD),
    ]

COLUMN_WIDTH_VALUES_OF_SURCHARGES = [(0, 1, 10), (2, 2, 15), (2, 3, 10)]
TABLE_HEAD_OF_SURCHARGES = [
    ("Monat", TABLE_FORMAT_HEAD),
    ("Stellennr.", TABLE_FORMAT_HEAD),
    ("U1", TABLE_FORMAT_HEAD),
    ("U2", TABLE_FORMAT_HEAD),
    ("insoU", TABLE_FORMAT_HEAD)
    ]

# each tuple contains the first_col, the last_col and the width of the column(s)
COLUMN_WIDTH_VALUES_OF_PROJECTS = [(0, 0, 20), (1, 3, 10)]


DATE_FORMAT = {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}
TEXT_FORMAT = {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}  
CURRENCY_FORMAT = {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'right'}

DATE_FORMAT_PROJECTS = {'bold': True, 'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'}
TEXT_FORMAT_PROJECTS = {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}
PROJECT_ID_FORMAT_PROJECTS = {'bold': True,'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'}


TABLE_FORMAT_FOOTER_SUM = {'bold': True,'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'right'}

TABLE_FOOTER_OF_COSTS = [
    ("", TABLE_FORMAT_HEAD),
    ("", TABLE_FORMAT_HEAD),
    ("", TABLE_FORMAT_HEAD),
    ("", TABLE_FORMAT_HEAD),
    ("", TABLE_FORMAT_HEAD),
    ("Summe:", TABLE_FORMAT_FOOTER_SUM)    
    ]

TABLE_FOOTER_OF_SURCHARGES = [
    ("", TABLE_FORMAT_HEAD),
    ("Summe:", TABLE_FORMAT_FOOTER_SUM)
    ]

SHEETS_KEYS = {
    'COSTS_SHEET': ('Kosten MA_innen', COLUMN_WIDTH_VALUES_OF_PROJECTS, 'portrait'),
    'SURCHARGES_RETURN_SHEET': ('0.2.1 Einnahmen aus U 1', COLUMN_WIDTH_VALUES_OF_SURCHARGES, 'portrait'),
    'COSTS_SHEET_PROJECT': ('1.1 Personalkosten', COLUMN_WIDTH_VALUES_OF_COSTS, 'landscape'),
    'SURCHARGES_SHEET': ('Umlagen', COLUMN_WIDTH_VALUES_OF_SURCHARGES, 'portrait'),
    'RIDE_COST_SHEET': ('3.5 Fahrtkosten', COLUMN_WIDTH_VALUES_OF_SURCHARGES, 'portrait'),
    'ACCOUNTING_SHEET': ('3.6 interne Buchhaltung', COLUMN_WIDTH_VALUES_OF_SURCHARGES, 'portrait'),
    'CLEANING_COAST_SHEET': ('3.7 Reinigung', COLUMN_WIDTH_VALUES_OF_SURCHARGES, 'portrait'),
    'PHONE_SHEET': ('3.11 Telefon Internet', COLUMN_WIDTH_VALUES_OF_SURCHARGES, 'portrait')
}

def get_sheetnames_of(project_id):
    sheet_names = {}
    sheet_names['0026'] = [
        'SURCHARGES_RETURN_SHEET',
        'COSTS_SHEET_PROJECT',
        'SURCHARGES_SHEET',
        'RIDE_COST_SHEET',
        'ACCOUNTING_SHEET',
        'CLEANING_COAST_SHEET',
        'PHONE_SHEET'
    ]
    return sheet_names.get(project_id)
