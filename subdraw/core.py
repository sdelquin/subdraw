import itertools
import operator

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
        return f'{self.subject}{settings.SUBJECT_DELIMITER}{self.group}({self.hours})'


class Schedule:
    def __init__(self, subjects: tuple[Subject]):
        self.subjects = sorted(subjects, key=operator.attrgetter('group'))

    @property
    def hours(self):
        return sum(s.hours for s in self.subjects)

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

    def __str__(self):
        items = ', '.join(str(s) for s in self.subjects)
        return f'{items} -> {self.hours}h'


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

    def get_schedules(self, hours, max_size, include: tuple[str], exclude: tuple[str]):
        max_size = max_size if max_size > 0 else len(self.subjects)
        for size in range(max_size):
            for subjects in itertools.combinations(self.subjects, size + 1):
                schedule = Schedule(subjects)
                if ((not include) or schedule.has_patterns(include)) and (
                    (not exclude) or schedule.lack_patterns(exclude)
                ):
                    if schedule.hours == hours:
                        yield schedule

    def __str__(self):
        return '\n'.join(str(s) for s in self.subjects)
