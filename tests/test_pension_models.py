from src.get_company_pension_scheme.pension_models import Pension


def test_pension_model():
    pension = Pension(
        staff_id=1011,
        name="Özkan, Hasan",
        month="01/2025",
        pension_amount=150.00
    )

    assert pension.staff_id == 1011
    assert pension.name == "Özkan, Hasan"
    assert pension.month == "01/2025"
    assert pension.pension_amount == 150.00
