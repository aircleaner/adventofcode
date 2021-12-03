
def get_gamma_epsilon(input):
    zero_count = [0] * 12
    one_count = [0] * 12

    for line in input:
        l = list(line.strip())
        for i, v in enumerate(l):
            zero_count[i] = (zero_count[i] + 1) if (int(v) == 0) else zero_count[i]
            one_count[i] += int(v)

    gamma = [1 if (one_count[i] >= zero_count[i]) else 0 for i, _ in enumerate(zero_count)]
    epsilon = [1 if (one_count[i] < zero_count[i]) else 0 for i, _ in enumerate(zero_count)]
    print(gamma)
    print(epsilon)
    print()
    return gamma, epsilon

input = []
with open('input_3.txt') as input_file:
    for line in input_file:
        input.append(line.strip())

gamma, epsilon = get_gamma_epsilon(input)

oxygen = input
for i, _ in enumerate(gamma):
    gamma, _ = get_gamma_epsilon(oxygen)
    if len(oxygen) == 1:
        break
    oxygen = [v for v in oxygen if int(v[i]) == gamma[i]]

co = input
for i, _ in enumerate(epsilon):
    _, epsilon = get_gamma_epsilon(co)
    if len(co) == 1:
        break
    co = [v for v in co if int(v[i]) == epsilon[i]]

print(oxygen)
print(co)
print(int(''.join(map(str, oxygen)), 2) * int(''.join(map(str, co)), 2))
