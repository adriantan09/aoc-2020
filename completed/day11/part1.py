def find_adjacent_seats(seats, row, col):
    adjacent_seats = []
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            _x = col + x
            _y = row + y
            if is_adjacent(seats, _y, _x) and not (x == 0 and y == 0):
                adjacent_seats.append(seats[_y][_x])
    return adjacent_seats

def is_adjacent(seats, row, col):
    return (
        (col >= 0 and col <= len(seats[0]) - 1) and
        (row >= 0 and row <= len(seats) - 1)
    )
