input = []
with open('input_1.txt') as input_file:
    for line in input_file:
        input.append(int(line.strip()))

increasing = 0

print(sum(input[0:0+3]))
for i, _ in enumerate(input):
    if i > len(input) - 1 - 2 - 1:
        break
    if sum(input[i:i+3]) < sum(input[i+1:i+3+1]):
        increasing = increasing + 1


print(f"\nNumber of increasing: {increasing}")