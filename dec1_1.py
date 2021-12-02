input = []
with open('input_1_1.txt') as input_file:
    for line in input_file:
        input.append(int(line.strip()))

# print(input)

increasing = 0

for i, v in enumerate(input):
    if i == 0:
        continue
    if v > input[i - 1]:
        increasing = increasing + 1

print(f"\nNumber of increasing: {increasing}")