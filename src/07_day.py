"""
https://adventofcode.com/2022/day/7
"""

from aoc2022_utils import read_input_file

# Input Processing
raw_input = read_input_file('07')

lines = raw_input.splitlines()

commands = [line.split(' ') for line in lines]

tree=dict()
directories = []

for command in commands[:15]:
    # print(command, '\n')
    if command[0] == '$':

        if command[1] == 'cd' and command[2] != '..':
            tree[command[2]] = dict()
            directories.append(command[2])
            print(f'Change directory to `{command[2]}` - pwd: `{directories[-1]}`')
            # print(f'Current directory: {directories[-1]}', '\n')

        elif command[1] == 'cd' and command[2] == '..':
            directories.pop()
            print(f'Change back to directory `{directories[-1]}`')
            print(f'Current directory: {directories[-1]}')

        elif command[1] == 'ls':
            print(f'List content of directory `{directories[-1]}`:')

    elif (re.findall(r'[a-z]', string=command[0])):
        tree[directories[-1]] = directories[-1]
        print(f'{command[1]}')

    elif (re.findall(r'\d', string=command[0])):
        print(f'{command[1]} \t {command[0]}')

print(tree)
