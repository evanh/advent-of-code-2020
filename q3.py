input_file = open("q3.txt", "r")

slopes = {
    (1, 1): 0,
    (1, 3): 0,
    (1, 5): 0,
    (1, 7): 0,
    (2, 0.5): 0,
}

i = row_size = 0
for line in input_file:
    line = line.strip()
    if row_size == 0:
        row_size = len(line)

    print(line)
    for slope in slopes:
        down, right = slope
        if i % down != 0:
            print("." * row_size)
            continue

        y_coord = int(right * i)
        y_coord = y_coord % row_size
        if line[y_coord] == "#":
            slopes[slope] += 1

        x = "." * row_size
        print(f"{x[:y_coord]}!{x[y_coord+1:]}")

    i += 1

total = 1
for slope in slopes:
    print(f"HITS {slope} Tree: {slopes[slope]}")
    total *= slopes[slope]

print("TOTAL", total)