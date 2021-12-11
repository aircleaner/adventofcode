import numpy as np
import math


def read_input(file):
    input = []
    with open(file) as input_file:
        for line in input_file:
            input.append([int(x) for x in line.strip()])
    # print(input)
    return input


def inc_by_one(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] += 1


def set_to_zero(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] > 9:
                list[i][j] = 0


def inc_adjacent(list, idx):
    # print(f"idx: {idx}")
    for i in range(max(idx[0] - 1, 0), min(idx[0] + 1 + 1, len(list))):
        # print(f"i: {i}")
        for j in range(max(idx[1] - 1, 0), min(idx[1] + 1 + 1, len(list[i]))):
            # print(f" j: {j}")
            list[i][j] += 1


def flash(list, flashed=None):
    if flashed is None:
        flashed = [[0 for i in range(10)] for j in range(10)]
    flashes = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] > 9 and flashed[i][j] == 0:
                flashed[i][j] = 1
                flashes += 1
                inc_adjacent(list, [i, j])
    if flashes > 0:
        flashes += flash(list, flashed=flashed)
    return flashes


def print_list(list):
    for i in range(len(list)):
        line = ""
        for j in range(len(list[i])):
            if list[i][j] < 10:
                line += f" {list[i][j]} "
            else:
                line += f"{list[i][j]} "
        print(line)
    print("\n")


def part1(input):
    flashes = 0
    # print_list(input)
    for i in range(100):
        inc_by_one(input)
        flashes += flash(input)
        set_to_zero(input)
        # print_list(input)
    return flashes


def part2(input):
    # print_list(input)
    for i in range(2000):
        inc_by_one(input)
        flashes = flash(input)
        print(flashes)
        if flashes == len(input)*len(input[0]):
            return i + 1
        set_to_zero(input)
        # print_list(input)
    return None


if __name__ == '__main__':
    input = read_input("input_11_test.txt")
    result = part1(input)
    expected = 1656
    assert result == expected, f"Result was: {result} epected: {expected}"

    input = read_input("input_11.txt")
    result = part1(input)
    print(f"part1 result: {result}")
    assert result == 1721

    input = read_input("input_11_test.txt")
    result = part2(input)
    expected = 195
    assert result == expected, f"Result was: {result} epected: {expected}"

    input = read_input("input_11.txt")
    result = part2(input)
    print(f"part2 result: {result}")
    assert result == 298
