from src.get_refunds.refunds_mapper import RefundsMapper
from src.get_refunds.refunds_models import Refund


def test_to_dict():
    refund = Refund(
        staff_id=1011,
        name="Özkan, Hasan",
        month="01/2025",
        levy_type="U1",
        last_day="10.01.2025",
        refunds_start_day="13.01.2025",
        refunds_end_day="22.01.2025",
        data_id="4dad0b100154487ebf75",
        data_transfer_day="19.02.2025",
        refund_amount="809,17",
        status=None
    )

    result = RefundsMapper.to_dict(refund)

    assert result["title"] == "U1 Özkan, Hasan 13. - 22.01.25"
    assert result["staff_id"] == 1011
    assert result["month"] == "01/2025"
    assert result["refund_amount"] == "809,17"
    assert result["status"] == None

    refund = Refund(
        staff_id=1011,
        name="Özkan, Hasan",
        month="01/2025",
        levy_type="U1",
        last_day="10.01.2025",
        refunds_start_day="13.01.2025",
        refunds_end_day="13.01.2025",
        data_id="4dad0b100154487ebf75",
        data_transfer_day="19.02.2025",
        refund_amount="809,17",
        status=None
    )

    result = RefundsMapper.to_dict(refund)

    assert result["title"] == "U1 Özkan, Hasan 13.01.25"
    assert result["staff_id"] == 1011
    assert result["month"] == "01/2025"
    assert result["refund_amount"] == "809,17"
    assert result["status"] == None


def test_list_to_dict():
    refunds = [
        Refund(
            staff_id=1011,
            name="Özkan, Hasan",
            month="01/2025",
            levy_type="U1",
            last_day="10.01.2025",
            refunds_start_day="13.01.2025",
            refunds_end_day="22.01.2025",
            data_id="4dad0b100154487ebf75",
            data_transfer_day="19.02.2025",
            refund_amount="809,17",
            status=None
        ),
        Refund(
            staff_id=1015,
            name="Barrientos, J.",
            month="12/2024",
            levy_type="U1",
            last_day="05.12.2024",
            refunds_start_day="06.12.2024",
            refunds_end_day="13.12.2024",
            data_id=None,
            data_transfer_day="19.02.2025",
            refund_amount="468,55",
            status="S"
        )
    ]

    result = RefundsMapper.list_to_dict(refunds)

    assert len(result) == 2
    assert result[0]["title"] == "U1 Özkan, Hasan 13. - 22.01.25"
    assert result[0]["staff_id"] == 1011
    assert result[0]["month"] == "01/2025"
    assert result[0]["refund_amount"] == "809,17"
    assert result[0]["status"] == None

    assert result[1]["title"] == "U1 Barrientos, J. 06. - 13.12.24"
    assert result[1]["staff_id"] == 1015
    assert result[1]["month"] == "12/2024"
    assert result[1]["refund_amount"] == "468,55"
    assert result[1]["status"] == "S"


def test_format_period():
    assert RefundsMapper.format_period(
        "13.01.2025", "22.01.2025") == "13. - 22.01.25"
    assert RefundsMapper.format_period(
        "13.01.2025", "13.01.2025") == "13.01.25"
    assert RefundsMapper.format_period(
        "30.12.2024", "05.01.2025") == "30.12.24 - 05.01.25"
