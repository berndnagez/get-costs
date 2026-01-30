from src.get_costs import projectlist_creater


def test_erase_unneeded_data():
    data = [
        {
            'ID': '1004',
            'Name': 'Björn Nagel',
            'Unneeded1': 'data1'
        },
        {
            'ID': '1156',
            'Name': 'Nels Wieschebrook',
            'Unneeded1': 'data2',
            'Unneeded2': 'data3'
        }
    ]
    excepted_data = [
        {
            'ID': '1004',
            'Name': 'Björn Nagel'
        },
        {
            'ID': '1156',
            'Name': 'Nels Wieschebrook'
        }
    ]
    cleaned_data = projectlist_creater.erase_unneeded_data(data)
    assert cleaned_data == excepted_data


def test_erase_unneeded_employee_data():
    data = [
        {
            'ID': '1004',
            'Name': 'Björn Nagel',
            'Kontrolle': 'check1'
        },
        {
            'ID': '1156',
            'Name': 'Nels Wieschebrook',
            'Kontrolle': 'check2'
        }
    ]
    excepted_data = [
        {
            'ID': '1004',
            'Name': 'Björn Nagel'
        },
        {
            'ID': '1156',
            'Name': 'Nels Wieschebrook'
        }
    ]
    cleaned_data = projectlist_creater.erase_unneeded_employee_data(data)
    assert cleaned_data == excepted_data


