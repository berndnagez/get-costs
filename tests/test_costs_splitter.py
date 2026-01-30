from src.get_costs import costs_splitter


def test_get_divisor():
    project = {'Wochenstd': '24', 'project_hours': '20.0'}
    expected_divisor = '/24*20.0'
    returned_divisor = costs_splitter.get_divisor(project)
    assert expected_divisor == returned_divisor


def test_replace_comma():
    str_with_comma = "19,99"
    expected_str = "19.99"
    returned_str = costs_splitter.replace_comma(str_with_comma)
    assert expected_str == returned_str


def test_get_pay():
    project = {'St.Brutto - Steuerbrutto': '2297.29'}
    expected_pay = '2297.29'
    returned_pay = costs_splitter.get_pay(project)
    assert expected_pay == returned_pay

    project = {'St.Brutto - Steuerbrutto': '0.0',
               'BezPausch - Pauschal versteuerte Bezüge': '533'}
    expected_pay = '533'
    returned_pay = costs_splitter.get_pay(project)
    assert expected_pay == returned_pay


def test_get_social_insurance():
    project = {'KV-AG-Beitrag': '187.23', 'RV-AG-Beitrag': '213.65',
               'AV-AG-Beitrag': '29.86', 'PV-AG-Beitrag': '39.05'}
    expected_insurance = '469.79'
    returned_insurance = costs_splitter.get_social_insurance(project)
    assert expected_insurance == returned_insurance

    project = {'KV-AG-Beitrag': None, 'RV-AG-Beitrag': None,
               'AV-AG-Beitrag': None, 'PV-AG-Beitrag': None}
    expected_insurance = 0.0
    returned_insurance = costs_splitter.get_social_insurance(project)
    assert expected_insurance == returned_insurance


def test_get_surcharges():
    project = {'U1 - Umlage 1': '55.13', 'U2 - Umlage 2': '8.96',
               'InsoU - Insolvenzgeldumlage': '1.38'}
    expected_surcharges = '65.47'
    returned_surcharges = costs_splitter.get_surcharges(project)
    assert expected_surcharges == returned_surcharges

    project = {'U1 - Umlage 1': None, 'U2 - Umlage 2': None,
               'InsoU - Insolvenzgeldumlage': None}
    expected_surcharges = 0.0
    returned_surcharges = costs_splitter.get_surcharges(project)
    assert expected_surcharges == returned_surcharges


