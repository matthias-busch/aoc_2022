"""
https://adventofcode.com/2022/day/4
"""

from aoc2022_utils import read_input_file

# Input Processing
raw_input = read_input_file('04')

lines = raw_input.splitlines()

lists = [line.split(',') for line in lines]

sections = [[item.split('-') for item in list] for list in lists]

# Part one
def sections_fully_overlapped(sections: list[list[str],list[str]]) -> bool:
    section_1 = set(list(range(int(sections[0][0]), int(sections[0][1]) + 1)))
    section_2 = set(list(range(int(sections[1][0]), int(sections[1][1]) + 1)))

    return ( section_1.issubset(section_2) or section_2.issubset(section_1) )

# Part two
def sections_partially_overlapped(sections: list[list[str],list[str]]) -> bool:
    section_1 = set(list(range(int(sections[0][0]), int(sections[0][1]) + 1)))
    section_2 = set(list(range(int(sections[1][0]), int(sections[1][1]) + 1)))

    if len(section_1.intersection(section_2)) > 0 :
        partial_overlap = True
    else:
        partial_overlap = False

    return partial_overlap


# Results
solution_1 = sum([sections_fully_overlapped(section) for section in sections])
print(f'{solution_1 = }')

solution_2 = sum([sections_partially_overlapped(section) for section in sections])
print(f'{solution_2 = }')
