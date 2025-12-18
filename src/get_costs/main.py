#!/usr/bin/env python3

from sys import argv
# own modules
from choice_getter import get_choice
from result_file_creator import create_result_file_for, create_result_file_for_all_projects, create_result_file_for_project_with

#TODO feature request: Bonus mit einbauen (siehe 24_12_18 Lohnjournal Dezember 2024.xlsx), Schwierigkeit: keine Extraspalte für den Bonus,
# kommt einfach in den Spalten "Gesamtbrutto" und "Auszahlungsbetrag" dazu

#TODO einmal alle Dateien durchgehen = werden sie noch benutzt? Sonst löschen
# aber vielleicht erst, wenn die Funktionaliät für Paul da ist

def print_project_id_info():
    print(f'Folgendes Projekt wurde gewählt: {project_id}.')
    print(f'Es wird die Datei "{project_id}.xlsx" erzeugt.')


def print_journal_info():
    print(f'Folgendes Lohnjournal wurde gewählt: {journal}.')


def print_project_info_and_journal_info():
    print(f'Für das Projekt "{project_id}" wird folgendes Lohnjournal ausgewertet: "{journal}".')
    print(f'Es wird die Datei "{project_id}.xlsx" erzeugt.')

if __name__ == "__main__":
    choice = get_choice(argv[1:])
    if len(choice) == 1:
        opt, arg = choice[0]
        if opt in ('-p', '--project'):
            project_id = arg
            print_project_id_info()
            # TODO checken der These: nimmt einfach alle Dateien einen Ordners. Gut wäre es, wenn ein Zeitraum bspw. Zuwendungsjahr comMIT!mennt oder Kalenderjahr definiert werden könnte
            create_result_file_for(project_id)
        elif opt in ('-i', '--ifile'):
            journal = arg
            print_journal_info()
            create_result_file_for_all_projects(journal)
    else:
        for opt, arg in choice:
            if opt in ('-p', '--project'):
                project_id = arg
            elif opt in ('-i', '--ifile'):
                journal = arg
        print_project_info_and_journal_info()
        create_result_file_for_project_with(journal, project_id)
    print("Fertig.")