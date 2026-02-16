from src.get_refunds.refunds_reader import RefundsReader
from src.get_refunds.refunds_models import Refund


def test_read():
    file_path = "tests/test_data/26_01_21 Übersicht Krankmeldungen Januar 2026.txt"
    reader = RefundsReader()
    refunds = reader.read(file_path)

    assert len(refunds) == 16

    for r in refunds:
        assert isinstance(r, Refund)

    assert refunds[0].staff_id == 1147
    assert refunds[0].name == "Arda, Recep"
    assert refunds[0].data_id == "b4726fbb95654936b9ba"
    assert refunds[0].refund_amount == "129,60"
    assert refunds[0].status is None
    assert refunds[2].levy_type == "U2-BV"
    assert refunds[2].last_day is None
    assert refunds[4].month is None

    file_path = "tests/test_data/25_01_22 Übersicht Krankmeldungen Januar 2025.txt"
    reader = RefundsReader()
    refunds = reader.read(file_path)

    assert len(refunds) == 38

    assert refunds[29].status == "S"

    file_path = "tests/test_data/25_06_20 Übersicht Krankmeldungen Juni 2025.txt"
    reader = RefundsReader()
    refunds = reader.read(file_path)

    assert len(refunds) == 11


def test_get_all_lines(tmp_path):
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("P-Nr. Name                  NB-      Umlage  Letzter Tag  Erstattung  Erstattung  Datensatz-ID          DÜ am         Erstattung\n01011 Özkan, Hasan          01/2025  U1      10.01.2025   13.01.2025  22.01.2025  4dad0b100154487ebf75  19.02.2025        809,17", encoding="windows-1252")

    reader = RefundsReader()
    lines = reader.get_all_lines(file_path)

    assert lines == ["P-Nr. Name                  NB-      Umlage  Letzter Tag  Erstattung  Erstattung  Datensatz-ID          DÜ am         Erstattung\n",
                     "01011 Özkan, Hasan          01/2025  U1      10.01.2025   13.01.2025  22.01.2025  4dad0b100154487ebf75  19.02.2025        809,17"]


def test_extract_refunds():
    lines = [
        "P-Nr. Name                  NB-      Umlage  Letzter Tag  Erstattung  Erstattung  Datensatz-ID          DÜ am         Erstattung\n",
        "01011 Özkan, Hasan          01/2025  U1      10.01.2025   13.01.2025  22.01.2025  4dad0b100154487ebf75  19.02.2025        809,17",
        "01015 Barrientos, J.        12/2024  U1      05.12.2024   06.12.2024  13.12.2024                        19.02.2025        468,55  S"
    ]
    reader = RefundsReader()
    refunds = reader.extract_refunds(lines)

    assert len(refunds) == 2

    for r in refunds:
        assert isinstance(r, Refund)

    assert refunds[0].staff_id == 1011
    assert refunds[0].name == "Özkan, Hasan"
    assert refunds[0].data_id == "4dad0b100154487ebf75"
    assert refunds[0].refund_amount == "809,17"
    assert refunds[0].status is None
    assert refunds[1].staff_id == 1015
    assert refunds[1].name == "Barrientos, J."
    assert refunds[1].data_id is None
    assert refunds[1].refund_amount == "468,55"
    assert refunds[1].status == "S"
