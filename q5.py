input_file = open('q5.txt', 'r')


def to_int(val: str, one: str) -> int:
    total = 0
    exp = 0
    for v in reversed(val):
        total += 2 ** exp if v == one else 0
        exp += 1

    return total


seats = []
for line in input_file:
    line = line.strip()
    row = line[:7]
    row_num = to_int(row, "B")
    seat = line[7:]
    seat_num = to_int(seat, "R")
    seat_id = (row_num * 8) + seat_num
    seats.append(seat_id)


sorted_seats = sorted(seats)
prev = sorted_seats[0]
for sid in sorted_seats[1:]:
    if sid - prev > 1:
        print("MISSING", sid - 1)
        break
    prev = sid
