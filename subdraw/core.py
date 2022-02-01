import itertools


def get_subjects(filename):
    subjects = {}
    with open(filename) as f:
        for line in f:
            fields = line.strip().split(',')
            subject_group = f'{fields[0]}-{fields[-1]}'
            hours = int(fields[1])
            subjects[subject_group] = hours
    return subjects


def combination_has_subjects(combination: tuple, subjects: tuple[str]):
    matches = 0
    for subject in subjects:
        for item in combination:
            if subject in item:
                matches += 1
                break
    return matches == len(subjects)


def combination_hasnot_subjects(combination: tuple, subjects: tuple[str]):
    for subject in subjects:
        for item in combination:
            if subject in item:
                return False
    return True


def get_combinations(
    subjects: dict, hours, max_size, include: tuple[str], exclude: tuple[str]
):
    max_size = max_size if max_size > 0 else len(subjects)
    for size in range(max_size):
        for combination in itertools.combinations(subjects, size + 1):
            if ((not include) or combination_has_subjects(combination, include)) and (
                (not exclude) or combination_hasnot_subjects(combination, exclude)
            ):
                combination_hours = sum(subjects[s] for s in combination)
                if combination_hours == hours:
                    yield combination, hours


def show_combination(combination: tuple[tuple[str], int]):
    subjects = ', '.join(combination[0])
    hours = combination[1]
    print(f'{subjects} -> {hours}')
