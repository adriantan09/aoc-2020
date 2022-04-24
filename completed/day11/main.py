import sys

from part1 import find_adjacent_seats
from part2 import find_seats

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')
seats = [list(l) for l in lines]

def fill_seats(seats, find_seats, seat_count):
    old_total = count_occupied_seats(seats)
    new_seats = occupy_seats(seats, find_seats, seat_count)
    new_total = count_occupied_seats(new_seats)
    
    # visualisation(seats)

    if new_total - old_total == 0:
        return new_total

    return fill_seats(new_seats, find_seats, seat_count)

def occupy_seats(seats, find_seats, seat_count):
    new_seats = [row[:] for row in seats]
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            neighbour_seats = find_seats(seats, row, col)
            if seats[row][col] == 'L' and '#' not in neighbour_seats:
                new_seats[row][col] = '#'
            elif seats[row][col] == '#' and neighbour_seats.count('#') >= seat_count:
                new_seats[row][col] = 'L'
    return new_seats

def count_occupied_seats(seats):
    total = 0
    for row in seats:
        total += row.count('#')
    return total

print('part 1:', fill_seats(seats, find_adjacent_seats, 4))
print('part 2:', fill_seats(seats, find_seats, 5))
