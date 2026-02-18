import datetime
from src.get_costs.output import project_rows_creator


def test_create_project_sheets():
    expected_project_sheets = {
        'SURCHARGES_RETURN_SHEET': [],
        'COSTS_SHEET_PROJECT': [],
        'SURCHARGES_SHEET': [],
        'RIDE_COST_SHEET': [],
        'ACCOUNTING_SHEET': [],
        'CLEANING_COAST_SHEET': [],
        'PHONE_SHEET': []

    }
    returned_project_sheets = project_rows_creator.create_project_sheets([
        'SURCHARGES_RETURN_SHEET',
        'COSTS_SHEET_PROJECT',
        'SURCHARGES_SHEET',
        'RIDE_COST_SHEET',
        'ACCOUNTING_SHEET',
        'CLEANING_COAST_SHEET',
        'PHONE_SHEET'
    ])
    assert expected_project_sheets == returned_project_sheets


def test_append_row_to():
    expected_project_sheets = {
        'SURCHARGES_RETURN_SHEET': [('Hello', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('World', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
        'COSTS_SHEET_PROJECT': [('Hello', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('World', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
        'SURCHARGES_SHEET': [],
        'RIDE_COST_SHEET': [('HVV', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
        'ACCOUNTING_SHEET': [],
        'CLEANING_COAST_SHEET': [],
        'PHONE_SHEET': []

    }
    project_sheets = {
        'SURCHARGES_RETURN_SHEET': [('Hello', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('World', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
        'COSTS_SHEET_PROJECT': [('Hello', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
        'SURCHARGES_SHEET': [],
        'RIDE_COST_SHEET': [('HVV', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
        'ACCOUNTING_SHEET': [],
        'CLEANING_COAST_SHEET': [],
        'PHONE_SHEET': []

    }
    returned_project_sheets = project_rows_creator.append_row_to(
        'COSTS_SHEET_PROJECT', project_sheets, ('World', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}))

    assert expected_project_sheets == returned_project_sheets

    expected_project_sheets = {
        'SURCHARGES_RETURN_SHEET': [
            ('Hello', {'font_name': 'Arial',
             'font_size': '10', 'align': 'left'}),
            ('World', {'font_name': 'Arial',
             'font_size': '10', 'align': 'left'}),
            ('And Hello Björn', {'font_name': 'Arial',
             'font_size': '10', 'align': 'left'})
        ],
        'COSTS_SHEET_PROJECT': [('Hello', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('World', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
        'SURCHARGES_SHEET': [],
        'RIDE_COST_SHEET': [('HVV', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
        'ACCOUNTING_SHEET': [],
        'CLEANING_COAST_SHEET': [],
        'PHONE_SHEET': []

    }
    project_sheets = {
        'SURCHARGES_RETURN_SHEET': [('Hello', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('World', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
        'COSTS_SHEET_PROJECT': [('Hello', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('World', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
        'SURCHARGES_SHEET': [],
        'RIDE_COST_SHEET': [('HVV', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
        'ACCOUNTING_SHEET': [],
        'CLEANING_COAST_SHEET': [],
        'PHONE_SHEET': []

    }
    returned_project_sheets = project_rows_creator.append_row_to('SURCHARGES_RETURN_SHEET', project_sheets, ('And Hello Björn', {
                                                                 'font_name': 'Arial', 'font_size': '10', 'align': 'left'}))

    assert expected_project_sheets == returned_project_sheets


def test_distribute_values_to_sheets():
    project_id = "0026"

    splitted_values_list = [
        {'project_id': '0026_comM', 'staff_id': '1004', 'project_hours': '20.0', 'Gehalt': '=ROUND(2297.29/24*20.0, 2)', 'Sozialv.': '=ROUND(469.79/24*20.0, 2)', 'U1': '=ROUND(55.13/24*20.0, 2)',
         'U2': '=ROUND(8.96/24*20.0, 2)', 'InsoU': '=ROUND(1.38/24*20.0, 2)', 'bAV': '=ROUND(75.0/24*20.0, 2)', 'AU-Erstattung': '=ROUND(237.23/24*20.0, 2)'}
    ]

    project_sheets = {
        'SURCHARGES_RETURN_SHEET': [],
        'COSTS_SHEET_PROJECT': [],
        'SURCHARGES_SHEET': [],
        'RIDE_COST_SHEET': [],
        'ACCOUNTING_SHEET': [],
        'CLEANING_COAST_SHEET': [],
        'PHONE_SHEET': []

    }
    expected_project_sheets = {'SURCHARGES_RETURN_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Stellennummer', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'}), ('Betrag', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'})]], 'COSTS_SHEET_PROJECT': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Stellennr.', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('Stellenanteil u. Entgeltgr.', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('Entgelt', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('AG-Anteil Sozialv.', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('AG-Anteil bAV', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('AG-Brutto', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'})], [(datetime.date(2024, 1, 1), {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('1004', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('0,50 Haustarif', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(2297.29/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(469.79/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(75.0/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=SUM(D2:F2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})]], 'SURCHARGES_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Stellennr.', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('U1', {
        'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('U2', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('insoU', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'})], [(datetime.date(2024, 1, 1), {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('1004', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(55.13/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(8.96/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(1.38/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})]], 'RIDE_COST_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Verwendungszweck', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'}), ('Betrag', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'})], []], 'ACCOUNTING_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Verwendungszweck', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'}), ('Betrag', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'})]], 'CLEANING_COAST_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Verwendungszweck', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'}), ('Betrag', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'})]], 'PHONE_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Verwendungszweck', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'}), ('Betrag', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'})], []]}

    project_rows_creator.distribute_values_to_sheets(
        splitted_values_list, project_id, datetime.date(2024, 1, 1), project_sheets)

    assert expected_project_sheets == project_sheets

    splitted_values_list = [
        {'project_id': '0026_comM', 'staff_id': '1004', 'project_hours': '20.0', 'Gehalt': '=ROUND(2297.29/24*20.0, 2)', 'Sozialv.': '=ROUND(469.79/24*20.0, 2)', 'U1': '=ROUND(55.13/24*20.0, 2)',
         'U2': '=ROUND(8.96/24*20.0, 2)', 'InsoU': '=ROUND(1.38/24*20.0, 2)', 'bAV': '=ROUND(75.0/24*20.0, 2)', 'AU-Erstattung': '=ROUND(237.23/24*20.0, 2)'},
        {'project_id': '0054_comBüse', 'staff_id': '1004', 'project_hours': '4.0', 'Gehalt': '=ROUND(2297.29/24*4.0, 2)', 'Sozialv.': '=ROUND(469.79/24*4.0, 2)', 'U1': '=ROUND(55.13/24*4.0, 2)',
         'U2': '=ROUND(8.96/24*4.0, 2)', 'InsoU': '=ROUND(1.38/24*4.0, 2)', 'bAV': '=ROUND(75.0/24*4.0, 2)', 'AU-Erstattung': '=ROUND(237.23/24*4.0, 2)'},
        {'project_id': '0005_Präv', 'staff_id': '1032', 'project_hours': '7.0', 'Gehalt': '=ROUND(3675.67/40*7.0, 2)', 'Sozialv.': '=ROUND(749.47/40*7.0, 2)', 'U1': '=ROUND(124.97/40*7.0, 2)',
         'U2': '=ROUND(15.81/40*7.0, 2)', 'InsoU': '=ROUND(2.21/40*7.0, 2)', 'bAV': '=ROUND(150.0/40*7.0, 2)', 'HVV': '=ROUND(46.55/40*7.0, 2)', '1&1': '=ROUND(7.99/40*7.0, 2)'},
        {'project_id': '0009_Talk about ', 'staff_id': '1032', 'project_hours': '13.0', 'Gehalt': '=ROUND(3675.67/40*13.0, 2)', 'Sozialv.': '=ROUND(749.47/40*13.0, 2)', 'U1': '=ROUND(124.97/40*13.0, 2)',
         'U2': '=ROUND(15.81/40*13.0, 2)', 'InsoU': '=ROUND(2.21/40*13.0, 2)', 'bAV': '=ROUND(150.0/40*13.0, 2)', 'HVV': '=ROUND(46.55/40*13.0, 2)', '1&1': '=ROUND(7.99/40*13.0, 2)'},
        {'project_id': '0026_comM', 'staff_id': '1032', 'project_hours': '20.0', 'Gehalt': '=ROUND(3675.67/40*20.0, 2)', 'Sozialv.': '=ROUND(749.47/40*20.0, 2)', 'U1': '=ROUND(124.97/40*20.0, 2)',
         'U2': '=ROUND(15.81/40*20.0, 2)', 'InsoU': '=ROUND(2.21/40*20.0, 2)', 'bAV': '=ROUND(150.0/40*20.0, 2)', 'HVV': '=ROUND(46.55/40*20.0, 2)', '1&1': '=ROUND(7.99/40*20.0, 2)'},
        {'project_id': '0026_comM', 'staff_id': '1028',
            'project_hours': '20.0', 'Gehalt': '=899.47*32.34%'},
        {'project_id': '0026_comM', 'staff_id': '1035', 'project_hours': '10.0',
            'Gehalt': '=ROUND(4621.6900000000005/20*10, 2)*32.34%'}
    ]

    project_sheets = {
        'SURCHARGES_RETURN_SHEET': [],
        'COSTS_SHEET_PROJECT': [],
        'SURCHARGES_SHEET': [],
        'RIDE_COST_SHEET': [],
        'ACCOUNTING_SHEET': [],
        'CLEANING_COAST_SHEET': [],
        'PHONE_SHEET': []

    }
    expected_project_sheets = {'SURCHARGES_RETURN_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Stellennummer', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'}), ('Betrag', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'})]], 'COSTS_SHEET_PROJECT': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Stellennr.', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('Stellenanteil u. Entgeltgr.', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('Entgelt', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('AG-Anteil Sozialv.', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('AG-Anteil bAV', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('AG-Brutto', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'})], [(datetime.date(2024, 1, 1), {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('1004', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('0,50 Haustarif', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(2297.29/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(469.79/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(75.0/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=SUM(D2:F2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})], [(datetime.date(2024, 1, 1), {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('1032', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('0,50 Haustarif', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(3675.67/40*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(749.47/40*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(150.0/40*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=SUM(D3:F3)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})]], 'SURCHARGES_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Stellennr.', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('U1', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('U2', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('insoU', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'})], [(datetime.date(2024, 1, 1), {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('1004', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(55.13/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'font_size': '10', 'align': 'center'}), ('=ROUND(8.96/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(1.38/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})], [(datetime.date(2024, 1, 1), {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('1032', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(124.97/40*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(15.81/40*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(2.21/40*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})]], 'RIDE_COST_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Verwendungszweck', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'}), ('Betrag', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'})], [], [(datetime.date(2024, 1, 1), {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('HVV Stellennr. 1032', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('=ROUND(46.55/40*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})]], 'ACCOUNTING_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Verwendungszweck', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'}), ('Betrag', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'})], [(datetime.date(2024, 1, 1), {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('interne Buchhaltung', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('=ROUND(4621.6900000000005/20*10, 2)*32.34%', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})]], 'CLEANING_COAST_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Verwendungszweck', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'}), ('Betrag', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'})], [(datetime.date(2024, 1, 1), {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('Reinigung', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('=899.47*32.34%', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})]], 'PHONE_SHEET': [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Verwendungszweck', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'}), ('Betrag', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'left'})], [], [(datetime.date(2024, 1, 1), {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('1&1 Handy 1032 (Vertragsnr. 86117152)', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('=ROUND(7.99/40*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})]]}

    project_rows_creator.distribute_values_to_sheets(
        splitted_values_list, project_id, datetime.date(2024, 1, 1), project_sheets)

    assert expected_project_sheets == project_sheets


def test_get_last_row_num_of():
    costs_sheet = [[('Monat', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'right'}), ('Stellennr.', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('Stellenanteil u. Entgeltgr.', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('Entgelt', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('AG-Anteil Sozialv.', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('AG-Anteil bAV', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'}), ('AG-Brutto', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': '#dddddd', 'align': 'center'})], [('', {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('1004', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('0,50 Haustarif', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(2297.29/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(469.79/24*20.0, 2)', {
        'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(75.0/24*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=SUM(D2:F2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})], [('', {'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10'}), ('1032', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('0,50 Haustarif', {'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(3675.67/40*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(749.47/40*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=ROUND(150.0/40*20.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'}), ('=SUM(D3:F3)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'center'})]]
    assert project_rows_creator.get_last_row_num_of(costs_sheet) == 3