def test_get_keys_and_value_list_of_projects():
    project = {'St.Brutto - Steuerbrutto': '2297.29', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '55.13', 'U2 - Umlage 2': '8.96', 'InsoU - Insolvenzgeldumlage': '1.38', 'KV-AG-Beitrag': '187.23',
               'RV-AG-Beitrag': '213.65', 'AV-AG-Beitrag': '29.86', 'PV-AG-Beitrag': '39.05', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0',  'Urban Sports': 'nan', 'AU-Erstattung': '237.23'}
    expected_keys_and_value_list = [
        ('Gehalt Björn', '2297.29'),
        ('Sozialv. Björn', '469.79'),
        ('Umlagen Björn', '65.47'),
        ('bAV Björn', '75.0'),
        ('HVV Björn', 'nan'),
        ('1&1 Björn', 'nan'),
        ('Wetell Björn', 'nan'),
        ('Edenred Björn', '-50.0'),
        ('Urban Sports Björn', 'nan'),
        ('AU-Erstattung Björn', '237.23')
    ]
    returned_keys_and_value_list = costs_splitter.get_keys_and_value_list_of_projects(
        "Björn", project)
    assert expected_keys_and_value_list == returned_keys_and_value_list


def test_create_formulas_for_projects():
    keys_and_value_list = [
        ('Gehalt Björn', '2297.29'),
        ('Sozialv. Björn', '469.79'),
        ('Umlagen Björn', '65.47'),
        ('bAV Björn', '75.0'),
        ('HVV Björn', 'nan'),
        ('1&1 Björn', 'nan'),
        ('Wetell Björn', 'nan'),
        ('Edenred Björn', '-50.0'),
        ('Urban Sports Björn', 'nan'),
        ('AU-Erstattung Björn', '237.23')
    ]
    divisor = '/24*20.0'
    splitted_values_dict = {}
    splitted_values_dict['project_id'] = '0026_comM'
    expected_splitted_values_dict = {
        'project_id': '0026_comM',
        'Gehalt Björn': '=ROUND(-2297.29/24*20.0, 2)',
        'Sozialv. Björn': '=ROUND(-469.79/24*20.0, 2)',
        'Umlagen Björn': '=ROUND(-65.47/24*20.0, 2)',
        'bAV Björn': '=ROUND(-75.0/24*20.0, 2)',
        'Edenred Björn': '=ROUND(-50.0/24*20.0, 2)',
        'AU-Erstattung Björn': '=ROUND(237.23/24*20.0, 2)'
    }
    returned_splitted_values_dict = costs_splitter.create_formulas_for_projects(
        keys_and_value_list, divisor, splitted_values_dict)
    assert expected_splitted_values_dict == returned_splitted_values_dict


def test_get_keys_and_value_list_of_project():
    project = {'St.Brutto - Steuerbrutto': '2297.29', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '55.13', 'U2 - Umlage 2': '8.96', 'InsoU - Insolvenzgeldumlage': '1.38', 'KV-AG-Beitrag': '187.23',
               'RV-AG-Beitrag': '213.65', 'AV-AG-Beitrag': '29.86', 'PV-AG-Beitrag': '39.05', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0',  'Urban Sports': 'nan', 'AU-Erstattung': '237.23'}
    expected_keys_and_value_list = [
        ('Gehalt', '2297.29'),
        ('Sozialv.', '469.79'),
        ('U1', '55.13'),
        ('U2', '8.96'),
        ('InsoU', '1.38'),
        ('bAV', '75.0'),
        ('HVV', 'nan'),
        ('1&1', 'nan'),
        ('Wetell', 'nan'),
        ('AU-Erstattung', '237.23')
    ]
    returned_keys_and_value_list = costs_splitter.get_keys_and_value_list_of_project(
        project)
    assert expected_keys_and_value_list == returned_keys_and_value_list


def test_get_divisor_accounting_person():
    project = {'Wochenstd': '24'}
    expected_divisor = '/24*10'
    returned_divisor = costs_splitter.get_divisor_accounting_person(project)
    assert expected_divisor == returned_divisor


def test_create_formulas_for_accounting_person():
    project_id = '0026'
    keys_and_value_list = [
        ('Gehalt', '2297.29'),
        ('Sozialv.', '469.79'),
        ('U1', '55.13'),
        ('U2', '8.96'),
        ('InsoU', '1.38'),
        ('bAV', '75.0'),
        ('HVV', 'nan'),
        ('1&1', 'nan'),
        ('Wetell', 'nan'),
        ('AU-Erstattung', '237.23')
    ]
    divisor = '/24*10'
    splitted_values_dict = {}
    splitted_values_dict['project_id'] = '0026_comM'
    expected_splitted_values_dict = {
        'project_id': '0026_comM',
        'Gehalt': '=ROUND(2907.55/24*10, 2)*32.34%'
    }
    returned_splitted_values_dict = costs_splitter.create_formulas_for_accounting_person(
        project_id, keys_and_value_list, divisor, splitted_values_dict)
    assert expected_splitted_values_dict == returned_splitted_values_dict


def test_create_formulas_for_cleaning_person():
    project_id = '0026'
    keys_and_value_list = [
        ('Gehalt', '2297.29'),
        ('Sozialv.', '469.79'),
        ('U1', '55.13'),
        ('U2', '8.96'),
        ('InsoU', '1.38'),
        ('bAV', '75.0'),
        ('HVV', 'nan'),
        ('1&1', 'nan'),
        ('Wetell', 'nan'),
        ('AU-Erstattung', '237.23')
    ]
    splitted_values_dict = {}
    splitted_values_dict['project_id'] = '0026_comM'
    expected_splitted_values_dict = {
        'project_id': '0026_comM',
        'Gehalt': '=2907.55*32.34%'
    }
    returned_splitted_values_dict = costs_splitter.create_formulas_for_cleaning_person(
        project_id, keys_and_value_list, splitted_values_dict)
    assert expected_splitted_values_dict == returned_splitted_values_dict


def test_create_formulas_for_project():
    keys_and_value_list = [
        ('Gehalt', '2297.29'),
        ('Sozialv.', '469.79'),
        ('U1', '55.13'),
        ('U2', '8.96'),
        ('InsoU', '1.38'),
        ('bAV', '75.0'),
        ('HVV', 'nan'),
        ('1&1', 'nan'),
        ('Wetell', 'nan'),
        ('AU-Erstattung', '237.23')
    ]
    divisor = '/24*20.0'
    splitted_values_dict = {}
    splitted_values_dict['project_id'] = '0026_comM'
    expected_splitted_values_dict = {
        'project_id': '0026_comM',
        'Gehalt': '=ROUND(2297.29/24*20.0, 2)',
        'Sozialv.': '=ROUND(469.79/24*20.0, 2)',
        'U1': '=ROUND(55.13/24*20.0, 2)',
        'U2': '=ROUND(8.96/24*20.0, 2)',
        'InsoU': '=ROUND(1.38/24*20.0, 2)',
        'bAV': '=ROUND(75.0/24*20.0, 2)',
        'AU-Erstattung': '=ROUND(237.23/24*20.0, 2)'
    }
    returned_splitted_values_dict = costs_splitter.create_formulas_for_project(
        keys_and_value_list, divisor, splitted_values_dict)
    assert expected_splitted_values_dict == returned_splitted_values_dict


def test_split():
    projectlist = [
        {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '24', 'St.Brutto - Steuerbrutto': '2297.29', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '55.13', 'U2 - Umlage 2': '8.96', 'InsoU - Insolvenzgeldumlage': '1.38',
            'KV-AG-Beitrag': '187.23', 'RV-AG-Beitrag': '213.65', 'AV-AG-Beitrag': '29.86', 'PV-AG-Beitrag': '39.05', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': '237.23'},
        {'project_id': '0054_comBüse', 'project_hours': '4.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '24', 'St.Brutto - Steuerbrutto': '2297.29', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '55.13', 'U2 - Umlage 2': '8.96',
            'InsoU - Insolvenzgeldumlage': '1.38', 'KV-AG-Beitrag': '187.23', 'RV-AG-Beitrag': '213.65', 'AV-AG-Beitrag': '29.86', 'PV-AG-Beitrag': '39.05', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': '237.23'},
        {'project_id': '0005_Präv', 'project_hours': '7.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21',
            'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0009_Talk about ', 'project_hours': '13.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81',
            'InsoU - Insolvenzgeldumlage': '2.21', 'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21',
            'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1028', 'Name': 'Birthe', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '0.0', 'BezPausch - Pauschal versteuerte Bezüge': '533', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21',
            'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0026_comM', 'project_hours': '10.0', 'ID': '1035', 'Name': 'Paul Thiessen', 'Wochenstd': '20', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21',
            'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0002_amb. TG ', 'project_hours': '25.0', 'ID': '1156', 'Name': 'Nels Wieschebrook', 'Wochenstd': '25.0', 'St.Brutto - Steuerbrutto': None, 'BezPausch - Pauschal versteuerte Bezüge': None, 'U1 - Umlage 1': None, 'U2 - Umlage 2': None,
            'InsoU - Insolvenzgeldumlage': None, 'KV-AG-Beitrag': None, 'RV-AG-Beitrag': None, 'AV-AG-Beitrag': None, 'PV-AG-Beitrag': None, 'bAV AG-Anteil': None, 'HVV': 'nan', '1&1': '-19.99', 'Wetell': 'nan', 'Edenred': 'nan', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}
    ]
    expected_splitted_values_list = [
        {'project_id': '0026_comM', 'Gehalt Björn': '=ROUND(-2297.29/24*20.0, 2)', 'Sozialv. Björn': '=ROUND(-469.79/24*20.0, 2)', 'Umlagen Björn': '=ROUND(-65.47/24*20.0, 2)',
         'bAV Björn': '=ROUND(-75.0/24*20.0, 2)', 'Edenred Björn': '=ROUND(-50.0/24*20.0, 2)', 'AU-Erstattung Björn': '=ROUND(237.23/24*20.0, 2)'},
        {'project_id': '0054_comBüse', 'Gehalt Björn': '=ROUND(-2297.29/24*4.0, 2)', 'Sozialv. Björn': '=ROUND(-469.79/24*4.0, 2)', 'Umlagen Björn': '=ROUND(-65.47/24*4.0, 2)',
         'bAV Björn': '=ROUND(-75.0/24*4.0, 2)', 'Edenred Björn': '=ROUND(-50.0/24*4.0, 2)', 'AU-Erstattung Björn': '=ROUND(237.23/24*4.0, 2)'},
        {'project_id': '0005_Präv', 'Gehalt Alan': '=ROUND(-3675.67/40*7.0, 2)', 'Sozialv. Alan': '=ROUND(-749.47/40*7.0, 2)', 'Umlagen Alan': '=ROUND(-142.99/40*7.0, 2)',
         'bAV Alan': '=ROUND(-150.0/40*7.0, 2)', 'HVV Alan': '=ROUND(-46.55/40*7.0, 2)', '1&1 Alan': '=ROUND(-7.99/40*7.0, 2)', 'Edenred Alan': '=ROUND(-50.0/40*7.0, 2)'},
        {'project_id': '0009_Talk about ', 'Gehalt Alan': '=ROUND(-3675.67/40*13.0, 2)', 'Sozialv. Alan': '=ROUND(-749.47/40*13.0, 2)', 'Umlagen Alan': '=ROUND(-142.99/40*13.0, 2)',
         'bAV Alan': '=ROUND(-150.0/40*13.0, 2)', 'HVV Alan': '=ROUND(-46.55/40*13.0, 2)', '1&1 Alan': '=ROUND(-7.99/40*13.0, 2)', 'Edenred Alan': '=ROUND(-50.0/40*13.0, 2)'},
        {'project_id': '0026_comM', 'Gehalt Alan': '=ROUND(-3675.67/40*20.0, 2)', 'Sozialv. Alan': '=ROUND(-749.47/40*20.0, 2)', 'Umlagen Alan': '=ROUND(-142.99/40*20.0, 2)',
         'bAV Alan': '=ROUND(-150.0/40*20.0, 2)', 'HVV Alan': '=ROUND(-46.55/40*20.0, 2)', '1&1 Alan': '=ROUND(-7.99/40*20.0, 2)', 'Edenred Alan': '=ROUND(-50.0/40*20.0, 2)'},
        {'project_id': '0026_comM', 'Gehalt Birthe': '=ROUND(-533/40*20.0, 2)', 'Sozialv. Birthe': '=ROUND(-749.47/40*20.0, 2)', 'Umlagen Birthe': '=ROUND(-142.99/40*20.0, 2)',
         'bAV Birthe': '=ROUND(-150.0/40*20.0, 2)', 'HVV Birthe': '=ROUND(-46.55/40*20.0, 2)', '1&1 Birthe': '=ROUND(-7.99/40*20.0, 2)', 'Edenred Birthe': '=ROUND(-50.0/40*20.0, 2)'},
        {'project_id': '0026_comM', 'Gehalt Paul': '=ROUND(-3675.67/20*10.0, 2)', 'Sozialv. Paul': '=ROUND(-749.47/20*10.0, 2)', 'Umlagen Paul': '=ROUND(-142.99/20*10.0, 2)',
         'bAV Paul': '=ROUND(-150.0/20*10.0, 2)', 'HVV Paul': '=ROUND(-46.55/20*10.0, 2)', '1&1 Paul': '=ROUND(-7.99/20*10.0, 2)', 'Edenred Paul': '=ROUND(-50.0/20*10.0, 2)'},
        {'project_id': '0002_amb. TG ', 'Gehalt Nels': 0.0,
            'Sozialv. Nels': '=ROUND(-0.0/25.0*25.0, 2)', 'Umlagen Nels': '=ROUND(-0.0/25.0*25.0, 2)', 'bAV Nels': 0.0, '1&1 Nels': '=ROUND(-19.99/25.0*25.0, 2)'}
    ]
    returned_splitted_values_list = costs_splitter.split_costs(
        projectlist, projects=True)
    assert expected_splitted_values_list == returned_splitted_values_list

    projectlist = [
        {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '24', 'St.Brutto - Steuerbrutto': '2297.29', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '55.13', 'U2 - Umlage 2': '8.96', 'InsoU - Insolvenzgeldumlage': '1.38',
            'KV-AG-Beitrag': '187.23', 'RV-AG-Beitrag': '213.65', 'AV-AG-Beitrag': '29.86', 'PV-AG-Beitrag': '39.05', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': '237.23'},
        {'project_id': '0054_comBüse', 'project_hours': '4.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '24', 'St.Brutto - Steuerbrutto': '2297.29', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '55.13', 'U2 - Umlage 2': '8.96',
            'InsoU - Insolvenzgeldumlage': '1.38', 'KV-AG-Beitrag': '187.23', 'RV-AG-Beitrag': '213.65', 'AV-AG-Beitrag': '29.86', 'PV-AG-Beitrag': '39.05', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': '237.23'},
        {'project_id': '0005_Präv', 'project_hours': '7.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21',
            'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0009_Talk about ', 'project_hours': '13.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81',
            'InsoU - Insolvenzgeldumlage': '2.21', 'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21',
            'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1028', 'Name': 'Birthe', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '0.0', 'BezPausch - Pauschal versteuerte Bezüge': '533', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21',
            'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0026_comM', 'project_hours': '10.0', 'ID': '1035', 'Name': 'Paul Thiessen', 'Wochenstd': '20', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21',
            'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0002_amb. TG ', 'project_hours': '25.0', 'ID': '1156', 'Name': 'Nels Wieschebrook', 'Wochenstd': '25.0', 'St.Brutto - Steuerbrutto': None, 'BezPausch - Pauschal versteuerte Bezüge': None, 'U1 - Umlage 1': None, 'U2 - Umlage 2': None,
            'InsoU - Insolvenzgeldumlage': None, 'KV-AG-Beitrag': None, 'RV-AG-Beitrag': None, 'AV-AG-Beitrag': None, 'PV-AG-Beitrag': None, 'bAV AG-Anteil': None, 'HVV': 'nan', '1&1': '-19.99', 'Wetell': 'nan', 'Edenred': 'nan', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}
    ]
    expected_splitted_values_list = [
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
            'project_hours': '20.0', 'Gehalt': '=1575.46*32.34%'},
        {'project_id': '0026_comM', 'staff_id': '1035', 'project_hours': '10.0',
            'Gehalt': '=ROUND(4764.680000000001/20*10, 2)*32.34%'},
        {'project_id': '0002_amb. TG ', 'staff_id': '1156', 'project_hours': '25.0', 'Gehalt': 0.0,
            'Sozialv.': '=ROUND(0.0/25.0*25.0, 2)', 'U1': 0.0, 'U2': 0.0, 'InsoU': 0.0, 'bAV': 0.0, '1&1': '=ROUND(19.99/25.0*25.0, 2)'}
    ]
    returned_splitted_values_list = costs_splitter.split_costs(
        projectlist, projects=False)
    assert expected_splitted_values_list == returned_splitted_values_list
