import config

def create_formulas_for_projects(keys_and_value_list, divisor, splitted_values_dict):
    for key, value in keys_and_value_list:
        if value != 'nan' and value != '0.0':
            if "bAV" in key or "Gehalt" in key or "Sozialv" in key or "Umlagen" in key:
                if value == None:
                    splitted_values_dict[key] = 0.0
                    print(f'Der Wert für "{key}" wurde auf 0,00 Euro gesetzt.')
                else:
                    # hier werden die S&P-Daten für Paul mit einem negativen Vorzeichen versehen
                    splitted_values_dict[key] = f'=ROUND(-{value}{divisor}, 2)'
            else:    
                splitted_values_dict[key] = f'=ROUND({value}{divisor}, 2)'
    return splitted_values_dict


def create_formulas_for_project(keys_and_value_list, divisor, splitted_values_dict):
    for key, value in keys_and_value_list:
        if value != 'nan' and value != '0.0':
            if "bAV" in key or "Gehalt" in key or "Sozialv" in key or "U1" in key or "U2" in key or "InsoU" in key:
                if value == None:
                    splitted_values_dict[key] = 0.0
                    print(f'Der Wert für "{key}" wurde auf 0,00 Euro gesetzt.')
                else:
                    splitted_values_dict[key] = f'=ROUND({value}{divisor}, 2)'
            else:
                # hier kehre ich das Vorzeichen von Pauls negativen Zahlen um
                if value == None:
                    splitted_values_dict[key] = 0.0
                    #print(f'Der Wert für "{key}" bei value "{value}" wurde auf 0,00 Euro gesetzt.')
                else:
                    if float(value) < 0:
                        value = float(value)*-1  
                    splitted_values_dict[key] = f'=ROUND({value}{divisor}, 2)'
    return splitted_values_dict


def create_formulas_for_accounting_person(project_id, keys_and_value_list, divisor, splitted_values_dict):
    sum = float()
    factor = config.get_split_factor_for(project_id)
    for key, value in keys_and_value_list:
        if value != 'nan' and value != '0.0':
            if "bAV" in key or "Gehalt" in key or "Sozialv" in key or "U1" in key or "U2" in key or "InsoU" in key:
                if value == None:
                    splitted_values_dict[key] = 0.0
                    print(f'Der Wert für "{key}" wurde auf 0,00 Euro gesetzt.')
                else:
                    sum += float(value)
            else:
                # hier kehre ich das Vorzeichen von Pauls negativen Zahlen um
                if value == None:
                    splitted_values_dict[key] = 0.0
                    #print(f'Der Wert für "{key}" wurde auf 0,00 Euro gesetzt.')
                else:
                    if float(value) < 0:
                        if "HVV" in key:
                            value = float(value)*-1
                            sum += float(value)
    splitted_values_dict['Gehalt'] = f'=ROUND({sum}{divisor}, 2)*{factor}'
    return splitted_values_dict


def create_formulas_for_cleaning_person(project_id, keys_and_value_list, splitted_values_dict):
    sum = float()
    factor = config.get_split_factor_for(project_id)
    for key, value in keys_and_value_list:
        if value != 'nan' and value != '0.0':
            if "bAV" in key or "Gehalt" in key or "Sozialv" in key or "U1" in key or "U2" in key or "InsoU" in key:
                if value == None:
                    splitted_values_dict[key] = 0.0
                    print(f'Der Wert für "{key}" wurde auf 0,00 Euro gesetzt.')
                else:
                    sum += float(value)
    splitted_values_dict['Gehalt'] = f'={sum}*{factor}'
    return splitted_values_dict

# TODO: alle Spaltennamen, die von S&P kommen in der config als Dicts machen, so dass der key ein Variablenname ist und das value der eigentliche Spaltenname
# dann hier alle Spaltennamen durch die Variablen ersetzen, hätte den Vorteil, dass nur in der config was ändern muss, wenn S&P mal ander Spaltennamen haben
# und nicht gesamt Programmcode umschreiben muss
def get_pay(project):
    if project.get('St.Brutto - Steuerbrutto') == '0.0':
        return project.get('BezPausch - Pauschal versteuerte Bezüge')
    return project.get('St.Brutto - Steuerbrutto')


def get_social_insurance(project):
    if not project.get('KV-AG-Beitrag') and not project.get('RV-AG-Beitrag') and not project.get('AV-AG-Beitrag') and not project.get('PV-AG-Beitrag'):
        return 0.0
    insurance = float(project.get('KV-AG-Beitrag')) + float(project.get('RV-AG-Beitrag')) + float(project.get('AV-AG-Beitrag')) + float(project.get('PV-AG-Beitrag'))
    return str(insurance)


def get_umlagen(project):
    if not project.get('U1 - Umlage 1') and not project.get('U2 - Umlage 2') and not project.get('InsoU - Insolvenzgeldumlage'):
        return 0.0
    umlagen = float(project.get('U1 - Umlage 1')) + float(project.get('U2 - Umlage 2')) + float(project.get('InsoU - Insolvenzgeldumlage'))
    return str(umlagen)


def replace_semicolon(str):
    return str.replace(",", ".")

def get_divisor(project):
    divisor = replace_semicolon(project.get('Wochenstd'))
    factor = replace_semicolon(project.get('project_hours'))
    divisor = "/" + divisor + "*" + factor
    return divisor


