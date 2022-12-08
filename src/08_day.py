"""
https://adventofcode.com/2022/day/8
"""

from aoc2022_utils import read_input_file

# Input Processing
raw_input = read_input_file('08')

lines = raw_input.splitlines()

test_input="""30373
25512
65332
33549
35390
"""

test_lines = test_input.splitlines()


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


# Results
solution_1 = count_visible_trees(tree_map=lines)
print(f'{solution_1 = }')



