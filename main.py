import typer

import settings
from subdraw.core import SubDraw

app = typer.Typer(add_completion=False)


@app.command()
def run(
    filename: str = typer.Option(
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
    max_size: int = typer.Option(
        -1,
        '--max-size',
        '-s',
        help='Maximum number of subjects within each schedule. If -1 all sizes are valid.',
    ),
    include: list[str] = typer.Option(
        None, '--include', '-i', help='Include this subject, group or subject-group'
    ),
    exclude: list[str] = typer.Option(
        None, '--exclude', '-x', help='Exclude this subject, group or subject-group'
    ),
):
    subdraw = SubDraw(filename)
    for schedule in subdraw.get_schedules(hours, max_size, include, exclude):
        print(schedule)


if __name__ == '__main__':
    app()