def get_divisor_accounting_person(project):
    divisor = replace_semicolon(project.get('Wochenstd'))
    factor = '10'
    divisor = "/" + divisor + "*" + factor
    return divisor


def get_keys_and_value_list_of_projects(first_name, project):
    keys_and_value_list = [  
            ('Gehalt ' + first_name, get_pay(project)),
            ('Sozialv. ' + first_name, get_social_insurance(project)),
            ('Umlagen ' + first_name, get_umlagen(project)),
            ('bAV ' + first_name, project.get('bAV AG-Anteil')),
            ('HVV ' + first_name, project.get('HVV')),
            ('1&1 ' + first_name, project.get('1&1')),
            ('Wetell ' + first_name, project.get('Wetell')),
            ('Edenred ' + first_name, project.get('Edenred')),
            ('Urban Sports ' + first_name, project.get('Urban Sports')),
            ('AU-Erstattung ' + first_name, project.get('AU-Erstattung'))
            ]
    return keys_and_value_list


def get_keys_and_value_list_of_project(project):
    keys_and_value_list = [
            ('Gehalt', get_pay(project)),
            ('Sozialv.', get_social_insurance(project)),
            ('U1', project.get('U1 - Umlage 1')),
            ('U2', project.get('U2 - Umlage 2')),
            ('InsoU', project.get('InsoU - Insolvenzgeldumlage')),
            ('bAV', project.get('bAV AG-Anteil')),
            ('HVV', project.get('HVV')),
            ('1&1', project.get('1&1')),
            ('Wetell', project.get('Wetell')),
            ('AU-Erstattung', project.get('AU-Erstattung'))
            ]
    return keys_and_value_list


def split(project_list, projects):
    splitted_values_list = []
    for project in project_list:
        splitted_values_dict = {}        
        divisor = get_divisor(project)
        
        splitted_values_dict['project_id'] = project.get('project_id')
        project_id = project.get('project_id').split("_")[0]
        if projects:
            first_name = project.get('Name').split(" ")[0]
            keys_and_value_list = get_keys_and_value_list_of_projects(first_name, project)
            create_formulas_for_projects(keys_and_value_list, divisor, splitted_values_dict)
        else:
            splitted_values_dict['staff_id'] = project.get('ID')
            splitted_values_dict['project_hours'] = project.get('project_hours')
            keys_and_value_list = get_keys_and_value_list_of_project(project)
            if project.get('ID') == config.ID_OF_ACCOUNTING_PERSON:
                create_formulas_for_accounting_person(project_id, keys_and_value_list, get_divisor_accounting_person(project), splitted_values_dict)
            elif project.get('ID') == config.ID_OF_CLEANING_PERSON:
                create_formulas_for_cleaning_person(project_id, keys_and_value_list, splitted_values_dict)
            else:
                create_formulas_for_project(keys_and_value_list, divisor, splitted_values_dict)
        

        splitted_values_list.append(splitted_values_dict)
    return splitted_values_list



def show_debug_infos():
    # TODO wer macht die project_list? da auch ID durch staff_id ersetzen = Konsitenz
    # 19.01.2026: der project_costs_calculator.py macht die project_list, bekommt die ID vom data_reader (data_dict['ID'] = str(id))
    project_list = [
        {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '24', 'St.Brutto - Steuerbrutto': '2297.29', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '55.13', 'U2 - Umlage 2': '8.96', 'InsoU - Insolvenzgeldumlage': '1.38', 'KV-AG-Beitrag': '187.23', 'RV-AG-Beitrag': '213.65', 'AV-AG-Beitrag': '29.86', 'PV-AG-Beitrag': '39.05', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': '237.23'},
        {'project_id': '0054_comBüse', 'project_hours': '4.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '24', 'St.Brutto - Steuerbrutto': '2297.29', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '55.13', 'U2 - Umlage 2': '8.96', 'InsoU - Insolvenzgeldumlage': '1.38', 'KV-AG-Beitrag': '187.23', 'RV-AG-Beitrag': '213.65', 'AV-AG-Beitrag': '29.86', 'PV-AG-Beitrag': '39.05', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': '237.23'},
        {'project_id': '0005_Präv', 'project_hours': '7.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21', 'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0009_Talk about ', 'project_hours': '13.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21', 'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21', 'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1028', 'Name': 'Birthe', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '0', 'BezPausch - Pauschal versteuerte Bezüge': '533', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21', 'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0026_comM', 'project_hours': '10.0', 'ID': '1035', 'Name': 'Paul Thiessen', 'Wochenstd': '20', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21', 'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
        {'project_id': '0002_amb. TG ', 'project_hours': '25.0', 'ID': '1156', 'Name': 'Nels Wieschebrook', 'Wochenstd': '25.0', 'St.Brutto - Steuerbrutto': None, 'BezPausch - Pauschal versteuerte Bezüge': None, 'U1 - Umlage 1': None, 'U2 - Umlage 2': None, 'InsoU - Insolvenzgeldumlage': None, 'KV-AG-Beitrag': None, 'RV-AG-Beitrag': None, 'AV-AG-Beitrag': None, 'PV-AG-Beitrag': None, 'bAV AG-Anteil': None, 'HVV': 'nan', '1&1': '-19.99', 'Wetell': 'nan', 'Edenred': 'nan', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}
        ]
    print(split(project_list, projects=False))

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()

