from part1 import calc_row, calc_col, calc_seat_id

def find_seat_id(boarding_passes):
    
    seat_ids = []
    for boarding_pass in boarding_passes:
        row = calc_row(boarding_pass)
        col = calc_col(boarding_pass)
        seat_id = calc_seat_id(row, col)
        seat_ids.append(seat_id)

    seat_ids.sort()

    for i in range(len(seat_ids) - 1):
        if (seat_ids[i + 1] - seat_ids[i] != 1):
            return seat_ids[i] + 1

    return 0