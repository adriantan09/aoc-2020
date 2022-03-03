# Time complexity: O(n) where n is the number of directions
def find_manhattan_dist(directions):
    compass = {0: 0, 90: 0, 180: 0, 270: 0}
    curr_degrees = 90
    for d in directions:
        if d[0] == 'N': compass[0] += d[1]
        elif d[0] == 'E': compass[90] += d[1]
        elif d[0] == 'S': compass[180] += d[1]
        elif d[0] == 'W': compass[270] += d[1]
        elif d[0] == 'F': compass[curr_degrees % 360] += d[1]
        elif d[0] == 'L': curr_degrees -= d[1]
        elif d[0] == 'R': curr_degrees += d[1]

    return abs(compass[90] - compass[270]) + abs(compass[0] - compass[180])