"""
https://adventofcode.com/2022/day/1
"""

with open(rf'../inputs/01_input.txt', encoding='utf-8') as fh:
    raw_input = fh.read()

# split input in elves -- list of lists with elves' calories
elves = [elf.splitlines() for elf in raw_input.split('\n\n')]
# convert to int for calculations
elves = [[int(calories) for calories in elf] for elf in elves]

calories = [sum(calories) for calories in elves]

solution_1 = max(calories)
solution_2 = sum(sorted(calories, reverse=True)[:3])

print(f'{solution_1 = }')
print(f'{solution_2 = }')






