import hashlib
import itertools
import operator

from rich.console import Console
from rich.table import Table

import settings


class Subject:
    def __init__(self, subject, hours, group):
        self.subject = subject
        self.group = group
        self.hours = int(hours)

    def has_pattern(self, pattern):
        if len(m := pattern.split(settings.SUBJECT_DELIMITER)) > 1:
            return m[0] in self.subject and m[1] in self.group
        return pattern in self.subject or pattern in self.group

    def __str__(self):
        return f'{self.subject}{settings.SUBJECT_DELIMITER}{self.group} ({self.hours})'

    @property
    def color(self):
        if settings.OUTPUT_COLOR:
            payload = self.subject + self.group
            hash = int(hashlib.md5(payload.encode('utf-8')).hexdigest(), base=16)
            color_index = hash % len(settings.SUBJECT_COLORS)
            return settings.SUBJECT_COLORS[color_index]
        return settings.REGULAR_COLOR


class Schedule:
    def __init__(self, subjects: tuple[Subject]):
        self.subjects = sorted(subjects, key=operator.attrgetter('group'))

    @property
    def hours(self):
        return sum(s.hours for s in self.subjects)

    @property
    def num_groups(self):
        return len(set(s.group for s in self.subjects))

    @property
    def hours_color(self):
        if settings.OUTPUT_COLOR:
            color_index = self.hours % len(settings.HOURS_COLORS)
            return settings.HOURS_COLORS[color_index]
        return settings.REGULAR_COLOR

    def has_patterns(self, patterns: tuple[str]):
        matches = 0
        for pattern in patterns:
            for subject in self.subjects:
                if subject.has_pattern(pattern):
                    matches += 1
                    break
        return matches == len(patterns)

    def lack_patterns(self, patterns: tuple[str]):
        for pattern in patterns:
            for subject in self.subjects:
                if subject.has_pattern(pattern):
                    return False
        return True

    def __len__(self):
        return len(self.subjects)


class SubDraw:
    def __init__(self, filename):
        self.subjects = self.load_subjects(filename)

    def load_subjects(self, filename):
        subjects = []
        with open(filename) as f:
            for line in f:
                fields = line.strip().split(',')
                subject = Subject(*fields)
                subjects.append(subject)
        return subjects

    def get_schedules(
        self,
        hours=settings.WEEKLY_TEACHING_HOURS,
        hours_range=0,
        max_size=-1,
        max_groups=-1,
        include: tuple[str] = [],
        exclude: tuple[str] = [],
    ):
        self.schedules = []
        self.max_schedule_size = 0
        max_size = max_size if max_size > 0 else len(self.subjects)
        for size in range(max_size):
            for subjects in itertools.combinations(self.subjects, size + 1):
                schedule = Schedule(subjects)
                if all(
                    [
                        (not include) or schedule.has_patterns(include),
                        (not exclude) or schedule.lack_patterns(exclude),
                        (hours - hours_range) <= schedule.hours <= (hours + hours_range),
                        max_groups < 0 or schedule.num_groups <= max_groups,
                    ],
                ):
                    self.max_schedule_size = max(self.max_schedule_size, len(schedule))
                    self.schedules.append(schedule)
        self.schedules = sorted(self.schedules, key=operator.attrgetter('hours'))

    def schedules_as_table(self):
        console = Console()
        table = Table()

        for col in range(self.max_schedule_size):
            table.add_column(f'S{col + 1}')
        table.add_column('G')
        table.add_column('H')

        for schedule in self.schedules:
            subjects = [f'[color({s.color})]{str(s)}[/]' for s in schedule.subjects]
            gaps = ['' for _ in range(len(schedule), self.max_schedule_size)]
            num_groups = str(schedule.num_groups)
            hours = f'[color({schedule.hours_color})]{schedule.hours}[/]'
            table.add_row(*subjects, *gaps, num_groups, hours)

        console.print(table)

    def schedules_as_csv(self, output_filename: str):
        f = open(output_filename, 'w')

        header = []
        for col in range(self.max_schedule_size):
            header.append(f'S{col + 1}')
        header.append('G')
        header.append('H')
        f.write(','.join(header) + '\n')

        for schedule in self.schedules:
            subjects = [str(s) for s in schedule.subjects]
            gaps = ['' for _ in range(len(schedule), self.max_schedule_size)]
            num_groups = str(schedule.num_groups)
            hours = str(schedule.hours)
            row = [*subjects, *gaps, num_groups, hours]
            f.write(','.join(row) + '\n')

        f.close()
