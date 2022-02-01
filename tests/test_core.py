import pytest

import settings
from subdraw.core import Schedule, SubDraw, Subject


@pytest.fixture
def subdraw(scope='module'):
    return SubDraw('tests/subjects.csv')


@pytest.fixture
def subject(scope='module'):
    return Subject('VAO', 1, 'ESO1A')


@pytest.fixture
def schedule(scope='module'):
    subject1 = Subject('MAT', 2, 'ESO1A')
    subject2 = Subject('LCL', 3, 'ESO1A')
    subject3 = Subject('PLW', 5, 'ESO1A')
    return Schedule((subject1, subject2, subject3))


def test_subjects_are_loaded(subdraw):
    assert len(subdraw.subjects) == 10
    assert all(type(s) == Subject for s in subdraw.subjects)
    assert all(s.group.startswith('ESO') for s in subdraw.subjects)


def test_subject_has_pattern(subject):
    assert subject.has_pattern('VAO')
    assert subject.has_pattern('ESO1A')
    assert subject.has_pattern('VAO-ESO1A')
    assert not subject.has_pattern('MAT')


def test_schedule_has_patterns(schedule):
    assert schedule.has_patterns(('MAT', 'ESO1A'))
    assert schedule.lack_patterns(('VAO', 'ESO1B'))


def test_schedule_has_right_hours(schedule):
    assert schedule.hours == 10


def test_schedules_have_given_hours(subdraw):
    schedules = list(subdraw.get_schedules(hours=10))
    assert all(s.hours == 10 for s in schedules)
    assert len(schedules) == 42


def test_schedules_have_default_hours(subdraw):
    schedules = list(subdraw.get_schedules())
    assert all(s.hours == settings.WEEKLY_TEACHING_HOURS for s in schedules)


def test_schedules_have_given_size(subdraw):
    schedules = list(subdraw.get_schedules(hours=12, max_size=4))
    assert all(len(s) <= 4 for s in schedules)