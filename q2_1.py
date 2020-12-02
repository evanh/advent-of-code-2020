import re

data = []

input_file = open("q2_1.txt", "r")

matcher = re.compile("(\d+)-(\d+) (\w): (.*)")
lines = []
for line in input_file:
    match = matcher.search(line)
    minn, maxn, char, password = match.groups()
    lines.append([int(minn), int(maxn), char, password])

valid = 0
for line in lines:
    minn, maxn, char, password = line
    count = 0
    for p in password:
        if p == char:
            count += 1

        if count > maxn:
            break

    if count >= minn and count <= maxn:
        valid += 1

print("VALID pt 1", valid)

valid = 0
for line in lines:
    minn, maxn, char, password = line
    if len(password) < maxn:
        continue

    tests = [password[minn-1] == char, password[maxn-1] == char]
    if sum(tests) == 1:
        valid += 1

print("VALID pt 2", valid)