import hashlib
import itertools
import operator
from functools import lru_cache

from rich.console import Console
from rich.table import Table

import settings
from subdraw import utils


class Subject:
    def __init__(self, subject, hours, group):
        self.subject = subject
        self.group = group
        self.hours = int(hours)
        self.hash = self.get_hash()
        self.color = self.get_color()

    @lru_cache
    def has_pattern(self, pattern: str):
        pattern = pattern.upper()
        subject = self.subject.upper()
        group = self.group.upper()

        if len(m := pattern.split(settings.SUBJECT_DELIMITER)) > 1:
            return m[0] in subject and m[1] in group
        return pattern in subject or pattern in group

    def __str__(self):
        return f'{self.subject}{settings.SUBJECT_DELIMITER}{self.group} ({self.hours})'

    def get_hash(self):
        return int(
            hashlib.md5((self.subject + self.group).encode('utf-8')).hexdigest(), base=16
        )

    def get_color(self):
        return utils.get_color(self.hash, settings.SUBJECT_COLORS, settings.OUTPUT_COLOR)


class Schedule:
    def __init__(self, subjects: tuple[Subject]):
        self.subjects = sorted(subjects, key=operator.attrgetter('group'))
        self.hours = sum(s.hours for s in self.subjects)
        self.num_groups = len(set(s.group for s in self.subjects))
        self.smin_hours = min(s.hours for s in self.subjects)
        self.smax_hours = max(s.hours for s in self.subjects)
        self.hours_color = self.get_hours_color()

    def get_hours_color(self):
        return utils.get_color(self.hours, settings.HOURS_COLORS, settings.OUTPUT_COLOR)

    @lru_cache
    def has_patterns(self, patterns: tuple[str]):
        matches = 0
        for pattern in patterns:
            for subject in self.subjects:
                if subject.has_pattern(pattern):
                    matches += 1
                    break
        return matches == len(patterns)

    @lru_cache
    def lack_patterns(self, patterns: tuple[str]):
        for pattern in patterns:
            for subject in self.subjects:
                if subject.has_pattern(pattern):
                    return False
        return True

    def __len__(self):
        return len(self.subjects)

    def satisfies(
        self,
        hours,
        hours_range,
        min_groups,
        max_groups,
        smin_hours,
        smax_hours,
        include,
        exclude,
    ):
        return all(
            [
                (not include) or self.has_patterns(include),
                (not exclude) or self.lack_patterns(exclude),
                (hours - hours_range) <= self.hours <= (hours + hours_range),
                self.num_groups >= min_groups,
                max_groups < 0 or self.num_groups <= max_groups,
                self.smin_hours >= smin_hours,
                self.smax_hours <= smax_hours,
            ]
        )


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
        min_groups=1,
        max_groups=-1,
        smin_hours=1,
        smax_hours=settings.MAX_HOURS_PER_WEEK,
        include: tuple[str] = [],
        exclude: tuple[str] = [],
    ):
        self.schedules = []
        self.max_schedule_size = 0
        max_size = max_size if max_size > 0 else len(self.subjects)
        for size in range(max_size):
            for subjects in itertools.combinations(self.subjects, size + 1):
                schedule = Schedule(subjects)
                if schedule.satisfies(
                    hours,
                    hours_range,
                    min_groups,
                    max_groups,
                    smin_hours,
                    smax_hours,
                    include,
                    exclude,
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

        if self.schedules:
            console.print(table)
            print(f'{len(self.schedules)} available schedules!')
        else:
            print('No schedules available!')

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
