from src.get_refunds.refunds_service import RefundsService


def test_get_refunds_as_dict():
    file_path = "tests/test_data/26_01_21 Übersicht Krankmeldungen Januar 2026.txt"
    service = RefundsService()
    refunds_dict = service.get_refunds_as_dict(file_path)

    assert len(refunds_dict) == 16

    first_refund = refunds_dict[0]
    assert first_refund["title"] == "U1 Arda, Recep 16. - 17.12.25"
    assert first_refund["staff_id"] == "01147"
    assert first_refund["month"] == "12/2025"
    assert first_refund["refund_amount"] == "129,60"
    assert first_refund["status"] is None
