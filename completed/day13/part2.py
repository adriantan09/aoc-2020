# 1st attempt
# Brute force -> max recursion depth exceeded
# def function2(curr_departure_time, bus_ids):
#     if ids_match_departure_mins(curr_departure_time, bus_ids):
#         return curr_departure_time
#     return function2(curr_departure_time + 1, bus_ids)

# 2nd attempt 
# Brute force -> too slow
# def function2(bus_ids):
#     i = 0
#     while not ids_match_departure_mins(i, bus_ids): i += 1
#     return i

# Helper for 1st and 2nd attempt
# def ids_match_departure_mins(curr_departure_time, bus_ids):
#     for i, id in enumerate(bus_ids):
#         if id.isdigit():
#             wait_time = int(id) - (curr_departure_time % int(id))
#             if wait_time == int(id): wait_time = 0
#             if wait_time != i:
#                 return False
#     return True

# 3rd attempt
# Realise that all of the provided bus ids are prime numbers
# Multiplying prime numbers together will provide the lcm for them
def function2(bus_ids):
    curr_depart_time = 0
    step_size = int(bus_ids[0])
    for i in range(1, len(bus_ids)):
        id = bus_ids[i]
        if id.isdigit():
            next_depart_time = curr_depart_time + i
            while next_depart_time % int(id) != 0:
                curr_depart_time += step_size
                next_depart_time = curr_depart_time + i
            step_size *= int(id)
    return curr_depart_time
