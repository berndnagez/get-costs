from src.get_costs import id_merger


def test_merge_ids():
    journal_data_file = "../../1036 Siebert und Partner/- 06 Lohnabrechnung _ Journal/2025/- 01 Lohnjournale/25_09_11 Lohnjournal September 2025.xlsx"
    employee_data_file = "./- 01 Rohdaten Zur Auswertung/2025/employee_data_2025.xlsx"
    provisions_data_file = "./- 01 Rohdaten Zur Auswertung/2025/provisions_data_2025.xlsx"
    additional_costs_file = "./- 01 Rohdaten Zur Auswertung/2025/additional_costs_2025.xlsx"

    merged_ids = id_merger.merge_ids(
        files=(journal_data_file, employee_data_file,
               provisions_data_file, additional_costs_file),
        sheet_name='25_09'
    )

    expected_ids = [1001, 1004, 1005, 1011, 1015, 1019, 1022, 1026, 1028, 1029, 1030, 1031, 1034, 1035, 1036, 1038, 1139, 1140,
                    1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1154, 1155, 1156, 1158, 1159, 1160, 1161, 1162, 1157]

    assert merged_ids == expected_ids
