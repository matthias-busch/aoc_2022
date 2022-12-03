"""
https://adventofcode.com/2022/day/2
"""

with open(rf'../inputs/02_input.txt', encoding='utf-8') as fh:
    raw_input = fh.read()

games = [game.split(' ') for game in raw_input.splitlines()]

def calc_winner(game):
    # Rock - Paper - Scissor
    points = {'X': 1, 'Y': 2, 'Z': 3}

    if game[0] == 'A' and game[1] == 'X':
        return points['X'] + 3
    elif game[0] == 'A' and game[1] == 'Y':
        return points['Y'] + 6
    elif game[0] == 'A' and game[1] == 'Z':
        return points['Z']
    elif game[0] == 'B' and game[1] == 'X':
        return points['X']
    elif game[0] == 'B' and game[1] == 'Y':
        return points['Y'] + 3
    elif game[0] == 'B' and game[1] == 'Z':
        return points['Z'] + 6
    elif game[0] == 'C' and game[1] == 'X':
        return points['X'] + 6
    elif game[0] == 'C' and game[1] == 'Y':
        return points['Y']
    elif game[0] == 'C' and game[1] == 'Z':
        return points['Z'] + 3


def calc_winner_with_strategy(game):
    # Rock - Paper - Scissor
    points = {'A': 1, 'B': 2, 'C': 3}

    if game[0] == 'A' and game[1] == 'X': # LOSE
        return points['C']
    elif game[0] == 'A' and game[1] == 'Y': # DRAW
        return points['A'] + 3
    elif game[0] == 'A' and game[1] == 'Z': # WIN
        return points['B'] + 6
    elif game[0] == 'B' and game[1] == 'X':
        return points['A']
    elif game[0] == 'B' and game[1] == 'Y':
        return points['B'] + 3
    elif game[0] == 'B' and game[1] == 'Z':
        return points['C'] + 6
    elif game[0] == 'C' and game[1] == 'X':
        return points['B']
    elif game[0] == 'C' and game[1] == 'Y':
        return points['C'] + 3
    elif game[0] == 'C' and game[1] == 'Z':
        return points['A'] + 6

# Results
solution_1 = sum([calc_winner(game) for game in games])
print(f'{solution_1 = }')

solution_2 = sum([calc_winner_with_strategy(game) for game in games])
print(f'{solution_2 = }')
