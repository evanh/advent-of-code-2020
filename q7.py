from typing import NamedTuple, Sequence


class Bag(NamedTuple):
    count: int
    colour: str


input_file = open("q7.txt", "r")


def parse_bag(bag: str) -> str:
    colour = bag.replace("bags", "").replace("bag", "").strip()
    return colour


def parse_match(match: str) -> Sequence[Bag]:
    match = match.strip()[:-1]
    if match.strip() == "no other bags":
        return []

    bags = match.split(",")
    matches: Sequence[Bag] = []
    for bag in bags:
        count, rest = bag.strip().split(" ", 1)
        colour = parse_bag(rest)
        matches.append(Bag(int(count), colour))

    return matches


rules = {}
for line in input_file:
    lhs, rhs = line.split("contain", 1)
    colour = parse_bag(lhs)
    bags = parse_match(rhs)
    rules[colour] = bags


def contains_gold(colour: str) -> bool:
    if colour == "shiny gold":
        return False
    elif len(rules[colour]) == 0:
        return False

    matches = rules[colour]
    for match in matches:
        if match.colour == "shiny gold":
            return True

    for match in matches:
        if contains_gold(match.colour):
            return True

    return False


total = 0
for colour in rules:
    if contains_gold(colour):
        total += 1

print("TOTAL", total)


def count_bags(colour: str) -> int:
    if len(rules[colour]) == 0:
        return 1

    total = 1
    for bag in rules[colour]:
        total += bag.count * count_bags(bag.colour)

    return total


count = count_bags("shiny gold")
print("COUNT", count-1)
