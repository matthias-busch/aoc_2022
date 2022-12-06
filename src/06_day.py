"""
https://adventofcode.com/2022/day/5
"""

from aoc2022_utils import read_input_file

# Input Processing
raw_input = read_input_file('06')


def find_start_marker(input: str, no_distinct_chars: int) -> int:
    start = 0
    end = no_distinct_chars
    tmp_signal = raw_input[:no_distinct_chars]

    for i in range(len(raw_input)):
        if len(set(tmp_signal)) == no_distinct_chars:
            return end - 1
        else:
            tmp_signal = raw_input[start:end]
            start += 1
            end += 1


# Results
solution_1 = find_start_marker(input=raw_input, no_distinct_chars=4)
print(f'{solution_1 = }')

solution_2 = find_start_marker(input=raw_input, no_distinct_chars=14)
print(f'{solution_2 = }')
