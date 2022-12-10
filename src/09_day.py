"""
https://adventofcode.com/2022/day/9
"""

from aoc2022_utils import read_input_file

# Input Processing
raw_input = read_input_file('09')
lines = raw_input.splitlines()

test_input="""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

t_moves = [command.split(' ') for command in test_input.splitlines()]
t_moves = [[pair[0], int(pair[1])] for pair in t_moves]


def make_move(move: list[str, int], start_point : list[int, int] = None, flg_tail=False) -> int:

    direction = move[0]
    steps = move[1]

    if start_point is None:
        start_point = [0,0]

    if flg_tail:
        steps -= 1

    end_point = start_point

    print(f'{direction = } {steps = }')
    if direction == 'R':
        while steps > 0:
            end_point[0] += 1
            steps -= 1

    elif direction == 'L':
        while steps > 0:
            end_point[0] -= 1
            steps -= 1
    elif direction == 'U':
        while steps > 0:
            end_point[1] += 1
            steps -= 1
    elif direction == 'D':
        while steps > 0:
            end_point[1] -= 1
            steps -= 1
    return end_point

H = [0,0]
T = [0,0]

for move in t_moves:
    H = make_move(move=move, start_point=H)
    print(f'{H = }')

    if H[0] - T[0] > 1 or H[1] - T[1] > 1:
        T = make_move(move=move, start_point=T, flg_tail=True)
    print(f'{T = }')
