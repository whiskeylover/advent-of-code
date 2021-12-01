inc = 0
last = None

with open("input.txt", "r") as input:
    depths = input.readlines()

    for i in range(len(depths)):
        if i < 2:
            continue

        tot = int(depths[i - 2]) + int(depths[i - 1]) + int(depths[i])
        if not last:
            last = tot

        if tot > last:
            inc += 1

        last = tot

print(inc)
