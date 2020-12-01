#!

data = []

input_file = open("q1_1.txt", "r")

for line in input_file:
    try:
        num = int(line.strip())
        data.append(num)
    except:
        pass

print(len(data))

found = False
for num in data:
    for num2 in data:
        for num3 in data:
            if num + num2 + num3 == 2020:
                print(f"1: {num} 2: {num2} 3: {num3} = {num*num2*num3}")
                found = True
                break

        if found:
            break

    if found:
        break
