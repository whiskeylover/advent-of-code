inc = 0
last = None

with open("input.txt", "r") as input:
    for depth in input.readlines():
        #print(depth.strip())
        depth = int(depth)
        if not last:
            last = depth

        if depth > last:
            inc += 1

        last = depth

print(inc)
