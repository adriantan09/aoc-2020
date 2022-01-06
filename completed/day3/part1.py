# Time complexity: O(n)
# where n is the number of lines in the input file
def count_trees(data, row_increment, col_increment):
    row, col, n_trees = (0,) * 3
    while row < len(data):
        if (data[row][col % len(data[0])] == '#'):
            n_trees += 1
        row += row_increment
        col += col_increment
    
    return n_trees