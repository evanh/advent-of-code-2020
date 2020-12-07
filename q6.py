from typing import Sequence, Set

input_file = open("q6.txt", "r")


def get_len(g: Sequence[Set[str]]) -> int:
    if len(g) < 1:
        return 0
    elif len(g) == 1:
        return len(g[0])
    else:
        intersect = g[0].intersection(*g[1:])
        return len(intersect)


group = []
total = 0
for line in input_file:
    line = line.strip()
    if line == "":
        total += get_len(group)
        group = []
        continue

    group.append(set(line))

total += get_len(group)
print(total)
