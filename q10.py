input_file = open("q10.txt", "r")

adapters = []
for line in input_file:
    adapters.append(int(line.strip()))

adapters = sorted(adapters, reverse=True)
adapters = [adapters[0] + 3, *adapters, 0]
diffs = {}
prev = adapters[0]
for adapter in adapters[1:]:
    diff = prev - adapter
    diffs[diff] = diffs.get(diff, 0) + 1
    prev = adapter

print("DIFF", diffs)
print("MULT", diffs[1] * diffs[3])

# All credit for this solution to pt 2 goes to Zylphrex, I was completely stuck

ways = [1]
for i in range(1, len(adapters)):
    way = 0
    for j in range(1, 4):
        if i - j < 0:
            break

        if adapters[i-j] - adapters[i] <= 3:
            way += ways[i-j]

    ways.append(way)

print("WAYS", ways[-1])
