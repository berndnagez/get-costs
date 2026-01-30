import xlsxwriter
from .config import SHEETS_KEYS


def write(name, border, all_rows):
    workbook = get_workbook(f'{name}.xlsx')
    for worksheetname, data in all_rows.items():
        sheet_config = SHEETS_KEYS.get(worksheetname)
        sheetname = sheet_config[0]
        column_width = sheet_config[1]
        orientation = sheet_config[2]
        worksheet = create_sheet(
            workbook, sheetname, column_width, orientation)
        for row_num, content in enumerate(data):
            write_row(workbook, worksheet, border, row_num, content)

    workbook.close()


def get_workbook(name):
    workbook = create_workbook(name)
    return workbook


def create_workbook(name):
    return xlsxwriter.Workbook(name)


def set_column_width(worksheet, first_col, last_col, width):
    worksheet.set_column(first_col, last_col, width)


def create_sheet(workbook, sheetname, column_width_list, orientation):
    worksheet = workbook.add_worksheet(sheetname)
    for width in column_width_list:
        (first_col, last_col, width) = width
        set_column_width(worksheet, first_col, last_col, width)
    if orientation == "landscape":
        worksheet.set_landscape()
    worksheet.set_paper(9)
    return worksheet


def write_row(workbook, worksheet, border, row_num, content):
    column_num = 0
    for data in content:
        (content, format) = data
        worksheet.write(row_num, column_num, content,
                        get_cell_format(workbook, border, format))
        column_num += 1


def get_cell_format(workbook, border, format):
    cell_format = workbook.add_format(format)
    if border:
        cell_format.set_border()
    return cell_format


if __name__ == "__main__":
    last_row_num = 0
    border = False
    all_rows_test_1 = {
        "COSTS_SHEET": [
            [('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
            [('0005_Präv', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'}), ('Januar', {'bold': True, 'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray',
                                                                                                                                      'align': 'left'}), ('', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'}), ('', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'})],
            [('Gehalt Alan', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]',
                                                                                                                                                                  'font_name': 'Arial', 'font_size': '10', 'align': 'right'}), ('=ROUND(-3675.67/40*7.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'right'})],
            [('Sozialv. Alan', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]',
                                                                                                                                                                    'font_name': 'Arial', 'font_size': '10', 'align': 'right'}), ('=ROUND(-749.47/40*7.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'right'})],
            [('Umlagen Alan', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]',
                                                                                                                                                                   'font_name': 'Arial', 'font_size': '10', 'align': 'right'}), ('=ROUND(-142.99/40*7.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'right'})]
        ]
    }
    all_rows_test_2 = {
        "COSTS_SHEET_PROJECT": [
            [('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
            [('0005_Präv', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'}), ('Januar', {'bold': True, 'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray',
                                                                                                                                      'align': 'left'}), ('', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'}), ('', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'})],
            [('Gehalt Alan', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]',
                                                                                                                                                                  'font_name': 'Arial', 'font_size': '10', 'align': 'right'}), ('=ROUND(-3675.67/40*7.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'right'})],
            [('Sozialv. Alan', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]',
                                                                                                                                                                    'font_name': 'Arial', 'font_size': '10', 'align': 'right'}), ('=ROUND(-749.47/40*7.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'right'})],
            [('Umlagen Alan', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]',
                                                                                                                                                                   'font_name': 'Arial', 'font_size': '10', 'align': 'right'}), ('=ROUND(-142.99/40*7.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'right'})]
        ],
        "SURCHARGES_SHEET": [
            [('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'})],
            [('0005_Präv', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'}), ('Januar', {'bold': True, 'num_format': 'mmm yyyy', 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray',
                                                                                                                                      'align': 'left'}), ('', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'}), ('', {'bold': True, 'font_name': 'Arial', 'font_size': '10', 'bg_color': 'gray', 'align': 'left'})],
            [('Gehalt Björn', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]',
                                                                                                                                                                   'font_name': 'Arial', 'font_size': '10', 'align': 'right'}), ('=ROUND(-3675.67/40*7.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'right'})],
            [('Sozialv. Björn', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]',
                                                                                                                                                                     'font_name': 'Arial', 'font_size': '10', 'align': 'right'}), ('=ROUND(-749.47/40*7.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'right'})],
            [('Umlagen Björn', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'font_name': 'Arial', 'font_size': '10', 'align': 'left'}), ('', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]',
                                                                                                                                                                    'font_name': 'Arial', 'font_size': '10', 'align': 'right'}), ('=ROUND(-142.99/40*7.0, 2)', {'num_format': '#,##0.00 [$€-407];[Red]-#,##0.00 [$€-407]', 'font_name': 'Arial', 'font_size': '10', 'align': 'right'})]
        ]
    }
    write("test_1", border, all_rows_test_1)
    write("test_2", border, all_rows_test_2)
