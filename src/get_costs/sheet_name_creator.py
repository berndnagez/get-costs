def get_sheet_name_from(journal_name):
    parts = journal_name.split("_")
    sheet_name = f'{parts[0]}_{parts[1]}'
    return sheet_name
