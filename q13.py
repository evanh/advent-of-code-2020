input_file = open("q13.txt")

timestamp = None
bus_ids = None
for line in input_file:
    line = line.strip()
    if timestamp is None:
        timestamp = int(line)
        continue

    raw_bus_ids = line.strip()

bus_ids = [int(bus) for bus in raw_bus_ids.split(",") if bus != "x"]
earliest = None
earliest_bus_id = None
for bus_id in bus_ids:
    mult = int(timestamp / bus_id)
    next_time = (mult + 1) * bus_id
    if earliest is None or next_time < earliest:
        earliest = next_time
        earliest_bus_id = bus_id

solution = (earliest - timestamp) * earliest_bus_id
print(f"ID: {earliest_bus_id} at {earliest}: {earliest - timestamp} * {earliest_bus_id} = {solution}")
