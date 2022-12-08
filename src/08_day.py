"""
https://adventofcode.com/2022/day/8
"""

from aoc2022_utils import read_input_file

# Input Processing
raw_input = read_input_file('08')

lines = raw_input.splitlines()

def count_visible_trees(tree_map: list[list[int]]) -> int:

    visible_trees = []

    for i in range(len(tree_map)):
        for j in range(len(tree_map[i])):

            row = i
            column = j

            # check grid rows
            if (row == 0) or (row == len(tree_map) - 1):
                visible_trees.append((row, column))

            # check grid cols
            elif (column == 0) or (column == len(tree_map[i]) - 1 ):
                visible_trees.append((row, column))

            # check row left / right
            elif ( tree_map[i][j] > max(tree_map[i][:j]) ) or ( tree_map[i][j] > max(tree_map[i][j+1:]) ):
                visible_trees.append((row, column))

            # check column up / down
            elif ( tree_map[i][j] > max( [row[j] for row in tree_map[:i]] ) ) or ( tree_map[i][j] > max( [row[j] for row in tree_map[i+1:]] ) ):
                visible_trees.append((row, column))

    return len(visible_trees)


def compute_scenic_score(x: int, y: int, tree_map: list[list[int]]) -> dict[int]:
    left_distance : int = 0
    right_distance : int = 0
    up_distance : int = 0
    down_distance : int = 0
    # print(f'{x = } {y = } {tree_map[x][y] = }')

    # check top border
    if x == 0:
        up_distance += 0

    # check bottom border
    elif x == len(tree_map) - 1:
        down_distance += 0

    # check left border
    elif y == 0:
        left_distance += 0

    # check right border
    elif y == len(tree_map[x]) - 1:
        right_distance += 0

    # check inner trees
    else:
        # check left
        left = tree_map[x][:y]
        for tree in reversed(left):
            if tree_map[x][y] > tree:
                left_distance += 1
            elif tree_map[x][y] == tree:
                left_distance += 1
                break
            else:
                left_distance += 0
                break

        # check right
        right = tree_map[x][y+1:]
        for tree in right:
            if tree_map[x][y] > tree:
                right_distance += 1
            elif tree_map[x][y] == tree:
                right_distance += 0
                break
            else:
                right_distance += 1
                break

        # check up
        up = [row[y] for row in tree_map[:x]]
        for tree in reversed(up):
            if tree_map[x][y] > tree:
                up_distance += 1
            elif tree_map[x][y] == tree:
                up_distance += 1
                break
            else:
                up_distance += 0
                break

        # check down
        down = [row[y] for row in tree_map[x+1:]]
        for tree in down:
            if tree_map[x][y] > tree:
                down_distance += 1
            elif tree_map[x][y] == tree:
                down_distance += 1
                break
            else:
                down_distance += 0
                break
    # print(f'{left_distance = } {right_distance = } {up_distance = } {down_distance = }')
    scenic_score = left_distance * right_distance * up_distance * down_distance

    return scenic_score

scenic_scores = []
for x in range(len(lines)):
        for y in range(len(lines[x])):
            scenic_scores.append(compute_scenic_score(x=x, y=y, tree_map=lines))


# Results
solution_1 = count_visible_trees(tree_map=lines)
print(f'{solution_1 = }')

solution_2 = max(scenic_scores)
print(f'{solution_2 = }')


