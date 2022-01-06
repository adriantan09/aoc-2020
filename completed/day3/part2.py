from part1 import count_trees

# Time complexity: O(n * m)
# where n is the number of lines in the input file
# and m is the number of traversal instructions
def traverse_slope(data):
    traversals = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    tree_sum = 1
    for instruction in traversals:
        tree_sum *= count_trees(data, instruction[1], instruction[0])
    return tree_sum