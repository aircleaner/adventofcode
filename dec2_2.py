depth = 0
horizontal = 0
aim = 0

with open('input_2.txt') as input_file:
    for line in input_file:
        l = line.split()
        if l[0] == "forward":
            horizontal = horizontal + int(l[1])
            depth = depth + aim * int(l[1])
        elif l[0] == "down":
            aim = aim + int(l[1])
        elif l[0] == "up":
            aim = aim - int(l[1])

print(f"horizontal: {horizontal}, depth: {depth}, result: {horizontal * depth}")