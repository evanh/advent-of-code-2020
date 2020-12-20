from typing import NamedTuple, Set

lines = [line.strip() for line in open("q16.txt", "r")]


class Interval(NamedTuple):
    lower: int
    high: int

    def contains(self, x: int) -> bool:
        return x <= self.high and x >= self.lower


rules = {}
parse_my_ticket = False
my_ticket = []
parse_nearby = False
nearby = []
for line in lines:
    if line == "your ticket:":
        parse_my_ticket = True
        continue
    elif parse_my_ticket:
        my_ticket = [int(x) for x in line.split(",")]
        parse_my_ticket = False
        continue
    elif line == "nearby tickets:":
        parse_nearby = True
        continue
    elif parse_nearby:
        nearby.append([int(x) for x in line.split(",")])
        continue
    elif line != "":
        rule, value = line.split(":", 1)
        range1, range2 = value.split(" or ", 1)
        x, y = range1.split("-", 1)
        lhs = Interval(int(x), int(y))
        x, y = range2.split("-", 1)
        rhs = Interval(int(x), int(y))

        rules[rule] = (lhs, rhs)

invalid = 0
for near in nearby:
    for val in near:
        valid = False
        for _, intervals in rules.items():
            valid = intervals[0].contains(val) or intervals[1].contains(val)
            if valid:
                break

        if valid:
            continue

        invalid += val

print("Part 1", invalid)

valid_tickets = []
for near in nearby:
    invalid_ticket = False
    for val in near:
        valid = False
        for _, intervals in rules.items():
            valid = intervals[0].contains(val) or intervals[1].contains(val)
            if valid:
                break

        if valid:
            continue
        else:
            invalid_ticket = True
            break

    if invalid_ticket:
        continue
    else:
        valid_tickets.append(near)


def find_matching_rules(idx):
    possibles = set(r for r in rules)
    for ticket in valid_tickets:
        to_check = ticket[idx]
        to_remove = []
        for rule in possibles:
            lhs, rhs = rules[rule]
            if not lhs.contains(to_check) and not rhs.contains(to_check):
                to_remove.append(rule)

        for rule in to_remove:
            possibles.remove(rule)

        if len(possibles) == 1:
            break

    return possibles


# For each position, find the set of possible rules
rule_positions = []
for idx in range(len(my_ticket)):
    rule_positions.append(find_matching_rules(idx))


found: Set[str] = set()
ordered = [-1] * len(rule_positions)
while len(found) < len(ordered):

    for i, possibles in enumerate(rule_positions):
        if len(possibles) == 1:
            rule = possibles.pop()
            ordered[i] = rule
            found.add(rule)

    for i, possibles in enumerate(rule_positions):
        rule_positions[i] -= found

departures = 1
for i, rule in enumerate(ordered):
    if rule.startswith("departure"):
        departures *= my_ticket[i]

print("Part 2", departures)
