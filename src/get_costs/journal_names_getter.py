import os
import get_costs.config

def get_journal_names():
    journal_names = os.listdir(get_costs.config.PATH_TO_DATA_FOLDER)
    return sorted(journal_names)