from typing import List, Tuple

input_file = open("q14.txt", "r")
lines = [line.strip() for line in input_file]


def build_mask(mask: str) -> Tuple[int, int]:
    or_arr = ["0"] * len(mask)  # n or 0 = n
    an_arr = ["1"] * len(mask)  # n and 1 = n
    count = 0
    for i, c in enumerate(mask):
        if c == "X":
            count += 1
            continue
        elif c == "1":
            or_arr[i] = "1"  # n or 1 = 1
        elif c == "0":
            an_arr[i] = "0"  # n and 0 = 0

    or_mask = int("".join(or_arr), 2)
    and_mask = int("".join(an_arr), 2)
    return (or_mask, and_mask)


memory = {}
or_mask, and_mask = -1, -1
for line in lines:
    command, value = line.split(" = ", 1)
    if command == "mask":
        or_mask, and_mask = build_mask(value)
        continue

    masked = int(value) & and_mask
    masked = masked | or_mask

    _, raw_num = command.split("[", 1)
    num = int(raw_num[:-1])
    memory[num] = masked

print("PART 1 SUM", sum(memory.values()))


def build_floating(indexes: List[int], existing: List[int] = None) -> List[int]:
    if existing is None:
        existing = []

    if len(indexes) == 0:
        return existing

    if len(existing) == 0:
        existing.append(0)

    num_mask = 1 << indexes[0]
    new = []
    for prev in existing:
        new.append(prev ^ num_mask)

    existing += new
    return build_floating(indexes[1:], existing)


def build_mask(mask: str) -> Tuple[int, int]:
    or_arr = ["0"] * len(mask)  # n or 0 = n
    float_idx = []
    for i, c in enumerate(mask):
        if c == "X":
            float_idx.append(len(mask) - i - 1)
        elif c == "1":
            or_arr[i] = "1"  # n or 1 = 1

    mask = int("".join(or_arr), 2)
    floaters = build_floating(float_idx)
    return (mask, floaters)


def apply_mask(mask: int, floaters: List[int], address: int) -> List[int]:
    new_address = address | mask
    addresses = []
    for floater in floaters:
        addresses.append(new_address ^ floater)
    return addresses


memory = {}
mask = -1
floaters = []
for line in lines:
    command, value = line.split(" = ", 1)
    if command == "mask":
        floaters = []
        mask, floaters = build_mask(value)
        continue

    _, raw_addr = command.split("[", 1)
    address = int(raw_addr[:-1])
    possibles = apply_mask(mask, floaters, address)
    for possible in possibles:
        memory[possible] = int(value)

print("PART 2 SUM", sum(memory.values()))
