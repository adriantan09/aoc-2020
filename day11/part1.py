def part1(seats):
    old_total = count_occupied_seats(seats)
    new_seats = occupy_seats(seats)
    new_total = count_occupied_seats(new_seats)

    if new_total - old_total == 0:
        return new_total

    return part1(new_seats)

def find_adjacent_seats(seats, row, col):
    adjacent_seats = []
    for y in range(-1, 2):
        for x in range(-1, 2):
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

def occupy_seats(seats):
    new_seats = [row[:] for row in seats]
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            adjacent_seats = find_adjacent_seats(seats, row, col)
            if seats[row][col] == 'L' and '#' not in adjacent_seats:
                new_seats[row][col] = '#'
            elif seats[row][col] == '#' and adjacent_seats.count('#') >= 4:
                new_seats[row][col] = 'L'
    return new_seats

def count_occupied_seats(seats):
    total = 0
    for row in seats:
        total += row.count('#')
    return total
