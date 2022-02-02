from prettyconf import config

SUBJECTS_FILENAME = config('SUBJECTS_FILENAME', default='subjects.csv')
WEEKLY_TEACHING_HOURS = config('WEEKLY_TEACHING_HOURS', default=18, cast=int)
SUBJECT_DELIMITER = config('SUBJECT_DELIMITER', default='-')

OUTPUT_COLOR = config('OUTPUT_COLOR', default=True, cast=int)
OUTPUT_STD_COLOR = config('OUTPUT_STD_COLOR', default=7, cast=int)
OUTPUT_MAX_COLOR = config('OUTPUT_MAX_COLOR', default=15, cast=int)
