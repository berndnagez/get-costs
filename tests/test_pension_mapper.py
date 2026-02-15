from src.get_company_pension_scheme.pension_models import Pension
from src.get_company_pension_scheme.pension_mapper import PensionMapper


def test_to_dict():
    pension = Pension(
        staff_id=1011,
        name="Özkan, Hasan",
        month="01/2025",
        pension_amount=150.00
    )

    result = PensionMapper.to_dict(pension)

    assert result["staff_id"] == 1011
    assert result["name"] == "Özkan, Hasan"
    assert result["month"] == "01/2025"
    assert result["pension_amount"] == 150.00


def test_list_to_dict():
    pensions = [
        Pension(
            staff_id=1011,
            name="Özkan, Hasan",
            month="01/2025",
            pension_amount=150.00
        ),
        Pension(
            staff_id=1026,
            name="Ulbricht, Juliane",
            month="01/2025",
            pension_amount=112.5
        )
    ]

    result = PensionMapper.list_to_dict(pensions)

    assert len(result) == 2
    assert result[0]["staff_id"] == 1011
    assert result[0]["name"] == "Özkan, Hasan"
    assert result[0]["month"] == "01/2025"
    assert result[0]["pension_amount"] == 150.00

    assert result[1]["staff_id"] == 1026
    assert result[1]["name"] == "Ulbricht, Juliane"
    assert result[1]["month"] == "01/2025"
    assert result[1]["pension_amount"] == 112.5
