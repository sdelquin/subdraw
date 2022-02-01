from prettyconf import config

SUBJECTS_FILENAME = config('SUBJECTS_FILENAME', default='subjects.csv')
WEEKLY_TEACHING_HOURS = config('WEEKLY_TEACHING_HOURS', default=18, cast=int)
