"""
https://adventofcode.com/2022/day/3
"""

from typing import List, Set

from aoc2022_utils import read_input_file


def split_compartments(rucksack: str) -> list[set[str], set[str]]:
    size = len(rucksack)
    split_index = int((size / 2))

    return [set(rucksack[:split_index]), set(rucksack[split_index:])]

def calculate_priorities(rucksacks: list[set[str]]) -> int:
    import string
    lower_case_priorities = {k:v for (k,v) in zip(string.ascii_lowercase, range(1,27))}
    upper_case_priorities = {k:v for (k,v) in zip(string.ascii_uppercase, range(27,53))}
    union_priorities = lower_case_priorities | upper_case_priorities

    intersection = set.intersection(*rucksacks)

    return sum([union_priorities[item] for item in intersection])

raw_input = read_input_file(day='03')
rucksacks = raw_input.splitlines()

# Part one
compartments = [split_compartments(rucksack) for rucksack in rucksacks]

# Part two
rucksack_sets = [set(rucksack) for rucksack in rucksacks]
triplets = [rucksack_sets[x:x+3] for x in range(0, len(rucksack_sets), 3)]


# Results
solution_1 = sum([calculate_priorities(compartment) for compartment in compartments])
print(f'{solution_1 = }')
solution_2 = sum([calculate_priorities(triplet) for triplet in triplets])
print(f'{solution_2 = }')
