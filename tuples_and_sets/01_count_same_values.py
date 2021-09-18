numbers = tuple([float(x) for x in input().split()])
occurrences = {}

for num in numbers:
    if not num in occurrences:
        occurrences[num] = 0
    occurrences[num] += 1

for key, value in occurrences.items():
    print(f"{key} - {value} times")


# v.2

import sys
from io import StringIO

test_input1 = '-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3'
test_input2 = '2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3'

sys.stdin = StringIO(test_input2)

numbers = [float(x) for x in input().split(' ')]
# numbers = tuple(map(float, input().split(' ')))

numbers_counts = {}

for number in numbers:
    if number not in numbers_counts:
        numbers_counts[number] = 0
    numbers_counts[number] += 1

for number, count in numbers_counts.items():
    print(f'{number} - {count} times')

# ^ actual task
# v additional stuff

sorted_numbers_by_counter =\
    sorted((value, key) for key, value in numbers_counts.items())
print(sorted_numbers_by_counter)