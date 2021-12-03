depth = 0
horizontal = 0

with open('input_2.txt') as input_file:
    for line in input_file:
        l = line.split()
        if l[0] == "forward":
            horizontal = horizontal + int(l[1])
            print(f"forward: {int(l[1])}")
        elif l[0] == "down":
            depth = depth + int(l[1])
            print(f"down: {int(l[1])}")
        elif l[0] == "up":
            depth = depth - int(l[1])
            print(f"up: {int(l[1])}")

print(f"horizontal: {horizontal}, depth: {depth}, result: {horizontal * depth}")