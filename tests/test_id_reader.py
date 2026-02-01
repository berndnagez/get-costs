import numpy as np
from src.get_costs import id_reader


def test_get_all_ids_from():
    file = "../../1036 Siebert und Partner/- 06 Lohnabrechnung _ Journal/2025/- 01 Lohnjournale/25_09_11 Lohnjournal September 2025.xlsx"
    sheet_name = "first_sheet"
    expected_ids = [np.int64(1001), np.int64(1004), np.int64(1005), np.int64(1011), np.int64(1015), np.int64(1019), np.int64(1022), np.int64(1026), np.int64(1028), np.int64(1029), np.int64(1030), np.int64(1031), np.int64(1034), np.int64(1035), np.int64(1036), np.int64(1038), np.int64(1139), np.int64(
        1140), np.int64(1141), np.int64(1142), np.int64(1143), np.int64(1144), np.int64(1145), np.int64(1146), np.int64(1147), np.int64(1148), np.int64(1149), np.int64(1150), np.int64(1151), np.int64(1152), np.int64(1154), np.int64(1155), np.int64(1158), np.int64(1159), np.int64(1160), np.int64(1161), np.int64(1162)]
    returned_ids = id_reader.get_all_ids_from(file, sheet_name)
    assert expected_ids == returned_ids


def test_get_project_ids_from():
    file = "./- 01 Rohdaten Zur Auswertung/2025/employee_data_2025.xlsx"
    sheet_name = "25_09"
    project = "0026"
    expected_ids = [1004, 1139, 1145, 1154]
    returned_ids = id_reader.get_project_ids_from(file, sheet_name, project)
    assert expected_ids == returned_ids
