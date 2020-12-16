from typing import List


def findN(puzzle: List[int], n: int) -> int:
    memory = {}
    spoken = -1
    for i in range(n):
        if i > 0 and i % 10000 == 0:
            print(f"SPOKEN {i} times, seen {len(memory)}")
        if i < len(puzzle):
            memory[puzzle[i]] = [i]
            spoken = puzzle[i]
            continue

        # Which number should be spoken?
        if len(memory[spoken]) == 1:
            spoken = 0
        else:
            turns = memory[spoken]
            spoken = turns[-1] - turns[0]

        # Update memory
        memory.setdefault(spoken, list()).append(i)
        memory[spoken] = memory[spoken][-2:]

    return spoken


inputs = [
    ([0, 3, 6], 436),
    ([1, 3, 2], 1),
    ([2, 1, 3], 10),
    ([1, 2, 3], 27),
    ([2, 3, 1], 78),
    ([3, 2, 1], 438),
    ([3, 1, 2], 1836),
]

for puzzle, expected in inputs:
    assert findN(puzzle, 2020) == expected, puzzle


my_puzzle = [16, 11, 15, 0, 1, 7]
print("Part 1", findN(my_puzzle, 2020))
print("Part 2", findN(my_puzzle, 30000000))
