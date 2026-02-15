from src.get_company_pension_scheme.pension_reader import PensionReader
from src.get_company_pension_scheme.pension_models import Pension


def test_get_dataframe():
    pension_reader = PensionReader()
    dataframe_dict = pension_reader.get_dataframe(
        "./tests/test_data/26_01_21 BAV Januar 2026.xlsx")
    assert isinstance(dataframe_dict, dict)
    assert "bAV AG-Anteil" in dataframe_dict
    assert dataframe_dict["bAV AG-Anteil"][1004] == 112.5
    assert dataframe_dict["bAV AG-Anteil"][1165] == 0.00
    assert dataframe_dict["Name,Vorname (MA)"][1026] == "Ulbricht, Juliane"
    assert dataframe_dict["Abrechnungsmonat"][1022] == "2026/01"


def test_parse_pensions():
    pension_reader = PensionReader()
    dataframe_dict = {
        "bAV AG-Anteil": {1004: 112.5, 1026: 0.00},
        "Name,Vorname (MA)": {1004: "Björn Nagel", 1026: "Ulbricht, Juliane"},
        "Abrechnungsmonat": {1004: "2026/01", 1026: "2026/01"}
    }
    pensions = pension_reader.parse_pensions(dataframe_dict)
    assert len(pensions) == 2
    assert isinstance(pensions[0], Pension)
    assert pensions[0].staff_id == 1004
    assert pensions[0].name == "Björn Nagel"
    assert pensions[0].month == "2026/01"
    assert pensions[0].pension_amount == 112.5
    assert pensions[1].staff_id == 1026
    assert pensions[1].name == "Ulbricht, Juliane"
    assert pensions[1].month == "2026/01"
    assert pensions[1].pension_amount == 0.00
