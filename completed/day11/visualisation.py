import time

class colour:
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'

def visualisation(seats):
    for i in range(len(seats)):
        seat_row = ''
        for j in range(len(seats[0])):
            if seats[i][j] == '#':
                seats[i][j] = colour.OKBLUE + '#' + colour.ENDC
            seat_row += seats[i][j]
        print(seat_row)
    print()
    time.sleep(0.18)
