def function1(departure_time, bus_ids):
    wait_times = [id - (departure_time % id) for id in bus_ids]
    shortest_wait = min(wait_times)
    earliest_bus = bus_ids[wait_times.index(shortest_wait)]
    return shortest_wait * earliest_bus
