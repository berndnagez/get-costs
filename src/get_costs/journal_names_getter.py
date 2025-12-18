import os

def get_journal_names(path):
    journal_names = os.listdir(path)
    # iteration to remove lock-files
    for journal_name in journal_names:
        if "~lock" in journal_name:
            journal_names.remove(journal_name)
    return sorted(journal_names)