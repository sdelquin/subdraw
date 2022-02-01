import itertools

import typer

SUBJECTS_FILENAME = 'subjects.csv'
WEEKLY_TEACHING_HOURS = 18

app = typer.Typer(add_completion=False)


def get_subjects(filename):
    subjects = {}
    with open(filename) as f:
        for line in f:
            fields = line.strip().split(',')
            subject_group = f'{fields[0]}-{fields[-1]}'
            hours = int(fields[1])
            subjects[subject_group] = hours
    return subjects


def get_combinations(subjects, hours, max_size):
    max_size = max_size if max_size > 0 else len(subjects)
    for size in range(max_size):
        for combination in itertools.combinations(subjects, size + 1):
            combination_hours = sum(subjects[s] for s in combination)
            if combination_hours == hours:
                print(f'{combination} -> {hours}')


@app.command()
def run(
    filename: str = typer.Option(
        SUBJECTS_FILENAME,
        '--filename',
        '-i',
        help='Subjects filename',
    ),
    hours: int = typer.Option(
        WEEKLY_TEACHING_HOURS,
        '--hours',
        '-h',
        help='Number of hours to reach with subject combinations',
    ),
    max_size: int = typer.Option(
        -1,
        '--max-size',
        '-s',
        help='Maximum size for subject combinations',
    ),
):
    subjects = get_subjects(filename)
    get_combinations(subjects, hours, max_size)


if __name__ == '__main__':
    app()
