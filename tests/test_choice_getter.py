import pytest
from src.get_costs import choice_getter


def test_get_choice():
    excepted_result = [('-i', 'journal.xlsx')]
    returned_result = choice_getter.get_choice(('-i', 'journal.xlsx'))
    assert returned_result == excepted_result

    excepted_result = [('-p', '0026')]
    returned_result = choice_getter.get_choice(('-p', '0026'))
    assert returned_result == excepted_result

    excepted_result = [('-i', 'journal.xlsx'), ('-p', '0026')]
    returned_result = choice_getter.get_choice(
        ('-i', 'journal.xlsx', '-p', '0026'))
    assert returned_result == excepted_result

    excepted_result = [('--ifile', 'journal.xlsx'), ('--project', '0026')]
    returned_result = choice_getter.get_choice(
        ('--ifile', 'journal.xlsx', '--project', '0026'))
    assert returned_result == excepted_result

    excepted_result = [('--ifile', 'journal.xlsx')]
    returned_result = choice_getter.get_choice(('--ifile', 'journal.xlsx'))
    assert returned_result == excepted_result

    excepted_result = [('--project', '0026')]
    returned_result = choice_getter.get_choice(('--project', '0026'))
    assert returned_result == excepted_result


def test_get_choice_no_arguments(capfd):

    with pytest.raises(SystemExit) as sample:
        choice_getter.get_choice([])

    captured = capfd.readouterr()

    assert "Missing argument. Exit" in captured.out
    assert "" in captured.out
    assert "usage: main.py [-h] -i -p" in captured.out
    assert "" in captured.out
    assert "options:" in captured.out
    assert "-h, --help show this help message and exit" in captured.out
    assert "" in captured.out
    assert "positional arguments:" in captured.out
    assert "-i, --ifile <name of one journal>" in captured.out
    assert "-p, --project <project id of one project>" in captured.out
    assert "" in captured.out
    assert "" in captured.out
    assert sample.type == SystemExit
    assert sample.value.code == None


def test_get_choice_help_argument(capfd):

    with pytest.raises(SystemExit) as sample:
        choice_getter.get_choice(['-h'])

    captured = capfd.readouterr()

    assert "usage: main.py [-h] -i -p" in captured.out
    assert "" in captured.out
    assert "options:" in captured.out
    assert "-h, --help show this help message and exit" in captured.out
    assert "" in captured.out
    assert "positional arguments:" in captured.out
    assert "-i, --ifile <name of one journal>" in captured.out
    assert "-p, --project <project id of one project>" in captured.out
    assert "" in captured.out
    assert "" in captured.out
    assert sample.type == SystemExit
    assert sample.value.code == None


def test_get_choice_help_argument_long(capfd):

    with pytest.raises(SystemExit) as sample:
        choice_getter.get_choice(['--help'])

    captured = capfd.readouterr()

    assert "usage: main.py [-h] -i -p" in captured.out
    assert "" in captured.out
    assert "options:" in captured.out
    assert "-h, --help show this help message and exit" in captured.out
    assert "" in captured.out
    assert "positional arguments:" in captured.out
    assert "-i, --ifile <name of one journal>" in captured.out
    assert "-p, --project <project id of one project>" in captured.out
    assert "" in captured.out
    assert "" in captured.out
    assert sample.type == SystemExit
    assert sample.value.code == None


def test_get_choice_GetoptError_argument(capfd):

    with pytest.raises(SystemExit) as sample:
        choice_getter.get_choice(['-x'])

    captured = capfd.readouterr()

    assert "usage: main.py [-h] -i -p" in captured.out
    assert "" in captured.out
    assert "options:" in captured.out
    assert "-h, --help show this help message and exit" in captured.out
    assert "" in captured.out
    assert "positional arguments:" in captured.out
    assert "-i, --ifile <name of one journal>" in captured.out
    assert "-p, --project <project id of one project>" in captured.out
    assert "" in captured.out
    assert "" in captured.out
    assert sample.type == SystemExit
    assert sample.value.code == 2
