from __future__ import annotations

from typing import List


class Tile:
    def __init__(self, tid: int, lines: List[str]) -> None:
        self.tid = tid
        left, right = "", ""
        for line in lines:
            left += line[0]
            right += line[-1]

        self.ordered = [lines[0], right, lines[-1], left]
        self.sides = set(self.ordered)

    def matches(self, others: List[Tile]) -> int:
        count = 4
        for side in self.sides:
            for other in others:
                if other.tid == self.tid:
                    continue

                if side in other.sides:
                    count -= 1
                    break

        return count


tiles = []
current_data = []
current_tid = None
for line in open("q20_example.txt", "r"):
    line = line.strip()
    if line.startswith("Tile"):
        current_tid = int(line.strip("Tile ").strip(":"))
        continue
    elif line == "":
        tiles.append(Tile(current_tid, current_data))
        current_tid = None
        current_data = []
    else:
        current_data.append(line)

print("TILES", tiles)

corners = []
for tile in tiles:
    if tile.matches(tiles) == 2:
        corners.append(tile)

print("CORNERS", [c.tid for c in corners])