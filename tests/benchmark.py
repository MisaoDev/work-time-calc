import sys

sys.path.append('src')

import datetime
from random import randint
from work_time_calc.calc import WorkTimeCalculator


CHILE_HOLIDAYS = [
    (2023, 1, 1),
    (2023, 1, 2),
    (2023, 4, 7),
    (2023, 4, 8),
    (2023, 4, 9),
    (2023, 5, 1),
    (2023, 5, 21),
    (2023, 6, 7),
    (2023, 6, 21),
    (2023, 6, 26),
    (2023, 7, 16),
    (2023, 8, 15),
    (2023, 8, 20),
    (2023, 9, 18),
    (2023, 9, 19),
    (2023, 10, 9),
    (2023, 10, 27),
    (2023, 11, 1),
    (2023, 12, 8),
    (2023, 12, 25),
]


NUMBER_OF_TESTS = 100000


results = []
list1 = [
    datetime.datetime(
        2023,
        randint(1, 12),
        randint(1, 28),
        randint(0, 23),
        randint(0, 59),
        randint(0, 59),
    )
    for _ in range(NUMBER_OF_TESTS)
]
list2 = [
    datetime.datetime(
        2023,
        randint(1, 12),
        randint(1, 28),
        randint(0, 23),
        randint(0, 59),
        randint(0, 59),
    )
    for _ in range(NUMBER_OF_TESTS)
]

calc = WorkTimeCalculator(9, 17, '1111100')
start_time = datetime.datetime.now()
for i in range(NUMBER_OF_TESTS):
    delta = calc(list1[i], list2[i])
    results.append(delta.seconds)
benchmark = datetime.datetime.now() - start_time

print('Number of tests:', NUMBER_OF_TESTS)
print('Benchmark:', benchmark.total_seconds())
