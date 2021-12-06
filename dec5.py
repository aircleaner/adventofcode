import numpy as np


def read_input(path):
    coordinates = []
    with open(path) as input_file:
        for line in input_file:
            coordinates.append([[int(c) for c in v.strip().split(',')] for v in line.strip().split('->')])
    return np.array(coordinates)


def min_max(coord, pos):
    if coord[0][pos] < coord[1][pos]:
        return coord[0][pos], coord[1][pos]
    else:
        return coord[1][pos], coord[0][pos]


def part1(coordinates):
    max = np.amax(coordinates) + 1
    cloud_map = np.zeros((max, max), dtype=int)
    # print(cloud_map)

    for i, c in enumerate(coordinates):
        if c[0][0] == c[1][0]:
            # print(f"Match x: {c[0][0]} c[0][1]:{c[0][1]}, c[1][1]:{c[1][1]} min_max: {min_max(c, 1)}")
            min, max = min_max(c, 1)
            cloud_map[min:max+1, c[0][0]] += 1
        if c[0][1] == c[1][1]:
            # print(f"Match y: {c[0][1]} c[0][0]:{c[0][0]}, c[1][0]:{c[1][0]} min_max: {min_max(c, 0)}")
            min, max = min_max(c, 0)
            cloud_map[c[0][1], min:max+1] += 1
        # print(cloud_map)
    return (cloud_map > 1).sum()


if __name__ == '__main__':
    coordinates = read_input('input_5_test.txt')
    print(coordinates)
    result = part1(coordinates)
    expected = 5
    assert result == expected, f"Result was: {result} epected: {expected}"

    coordinates = read_input('input_5.txt')
    result = part1(coordinates)
    print(f"part1 result: {result}")
