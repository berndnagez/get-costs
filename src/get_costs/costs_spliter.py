def create_formulas(keys_and_value_list, divisor, splitted_values_dict):
    for key, value in keys_and_value_list:
        if value != 'nan' and value != '0.0':
            if "bAV" in key or "Gehalt" in key or "Sozialv" in key or "Umlagen" in key:
                if value == None:
                    splitted_values_dict[key] = 0.00
                    print(f'Der Wert für "{key}" wurde auf 0,00 Euro gesetzt.')
                else:
                    splitted_values_dict[key] = f'=ROUND(-{value}{divisor}, 2)'
            else:    
                splitted_values_dict[key] = f'=ROUND({value}{divisor}, 2)'
    return splitted_values_dict


# TODO: alle Spaltennamen, die von S&P kommen in der config als Dicts machen, so dass der key ein Variablenname ist und das value der eigentliche Spaltenname
# dann hier alle Spaltennamen durch die Variablen ersetzen, hätte den Vorteil, dass nur in der config was ändern muss, wenn S&P mal ander Spaltennamen haben
# und nicht gesamt Programmcode umschreiben muss
def get_pay(project):
    if project.get('St.Brutto - Steuerbrutto') == '0.0':
        return project.get('BezPausch - Pauschal versteuerte Bezüge')
    else:
        return project.get('St.Brutto - Steuerbrutto')


def get_social_insurance(project):
    insurance = float(project.get('KV-AG-Beitrag')) + float(project.get('RV-AG-Beitrag')) + float(project.get('AV-AG-Beitrag')) + float(project.get('PV-AG-Beitrag'))
    return str(insurance)


def get_umlagen(project):
    umlagen = float(project.get('U1 - Umlage 1')) + float(project.get('U2 - Umlage 2')) + float(project.get('InsoU - Insolvenzgeldumlage'))
    return str(umlagen)


def replace_semicolon(str):
    return str.replace(",", ".")

def get_divisor(project):
    divisor = replace_semicolon(project.get('Wochenstd'))
    factor = replace_semicolon(project.get('project_hours'))
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
        if projects:
            first_name = project.get('Name').split(" ")[0]
            keys_and_value_list = get_keys_and_value_list_of_projects(first_name, project)
        else:
            splitted_values_dict['ID'] = project.get('ID')
            keys_and_value_list = get_keys_and_value_list_of_project(project)
        create_formulas(keys_and_value_list, divisor, splitted_values_dict)

        splitted_values_list.append(splitted_values_dict)
    return splitted_values_list



def show_debug_infos():
    # project_list = [
    #     {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '24', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': '237.23'},
    #     {'project_id': '0054_comBüse', 'project_hours': '4.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '24', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': '237.23'},
    #     {'project_id': '0005_Präv', 'project_hours': '7.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
    #     {'project_id': '0009_Talk about ', 'project_hours': '13.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'},
    #     {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}
    # ]
    project_list = [{'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '24', 'St.Brutto - Steuerbrutto': '2297.29', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '55.13', 'U2 - Umlage 2': '8.96', 'InsoU - Insolvenzgeldumlage': '1.38', 'KV-AG-Beitrag': '187.23', 'RV-AG-Beitrag': '213.65', 'AV-AG-Beitrag': '29.86', 'PV-AG-Beitrag': '39.05', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': '237.23'}, {'project_id': '0054_comBüse', 'project_hours': '4.0', 'ID': '1004', 'Name': 'Björn Nagel', 'Wochenstd': '24', 'St.Brutto - Steuerbrutto': '2297.29', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '55.13', 'U2 - Umlage 2': '8.96', 'InsoU - Insolvenzgeldumlage': '1.38', 'KV-AG-Beitrag': '187.23', 'RV-AG-Beitrag': '213.65', 'AV-AG-Beitrag': '29.86', 'PV-AG-Beitrag': '39.05', 'bAV AG-Anteil': '75.0', 'HVV': 'nan', '1&1': 'nan', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': '237.23'}, {'project_id': '0005_Präv', 'project_hours': '7.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21', 'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}, {'project_id': '0009_Talk about ', 'project_hours': '13.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21', 'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}, {'project_id': '0026_comM', 'project_hours': '20.0', 'ID': '1032', 'Name': 'Alan Roberts', 'Wochenstd': '40', 'St.Brutto - Steuerbrutto': '3675.67', 'BezPausch - Pauschal versteuerte Bezüge': '0', 'U1 - Umlage 1': '124.97', 'U2 - Umlage 2': '15.81', 'InsoU - Insolvenzgeldumlage': '2.21', 'KV-AG-Beitrag': '297.36', 'RV-AG-Beitrag': '341.84', 'AV-AG-Beitrag': '47.78', 'PV-AG-Beitrag': '62.49', 'bAV AG-Anteil': '150.0', 'HVV': '-46.55', '1&1': '-7.99', 'Wetell': 'nan', 'Edenred': '-50.0', 'Urban Sports': 'nan', 'AU-Erstattung': 'nan'}]
    print(split(project_list, projects=False))

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()

