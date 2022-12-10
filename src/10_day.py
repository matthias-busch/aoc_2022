"""
https://adventofcode.com/2022/day/10
"""

from aoc2022_utils import read_input_file

# Input Processing
raw_input = read_input_file('10')
lines = raw_input.splitlines()

instructions = [instruction.split(' ') for instruction in lines]
instructions = [ [pair[0], int(pair[1])] if len(pair) > 1 else [pair[0]] for pair in instructions]

X = 1
cycle = 0
sum_signal_strength = 0

for instruction in instructions:
    if instruction[0] == 'noop':
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            sum_signal_strength += X * cycle

    elif instruction[0] == 'addx':
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            sum_signal_strength += X * cycle
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            sum_signal_strength += X * cycle

        X += instruction[1]


solution_1 = sum_signal_strength
print(f'{solution_1 = }')
