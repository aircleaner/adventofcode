import numpy as np
import math


def read_input(file):
    input = []
    with open(file) as input_file:
        for line in input_file:
            input.append(line.strip())
    # print(input)
    return input



lefts = ['(', '[', '{', '<']
left_right = {'(': ')', '[': ']', '{': '}', '<': '>'}
illegal_values = {')': 3, ']': 57, '}': 1197, '>': 25137}
complete_values = {')': 1, ']': 2, '}': 3, '>': 4}


def part1(input):
    illegal_sum = 0
    for line in input:
        # print(line)
        left_list = []
        for c in line:
            # print(c)
            if c in lefts:
                left_list.append(c)
            else:
                left = left_list.pop()
                if c != left_right[left]:
                    # print(f"found illegal {c}")
                    illegal_sum += illegal_values[c]
                    break
            # print(left_list)
    return illegal_sum


def part2(input):
    result = []
    for line in input:
        complete_sum = 0
        # print(line)
        left_list = []
        complete = True
        for c in line:
            # print(c)
            if c in lefts:
                left_list.append(c)
            else:
                left = left_list.pop()
                if c != left_right[left]:
                    # print(f"found illegal {c}")
                    complete = False
                    break
            # print(left_list)
        if complete:
            # print(left_list)
            for v in reversed(left_list):
                complete_sum = complete_sum * 5 + complete_values[left_right[v]]
            result.append(complete_sum)
    # print(result)
    result.sort()
    # print(result)
    return result[int(len(result)/2)]


if __name__ == '__main__':
    input = read_input("input_10_test.txt")
    result = part1(input)
    expected = 26397
    assert result == expected, f"Result was: {result} epected: {expected}"

    input = read_input("input_10.txt")
    result = part1(input)
    print(f"part1 result: {result}")
    assert result == 271245

    input = read_input("input_10_test.txt")
    result = part2(input)
    expected = 288957
    assert result == expected, f"Result was: {result} epected: {expected}"

    input = read_input("input_10.txt")
    result = part2(input)
    print(f"part2 result: {result}")
    assert result == 1685293086
