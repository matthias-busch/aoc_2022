"""
https://adventofcode.com/2022/day/5
"""
import copy
import re
from collections import deque

from aoc2022_utils import read_input_file

# Input Processing
raw_input = read_input_file('05')

lines = raw_input.splitlines()

start_configuration = lines[:8]

stack_1 = re.findall(pattern=r'[A-Z]', string= ','.join([line[:3] for line in start_configuration]))
stack_2 = re.findall(pattern=r'[A-Z]', string=','.join([line[4:7] for line in start_configuration]))
stack_3 = re.findall(pattern=r'[A-Z]', string=','.join([line[8:11] for line in start_configuration]))
stack_4 = re.findall(pattern=r'[A-Z]', string=','.join([line[12:15] for line in start_configuration]))
stack_5 = re.findall(pattern=r'[A-Z]', string=','.join([line[16:19] for line in start_configuration]))
stack_6 = re.findall(pattern=r'[A-Z]', string=','.join([line[20:23] for line in start_configuration]))
stack_7 = re.findall(pattern=r'[A-Z]', string=','.join([line[24:27] for line in start_configuration]))
stack_8 = re.findall(pattern=r'[A-Z]', string=','.join([line[28:31] for line in start_configuration]))
stack_9 = re.findall(pattern=r'[A-Z]', string=','.join([line[32:35] for line in start_configuration]))

stacks = [stack_1,stack_2,stack_3,stack_4,stack_5,stack_6,stack_7,stack_8,stack_9]
stacks = [deque(stack) for stack in stacks]

instructions = [re.findall(pattern=r'\d+', string=line) for line in lines[10:]]
instructions = [[int(item) for item in sublist] for sublist in instructions]

# Part one
def move_container(stacks: list[deque[str]], instructions: list[int]):
    number_of_crates = instructions[0]
    source_stack = instructions[1] - 1
    target_stack = instructions[2] -1

    tmp_stack = []

    for number in range(number_of_crates):
        tmp_stack.append(stacks[source_stack].popleft())

    stacks[target_stack].extendleft(tmp_stack)

    return stacks

part_one_stacks = copy.deepcopy(stacks)
for instruction in instructions:
    move_container(part_one_stacks, instructions=instruction)

solution_1 = ''.join([stack.popleft() for stack in part_one_stacks])
print(f'{solution_1 = }')

# Part two
def move_container_2(stacks: list[deque[str]], instructions: list[int]):
    number_of_crates = instructions[0]
    source_stack = instructions[1] - 1
    target_stack = instructions[2] -1

    tmp_stack = deque([])

    for number in range(number_of_crates):
        tmp_stack.extendleft(stacks[source_stack].popleft())

    stacks[target_stack].extendleft(tmp_stack)

    return stacks

part_two_stacks = copy.deepcopy(stacks)
for instruction in instructions:
    move_container_2(part_two_stacks, instructions=instruction)

solution_2 = ''.join([stack.popleft() for stack in part_two_stacks])
print(f'{solution_2 = }')
