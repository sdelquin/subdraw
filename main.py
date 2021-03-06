from pathlib import Path

import typer

import settings
from subdraw import core

app = typer.Typer(add_completion=False)


@app.command()
def run(
    filename: Path = typer.Option(
        settings.SUBJECTS_FILENAME,
        '--filename',
        '-f',
        help='Subjects filename (csv format)',
    ),
    hours: int = typer.Option(
        settings.WEEKLY_TEACHING_HOURS,
        '--hours',
        '-h',
        help='Number of hours to reach within each schedule',
    ),
    hours_range: int = typer.Option(
        0,
        '--hours-range',
        '-r',
        help='Schedules will be in [hours - hours-range, hours + hours-range]',
    ),
    max_size: int = typer.Option(
        -1,
        '--max-size',
        '-s',
        help='Maximum number of subjects within each schedule. If -1 all sizes are valid.',
    ),
    gmin: int = typer.Option(
        1, '--gmin', help='Minimum number of (different) groups within each schedule.'
    ),
    gmax: int = typer.Option(
        -1,
        '--gmax',
        help='Maximum number of (different) groups within each schedule. '
        'If -1 no restriction is applied.',
    ),
    smin_hours: int = typer.Option(
        1, '--smin', help='Minimum number of hours for each subject in schedule. '
    ),
    smax_hours: int = typer.Option(
        settings.MAX_HOURS_PER_WEEK,
        '--smax',
        help='Maximum number of hours for each subject in schedule. ',
    ),
    include: list[str] = typer.Option(
        None, '--include', '-i', help='Include this subject, group or subject-group.'
    ),
    exclude: list[str] = typer.Option(
        None, '--exclude', '-x', help='Exclude this subject, group or subject-group.'
    ),
    distinct_subjects: bool = typer.Option(
        False,
        '--distinct-subjects',
        '-d',
        help='All subjects (without group) must be different.',
    ),
    no_color: bool = typer.Option(False, '--no-color', help='Not colorized output.'),
    output_filename: Path = typer.Option(
        None,
        '--output',
        '-o',
        help='Output schedules to this filename in csv format.',
    ),
):
    settings.OUTPUT_COLOR = not no_color
    subdraw = core.SubDraw(filename)
    subdraw.get_schedules(
        hours,
        hours_range,
        max_size,
        gmin,
        gmax,
        smin_hours,
        smax_hours,
        include,
        exclude,
        distinct_subjects,
    )
    if output_filename:
        subdraw.schedules_as_csv(output_filename)
    else:
        subdraw.schedules_as_table()


if __name__ == '__main__':
    app()
