from typing import Set

input_file = open("q9.txt", "r")


def check(nums: Set[int], val: int) -> bool:
    for num in nums:
        diff = val - num
        if diff != num and diff in nums:
            return True

    return False


LEN = 25
preamble_check = set()
preamble = []
all_nums = []
mismatch = None
for line in input_file:
    num = int(line.strip())
    all_nums.append(num)
    # seed preamble
    if len(preamble) < LEN:
        preamble.append(num)
        preamble_check.add(num)
        continue

    if not check(preamble_check, num):
        mismatch = num
        break

    preamble_check.remove(preamble[0])
    preamble_check.add(num)
    preamble.append(num)
    preamble = preamble[1:]

print("NO MATCH", mismatch)

# PART 2 #
total = 0
top = 0
bottom = 0
nums = []
for i, num in enumerate(all_nums):
    total += num
    nums.append(num)
    if total == mismatch:
        break
    elif total < mismatch:
        continue

    j = 0
    found = False
    while total > mismatch:
        total -= nums[j]
        j += 1
        if total == mismatch:
            nums = nums[j:]
            found = True
            break

    if found:
        break

    nums = nums[j:]

print("DONE", max(nums), min(nums))
