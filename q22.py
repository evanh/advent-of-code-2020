from typing import List

# deck1 = [9, 2, 6, 3, 1]
# deck2 = [5, 8, 4, 7, 10]

deck1 = [14, 23, 6, 16, 46, 24, 13, 25, 17, 4, 31, 7, 1, 47, 15, 9, 50, 3, 30, 37, 43, 10, 28, 33, 32]
deck2 = [29, 49, 11, 42, 35, 18, 39, 40, 36, 19, 48, 22, 2, 20, 26, 8, 12, 44, 45, 21, 38, 41, 34, 5, 27]

p1 = deck1.copy()
p2 = deck2.copy()
while len(p1) > 0 and len(p2) > 0:
    card1, card2 = p1.pop(0), p2.pop(0)

    if card1 > card2:
        p1.extend([card1, card2])
    elif card2 > card1:
        p2.extend([card2, card1])

winner = p1 if len(p1) > 0 else p2
count = 0
for i, value in enumerate(reversed(winner)):
    count += (i+1) * value

print("PART 1", count)


def hash(p1: List[int], p2: List[int]) -> str:
    return f"{'.'.join([str(p) for p in p1])}|{'.'.join([str(p) for p in p2])}"


def game(p1: List[int], p2: List[int]) -> int:
    seen_before = set()
    while len(p1) > 0 and len(p2) > 0:
        hashed = hash(p1, p2)
        if hashed in seen_before:
            return 1

        seen_before.add(hashed)

        card1, card2 = p1.pop(0), p2.pop(0)
        if len(p1) >= card1 and len(p2) >= card2:
            winner = game(p1[:card1], p2[:card2])
            if winner == 1:
                p1.extend([card1, card2])
            else:
                p2.extend([card2, card1])

            continue

        if card1 > card2:
            p1.extend([card1, card2])
        elif card2 > card1:
            p2.extend([card2, card1])

    return 1 if len(p1) > 0 else 2


p1 = deck1.copy()
p2 = deck2.copy()
game(p1, p2)
winner = p1 if len(p1) > 0 else p2
count = 0
for i, value in enumerate(reversed(winner)):
    count += (i+1) * value

print("PART 2", count)
