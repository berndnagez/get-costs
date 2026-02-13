from src.get_refunds.refunds_models import Refund


def test_refund_model():
    refund = Refund(
        staff_id="01011",
        name="Özkan, Hasan",
        month="01/2025",
        levy_type="U1",
        last_day="10.01.2025",
        refunds_start_day="13.01.2025",
        refunds_end_day="22.01.2025",
        data_id="4dad0b100154487ebf75",
        data_transfer_day="19.02.2025",
        refund_amount="809,17"
    )

    assert refund.staff_id == "01011"
    assert refund.name == "Özkan, Hasan"
    assert refund.month == "01/2025"
    assert refund.levy_type == "U1"
    assert refund.last_day == "10.01.2025"
    assert refund.refunds_start_day == "13.01.2025"
    assert refund.refunds_end_day == "22.01.2025"
    assert refund.data_id == "4dad0b100154487ebf75"
    assert refund.data_transfer_day == "19.02.2025"
    assert refund.refund_amount == "809,17"
    assert refund.status is None
