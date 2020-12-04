from typing import Callable, Mapping, Optional

input_file = open("q4.txt", "r")

numbers = set("0123456789")
hex_numbers = numbers | set("abcdef")
ecls = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])


def num_validator(count: int, minn: Optional[int], maxn: Optional[int]) -> Callable[[str], bool]:
    def validator(field: str) -> bool:
        if len(field) != count:
            return False

        if len(set(field) - numbers) != 0:
            return False

        if minn is not None and int(field) < minn:
            return False

        if maxn is not None and int(field) > maxn:
            return False

        return True

    return validator


def height_validator(height: str) -> bool:
    """
    (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    if height.endswith("cm"):
        return num_validator(3, 150, 193)(height[:-2])
    elif height.endswith("in"):
        return num_validator(2, 59, 76)(height[:-2])
    else:
        return False


validators = {
    "byr": num_validator(4, 1920, 2002),  # (Birth Year) - four digits; at least 1920 and at most 2002.
    "iyr": num_validator(4, 2010, 2020),  # (Issue Year) - four digits; at least 2010 and at most 2020.
    "eyr": num_validator(4, 2020, 2030),  # (Expiration Year) - four digits; at least 2020 and at most 2030.
    "hgt": height_validator,
    "hcl": lambda x: len(x) == 7 and x[0] == "#" and len(set(x[1:]) - hex_numbers) == 0,  # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    "ecl": lambda x: x in ecls,
    "pid": num_validator(9, None, None),  # (Passport ID) - a nine-digit number, including leading zeroes.
}


def check_valid(p: Mapping[str, str]) -> bool:
    if len(passport) < 7:
        return False

    for key, value in p.items():
        if not validators[key](value):
            return False

    return True


valid_passports = 0
passport = {}
for line in input_file:
    line = line.strip()
    if line == "":
        if check_valid(passport):
            valid_passports += 1
        passport = {}
        continue

    fields = line.split()
    for field in fields:
        key, value = field.split(":", 1)
        if key != "cid":
            passport[key] = value

if check_valid(passport):
    valid_passports += 1

print("VALID", valid_passports)
