import typer

import settings
from subdraw import core

app = typer.Typer(add_completion=False)


@app.command()
def run(
    filename: str = typer.Option(
        settings.SUBJECTS_FILENAME,
        '--filename',
        '-i',
        help='Subjects filename',
    ),
    hours: int = typer.Option(
        settings.WEEKLY_TEACHING_HOURS,
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
    subjects = core.get_subjects(filename)
    for combination in core.get_combinations(subjects, hours, max_size):
        core.show_combination(combination)


if __name__ == '__main__':
    app()
