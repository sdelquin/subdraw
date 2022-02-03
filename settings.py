from prettyconf import config

SUBJECTS_FILENAME = config('SUBJECTS_FILENAME', default='subjects.csv')
WEEKLY_TEACHING_HOURS = config('WEEKLY_TEACHING_HOURS', default=18, cast=int)
SUBJECT_DELIMITER = config('SUBJECT_DELIMITER', default='-')
MAX_HOURS_PER_WEEK = config('MAX_HOURS_PER_WEEK', default=30, cast=int)

# https://rich.readthedocs.io/en/latest/appendix/colors.html#appendix-colors
OUTPUT_COLOR = config('OUTPUT_COLOR', default=True, cast=int)
REGULAR_COLOR = config('REGULAR_COLOR', default=7, cast=int)
SUBJECT_COLORS = [9, 10, 11, 12, 13, 14, 40, 101, 172, 190]
HOURS_COLORS = [9, 10, 11, 12, 13, 14]
