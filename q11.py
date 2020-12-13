from typing import Tuple

input_file = open("q11_example.txt", "r")

orig_state = []
for line in input_file:
    line = line.strip()
    row = [l for l in line]
    orig_state.append(row)

MAX_R = len(orig_state)
MAX_C = len(orig_state[0])


def mutate(r: int, c: int) -> Tuple[str, bool]:
    if old_state[r][c] == ".":
        return (".", False)

    modifiers = [1, 0, -1]
    occupied = 0
    for i in modifiers:
        for j in modifiers:
            if i == 0 and j == 0:
                continue

            new_r = r + i
            new_c = c + j
            if new_r < 0 or new_c < 0 or new_r >= MAX_R or new_c >= MAX_C:
                continue

            if old_state[new_r][new_c] == "#":
                occupied += 1

    if old_state[r][c] == "L" and occupied == 0:
        return ("#", True)

    if old_state[r][c] == "#" and occupied >= 4:
        return ("L", True)

    return (old_state[r][c], False)


def pprint(state):
    for row in state:
        print("".join(row))


old_state = orig_state
new_state = []
count = 0
while True:
    changed_state = False
    count += 1
    for r in range(MAX_R):
        row = []
        for c in range(MAX_C):
            value, changed = mutate(r, c)
            row.append(value)
            changed_state = changed_state or changed

        new_state.append(row)

    if not changed_state:
        old_state = new_state
        break

    old_state = new_state
    new_state = []

seats = 0
for row in old_state:
    for seat in row:
        seats += 1 if seat == "#" else 0

print("PART 1", seats)


def mutate_look(r: int, c: int) -> Tuple[str, bool]:
    if old_state[r][c] == ".":
        return (".", False)

    modifiers = [1, 0, -1]
    occupied = 0
    for i in modifiers:
        for j in modifiers:
            if i == 0 and j == 0:
                continue

            new_r = r + i
            new_c = c + j

            found = False
            while not found:
                if new_r < 0 or new_c < 0 or new_r >= MAX_R or new_c >= MAX_C:
                    found = True
                    continue

                point = old_state[new_r][new_c]
                if point == "#":
                    occupied += 1
                    found = True
                elif point == "L":
                    found = True

                new_r = new_r + i
                new_c = new_c + j

    if old_state[r][c] == "L" and occupied == 0:
        return ("#", True)

    if old_state[r][c] == "#" and occupied >= 5:
        return ("L", True)

    return (old_state[r][c], False)


old_state = orig_state
new_state = []
count = 0
while True:
    changed_state = False
    count += 1
    for r in range(MAX_R):
        row = []
        for c in range(MAX_C):
            value, changed = mutate_look(r, c)
            row.append(value)
            changed_state = changed_state or changed

        new_state.append(row)

    if not changed_state:
        old_state = new_state
        break

    old_state = new_state
    new_state = []

seats = 0
for row in old_state:
    for seat in row:
        seats += 1 if seat == "#" else 0

print("PART 2", seats)
