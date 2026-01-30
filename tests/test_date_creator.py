from src.get_costs import date_creator


def test_validate():
    valid_filename = "24_04_23 Lohnjournal April 2024.xlsx"
    invalid_filename = "Lohnjournal April 2024.xlsx"

    # This should not raise an error
    date_creator.validate(valid_filename)

    try:
        date_creator.validate(invalid_filename)
    except SystemExit as e:
        assert str(e) == 'Programmabbruch.'
    else:
        assert False, "Expected SystemExit for invalid filename"


def test_split_year_month():
    filename = "24_04_23 Lohnjournal April 2024.xlsx"
    year, month = date_creator.split_year_month(filename)
    assert year == "24"
    assert month == "04"


def test_get_sheet_name():
    filename = "24_04_23 Lohnjournal April 2024.xlsx"
    sheet_name = date_creator.get_sheet_name(filename)
    assert sheet_name == "24_04"


def test_get_date_from():
    filename = "24_04_23 Lohnjournal April 2024.xlsx"
    date_object = date_creator.get_date_from(filename)
    assert date_object.year == 2024
    assert date_object.month == 4
    assert date_object.day == 1


def test_get_year():
    filename = "24_04_23 Lohnjournal April 2024.xlsx"
    year = date_creator.get_year(filename)
    assert year == "24"


def test_get_date_object():
    sheet_name = "24_04"
    date_object = date_creator.get_date_object(sheet_name)
    assert date_object.year == 2024
    assert date_object.month == 4
    assert date_object.day == 1
