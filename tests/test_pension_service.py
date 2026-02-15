from src.get_company_pension_scheme.pension_service import PensionService


def test_get_pension_as_dict():
    file_path = "tests/test_data/26_01_21 BAV Januar 2026.xlsx"
    service = PensionService()
    pension_dict = service.get_pension_as_dict(file_path)

    assert len(pension_dict) == 34

    second_pension = pension_dict[1]
    assert second_pension["staff_id"] == 1004
    assert second_pension["name"] == "Nagel, Björn"
    assert second_pension["month"] == "2026/01"
    assert second_pension["pension_amount"] == 112.50

    thirty_third_pension = pension_dict[32]
    assert thirty_third_pension["staff_id"] == 1165
    assert thirty_third_pension["name"] == "Klein, Ida"
    assert thirty_third_pension["month"] == "2026/01"
    assert thirty_third_pension["pension_amount"] == 0.00
