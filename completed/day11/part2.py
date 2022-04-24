def find_seats(seats, row, col):
    row_length = len(seats)
    col_length = len(seats[0])
    neighbour_seats = []

    # top
    if row > 0:
        for i in range(row - 1, 0 - 1, -1):
            if seats[i][col] != '.':
                neighbour_seats.append(seats[i][col])
                break
    
    # bottom
    if row < row_length - 1:
        for i in range(row + 1, row_length, +1):
            if seats[i][col] != '.':
                neighbour_seats.append(seats[i][col])
                break

    # right
    if col < col_length - 1:
        for i in range(col + 1, col_length, +1):
            if seats[row][i] != '.':
                neighbour_seats.append(seats[row][i])
                break
    
    # left
    if col > 0:
        for i in range(col - 1, 0 - 1, -1):
            if seats[row][i] != '.':
                neighbour_seats.append(seats[row][i])
                break

    # top right
    i = 1
    while row - i >= 0 and col + i <= col_length - 1:
        if seats[row - i][col + i] != '.':
            neighbour_seats.append(seats[row - i][col + i])
            break
        i += 1

    # bottom right
    i = 1
    while row + i <= row_length - 1 and col + i <= col_length - 1:
        if seats[row + i][col + i] != '.':
            neighbour_seats.append(seats[row + i][col + i])
            break
        i += 1

    # top left
    i = 1
    while row - i >= 0 and col - i >= 0:
        if seats[row - i][col - i] != '.':
            neighbour_seats.append(seats[row - i][col - i])
            break
        i += 1

    # bottom left
    i = 1
    while row + i <= row_length - 1 and col - i >= 0:
        if seats[row + i][col - i] != '.':
            neighbour_seats.append(seats[row + i][col - i])
            break
        i += 1

    return neighbour_seats