def test_add_values_of_interest():
    employee = {'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '26.0', '0001_HZE': 'nan', '0002_amb. TG ': 'nan', '0108_GruLeLe': 'nan', '0005_Präv': 'nan', '0006_JAT': '1.0', '0009_Talk about ': 'nan', '0010_PTJA': 'nan', '0022_Rap f. V. ': 'nan', '0026_comM': '20.0', '0054_comBüse': '4.0', '0053_EOK': 'nan', '0060_StoP': 'nan', '0061_MGs': 'nan', '0064_Denkplosiv': 'nan', '9998_Verwaltung': '1.0',
                'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'KV-AG-Beitrag': '224.82', 'RV-AG-Beitrag': '240.33', 'AV-AG-Beitrag': '33.59', 'PV-AG-Beitrag': '46.51', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49', 'InsoU - Insolvenzgeldumlage': '3.88', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan', 'bAV AG-Anteil': '75.0'}
    project_dict = {
        'project_id': '0006_JAT',
        'project_hours': '1.0'
    }
    updated_project_dict = projectlist_creater.add_values_of_interest(
        project_dict, employee)
    excepted_project_dict = {'project_id': '0006_JAT', 'project_hours': '1.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '26.0', 'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49',
                             'InsoU - Insolvenzgeldumlage': '3.88', 'KV-AG-Beitrag': '224.82', 'RV-AG-Beitrag': '240.33', 'AV-AG-Beitrag': '33.59', 'PV-AG-Beitrag': '46.51', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}
    assert updated_project_dict == excepted_project_dict


def test_extract_projects():
    employee_data = [
        {
            'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '26.0', '0001_HZE': 'nan', '0002_amb. TG ': 'nan', '0108_GruLeLe': 'nan', '0005_Präv': 'nan', '0006_JAT': '1.0', '0009_Talk about ': 'nan', '0010_PTJA': 'nan', '0022_Rap f. V. ': 'nan', '0026_comM': '20.0', '0054_comBüse': '4.0', '0053_EOK': 'nan', '0060_StoP': 'nan', '0061_MGs': 'nan', '0064_Denkplosiv': 'nan', '9998_Verwaltung': '1.0', 'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'KV-AG-Beitrag': '224.82', 'RV-AG-Beitrag': '240.33', 'AV-AG-Beitrag': '33.59', 'PV-AG-Beitrag': '46.51', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49',
            'InsoU - Insolvenzgeldumlage': '3.88', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan', 'bAV AG-Anteil': '75.0'
        },
        {
            'ID': '1156', 'Name': 'Nels Wieschebrook', 'Wochenstd': '25.0', '0001_HZE': 'nan', '0002_amb. TG ': '25.0', '0108_GruLeLe': 'nan', '0005_Präv': 'nan', '0006_JAT': 'nan', '0009_Talk about ': 'nan', '0010_PTJA': 'nan', '0022_Rap f. V. ': 'nan', '0026_comM': 'nan',
            '0054_comBüse': 'nan', '0053_EOK': 'nan', '0060_StoP': 'nan', '0061_MGs': 'nan', '0064_Denkplosiv': 'nan', '9998_Verwaltung': 'nan', 'HVV': 'nan', '1&1': '-19.99', 'Wetell': 'nan', 'Edenred': 'nan', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'
        }
    ]
    excepted_projectlist = [{'project_id': '0006_JAT', 'project_hours': '1.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '26.0', 'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49', 'InsoU - Insolvenzgeldumlage': '3.88', 'KV-AG-Beitrag': '224.82', 'RV-AG-Beitrag': '240.33', 'AV-AG-Beitrag': '33.59', 'PV-AG-Beitrag': '46.51', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}, {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '26.0', 'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49', 'InsoU - Insolvenzgeldumlage': '3.88', 'KV-AG-Beitrag': '224.82', 'RV-AG-Beitrag': '240.33', 'AV-AG-Beitrag': '33.59', 'PV-AG-Beitrag': '46.51', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}, {'project_id': '0054_comBüse', 'project_hours': '4.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '26.0', 'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'InsoU - Insolvenzgeldumlage': '3.88', 'KV-AG-Beitrag': '224.82', 'RV-AG-Beitrag': '240.33', 'AV-AG-Beitrag': '33.59', 'PV-AG-Beitrag': '46.51', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}, {'project_id': '9998_Verwaltung', 'project_hours': '1.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '26.0', 'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49', 'InsoU - Insolvenzgeldumlage': '3.88', 'KV-AG-Beitrag': '224.82', 'RV-AG-Beitrag': '240.33', 'AV-AG-Beitrag': '33.59', 'PV-AG-Beitrag': '46.51', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}, {'project_id': '0002_amb. TG ', 'project_hours': '25.0', 'ID': '1156', 'Name': 'Nels Wieschebrook', 'Wochenstd': '25.0', 'St.Brutto - Steuerbrutto': None, 'BezPausch - Pauschal versteuerte Bezüge': None, 'U1 - Umlage 1': None, 'U2 - Umlage 2': None, 'InsoU - Insolvenzgeldumlage': None, 'KV-AG-Beitrag': None, 'RV-AG-Beitrag': None, 'AV-AG-Beitrag': None, 'PV-AG-Beitrag': None, 'bAV AG-Anteil': None, 'HVV': 'nan', '1&1': '-19.99', 'Wetell': 'nan', 'Edenred': 'nan', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}]
    projectlist = projectlist_creater.extract_projects(employee_data)
    assert projectlist == excepted_projectlist


def test_create_projectlist():
    employee_data = [{'ID': '1004', 'Name': 'Björn T.', 'Wochenstd': '26.0', '0001_HZE': 'nan', '0002_amb. TG ': 'nan', '0108_GruLeLe': 'nan', '0005_Präv': 'nan', '0006_JAT': '1.0', '0009_Talk about ': 'nan', '0010_PTJA': 'nan', '0022_Rap f. V. ': 'nan', '0026_comM': '20.0', '0054_comBüse': '4.0', '0053_EOK': 'nan', '0060_StoP': 'nan', '0061_MGs': 'nan', '0064_Denkplosiv': 'nan', '9998_Verwaltung': '1.0', 'Kontrolle': '0'}, {
        'ID': '1156', 'Name': 'Nels', 'Wochenstd': '25.0', '0001_HZE': 'nan', '0002_amb. TG ': '25.0', '0108_GruLeLe': 'nan', '0005_Präv': 'nan', '0006_JAT': 'nan', '0009_Talk about ': 'nan', '0010_PTJA': 'nan', '0022_Rap f. V. ': 'nan', '0026_comM': 'nan', '0054_comBüse': 'nan', '0053_EOK': 'nan', '0060_StoP': 'nan', '0061_MGs': 'nan', '0064_Denkplosiv': 'nan', '9998_Verwaltung': 'nan', 'Kontrolle': '0'}]
    journal_data = [{'ID': '1004', 'Abrechnungsmonat': '2025/09', 'Name,Vorname (MA)': 'Nagel, Björn', 'BGRS - Beitragsgruppenschlüssel': '1111', 'AN-Typ - Arbeitnehmertyp': '1', 'St.Kl. - Steuerklasse': '1', 'Ki.Frb. - Kinderfreibetrag': '0.5', 'Konf.A/E - Konnfession Arbeitnehmer/Ehegatte': 'nan', 'SV-Tage (BN) - Sozialversicherungstage': '30', 'St.Tage - Steuertage': '30', 'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'LSt - Lohnsteuer': '215.25', 'LStPausch - Pauschale Lohnsteuer': '0.0', 'KiSt - Kirchensteuer': '0.0', 'KiStPausch - Pauschale Kirchensteuer': '0',
                     'KV-Brutto': '2584.15', 'KV-AN-Beitrag': '224.82', 'KV-AG-Beitrag': '224.82', 'RV-Brutto': '2584.15', 'RV-AN-Beitrag': '240.33', 'RV-AG-Beitrag': '240.33', 'AV-Brutto': '2584.15', 'AV-AN-Beitrag': '33.59', 'AV-AG-Beitrag': '33.59', 'PV-Brutto': '2584.15', 'PV-AN-Beitrag': '46.51', 'PV-AG-Beitrag': '46.51', 'Z-KZ - PV-Beitragszuschlag für Kinderlose': 'nan', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49', 'InsoU - Insolvenzgeldumlage': '3.88', 'Gesamtbrutto': '2584.15', 'Nettobezüge/-abzüge': '0.0', 'Auszahlungsbetrag': '1823.65'}, {'ID': '1156'}]
    provision = [{'ID': '1004', 'Abrechnungsmonat': '2025/09',
                  'Name,Vorname (MA)': 'Nagel, Björn', 'bAV AG-Anteil': '75.0'}, {'ID': '1156'}]
    additional_costs = [{'ID': '1004', 'Name': 'Björn Nagel', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan', 'Unnamed: 8': 'nan'},
                        {'ID': '1156', 'Name': 'Nels Wieschebrook', 'HVV': 'nan', '1&1': '-19.99', 'Wetell': 'nan', 'Edenred': 'nan', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan', 'Unnamed: 8': 'nan'}]
    excepted_projectlist = [{'project_id': '0006_JAT', 'project_hours': '1.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '26.0', 'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49', 'InsoU - Insolvenzgeldumlage': '3.88', 'KV-AG-Beitrag': '224.82', 'RV-AG-Beitrag': '240.33', 'AV-AG-Beitrag': '33.59', 'PV-AG-Beitrag': '46.51', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}, {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '26.0', 'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49', 'InsoU - Insolvenzgeldumlage': '3.88', 'KV-AG-Beitrag': '224.82', 'RV-AG-Beitrag': '240.33', 'AV-AG-Beitrag': '33.59', 'PV-AG-Beitrag': '46.51', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}, {'project_id': '0054_comBüse', 'project_hours': '4.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '26.0', 'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'InsoU - Insolvenzgeldumlage': '3.88', 'KV-AG-Beitrag': '224.82', 'RV-AG-Beitrag': '240.33', 'AV-AG-Beitrag': '33.59', 'PV-AG-Beitrag': '46.51', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}, {'project_id': '9998_Verwaltung', 'project_hours': '1.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '26.0', 'St.Brutto - Steuerbrutto': '2584.15', 'BezPausch - Pauschal versteuerte Bezüge': '0.0', 'U1 - Umlage 1': '59.44', 'U2 - Umlage 2': '7.49', 'InsoU - Insolvenzgeldumlage': '3.88', 'KV-AG-Beitrag': '224.82', 'RV-AG-Beitrag': '240.33', 'AV-AG-Beitrag': '33.59', 'PV-AG-Beitrag': '46.51', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}, {'project_id': '0002_amb. TG ', 'project_hours': '25.0', 'ID': '1156', 'Name': 'Nels Wieschebrook', 'Wochenstd': '25.0', 'St.Brutto - Steuerbrutto': None, 'BezPausch - Pauschal versteuerte Bezüge': None, 'U1 - Umlage 1': None, 'U2 - Umlage 2': None, 'InsoU - Insolvenzgeldumlage': None, 'KV-AG-Beitrag': None, 'RV-AG-Beitrag': None, 'AV-AG-Beitrag': None, 'PV-AG-Beitrag': None, 'bAV AG-Anteil': None, 'HVV': 'nan', '1&1': '-19.99', 'Wetell': 'nan', 'Edenred': 'nan', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}]
    projectlist = projectlist_creater.create_projectlist(
        employee_data, journal_data, provision, additional_costs)
    assert projectlist == excepted_projectlist
