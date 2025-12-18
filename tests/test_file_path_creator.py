from src.get_costs import path_creator
import pytest

def test_validate_file_exists():
    with pytest.raises(path_creator.PathNotFoundError):
        path_creator.validate_path_exists(["./data/24_01_24 Lohnjournal Januar 2024.xlsx", "./data/24_02_24 Lohnjournal Januar 2024.xlsx"])

    path_creator.validate_path_exists(["main.py"])