from typing import List

input_file = open("q12.txt", "r")
commands = [line.strip() for line in input_file]
POLES = ["N", "E", "S", "W"]


class Ship:
    ship_direction: int = 1
    ship_location: List[int] = [0, 0]

    def rotate(self, direction: str, degrees: int) -> None:
        modifier = 1
        if direction == "L":
            modifier = -1

        rotation = (degrees % 360) / 90
        i = 0
        while i != rotation:
            self.ship_direction += modifier
            i += 1

        self.ship_direction = self.ship_direction % 4

    def move(self, direction: str, count: int) -> None:
        index, modifier = 0, 0
        if direction == "N":
            index, modifier = 1, 1
        elif direction == "E":
            index, modifier = 0, 1
        elif direction == "S":
            index, modifier = 1, -1
        elif direction == "W":
            index, modifier = 0, -1

        self.ship_location[index] += modifier * count

    def forward(self, value: int) -> None:
        direction = POLES[self.ship_direction]
        self.move(direction, value)

    def __repr__(self) -> str:
        return f"D: {POLES[self.ship_direction]} L: {self.ship_location}"


ship = Ship()
for line in commands:
    command = line[0]
    value = int(line[1:])
    if command in ("R", "L"):
        ship.rotate(command, value)
    elif command == "F":
        ship.forward(value)
    else:
        ship.move(command, value)


print("SHIP", ship)
print("MANS", abs(ship.ship_location[0]) + abs(ship.ship_location[1]))


class Ship2:
    waypoint: List[int] = [10, 1]
    location: List[int] = [0, 0]

    def _move(self, point: List[int], direction: str, count: int) -> None:
        index, modifier = 0, 0
        if direction == "N":
            index, modifier = 1, 1
        elif direction == "E":
            index, modifier = 0, 1
        elif direction == "S":
            index, modifier = 1, -1
        elif direction == "W":
            index, modifier = 0, -1

        point[index] += modifier * count

    def move(self, direction: str, count: int) -> None:
        self._move(self.waypoint, direction, count)

    def forward(self, value: int) -> None:
        east, north = self.waypoint[0] * value, self.waypoint[1] * value
        self._move(self.location, "E", east)
        self._move(self.location, "N", north)

    def rotate(self, direction: str, degrees: int) -> None:
        rotation = (degrees % 360)
        if rotation == 0:
            return

        m = -1 if direction == "R" else 1
        sinn, cosn = 0, 0
        if rotation == 90:
            sinn, cosn = m * 1, 0
        elif rotation == 180:
            sinn, cosn = 0, -1
        elif rotation == 270:
            sinn, cosn = m * -1, 0

        x, y = self.waypoint
        new_x = x * cosn - y * sinn
        new_y = y * cosn + x * sinn
        self.waypoint = [new_x, new_y]

    def __repr__(self) -> str:
        return f"W: {self.waypoint} L: {self.location}"


ship = Ship2()
for line in commands:
    command = line[0]
    value = int(line[1:])
    if command in ("R", "L"):
        ship.rotate(command, value)
    elif command == "F":
        ship.forward(value)
    else:
        ship.move(command, value)

print("SHIP", ship)
print("MANS", abs(ship.location[0]) + abs(ship.location[1]))
