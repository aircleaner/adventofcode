zero_count = [0] * 12
one_count = [0] * 12

with open('input_3.txt') as input_file:
    for line in input_file:
        l = list(line.strip())
        for i, v in enumerate(l):
            zero_count[i] = (zero_count[i] + 1) if (int(v) == 0) else zero_count[i]
            one_count[i] += int(v)

gamma = [1 if (one_count[i] > zero_count[i]) else 0 for i,_ in enumerate(zero_count)]
epsilon = [1 if (one_count[i] < zero_count[i]) else 0 for i,_ in enumerate(zero_count)]
print(gamma)
print(epsilon)
g = int(''.join(map(str, gamma)), 2)
e = int(''.join(map(str, epsilon)), 2)
print(g * e)