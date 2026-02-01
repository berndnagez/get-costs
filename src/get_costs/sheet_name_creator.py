def get_sheet_name_from(journal_name):
    parts = journal_name.split("_")
    year, month = parts[0], parts[1]
    sheet_name = f'{year}_{month}'
    return sheet_name
