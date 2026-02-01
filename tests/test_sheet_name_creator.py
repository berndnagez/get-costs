from src.get_costs import sheet_name_creator


def test_get_sheet_name_from():
    filename = "24_04_23 Lohnjournal April 2024.xlsx"
    sheet_name = sheet_name_creator.get_sheet_name_from(filename)
    assert sheet_name == "24_04"
