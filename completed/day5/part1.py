def find_max_seat_id(boarding_passes):
    
    max_seat_id = 0
    for boarding_pass in boarding_passes:
        row = calc_row(boarding_pass)
        col = calc_col(boarding_pass)
        seat_id = calc_seat_id(row, col)
        if (seat_id > max_seat_id):
            max_seat_id = seat_id

    return max_seat_id

def calc_row(boarding_pass):
    
    lower = 0
    row_range = upper = 127

    for i in range(0,7):
        row_range = round(row_range / 2)
        if boarding_pass[i] == 'F':
            upper -= round(row_range)
        else: # letter == 'B'
            lower += round(row_range)

    return lower or upper

def calc_col(boarding_pass):

    lower = 0
    col_range = upper = 7

    for i in range(7,10):
        col_range = round(col_range / 2)
        if boarding_pass[i] == 'L':
            upper -= round(col_range)
        else: # letter == 'R'
            lower += round(col_range)

    return lower or upper

def calc_seat_id(row, col):
    return (row * 8) + col