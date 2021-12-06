def read_input(path):
    numbers = []
    boards = []
    board_id = -1
    with open(path) as input_file:
        for i, line in enumerate(input_file):
            if i == 0:
                numbers = [int(v) for v in line.strip().split(',')]
            elif line == "\n":
                board_id += 1
                boards.append([])
            else:
                boards[board_id].append([(int(v), 0) for v in line.strip().split(' ') if v != ''])
    return numbers, boards


def check_line(line):
    for v in line:
        if v[1] == 0:
            return False
    return True


def has_bingo(boards):
    bingo = None
    for i, board in enumerate(boards):
        for line in board:
            if check_line(line):
                return i
        for j in range(len(board[0])):
            bingo = i
            for k in range(len(board)):
                if board[k][j][1] == 0:
                    bingo = None
                    break
            if bingo != None:
                return bingo
    return bingo


def mark_number(number, boards):
    boards = [[[(v[0], 1) if v[0] == number else (v[0], v[1]) for v in line] for line in board] for board in boards]
    return boards


def board_sum(board):
    sum = 0
    for line in board:
        for x in line:
            if x[1] == 0:
                sum += x[0]
    return sum


def part1(numbers, boards):
    for num in numbers:
        boards = mark_number(num, boards)
        bingo_index = has_bingo(boards)
        if bingo_index != None:
            return board_sum(boards[bingo_index]) * num
    return None


def part2(numbers, boards):
    last_bingo_board = []
    last_bingo_num = None
    for num in numbers:
        boards = mark_number(num, boards)
        while True:
            bingo_index = has_bingo(boards)
            if bingo_index != None:
                if len(boards) == 1:
                    return board_sum(boards[bingo_index]) * num
                else:
                    last_bingo_board = boards[bingo_index]
                    last_bingo_num = num
                    del boards[bingo_index]
            else:
                break
    return board_sum(last_bingo_board) * last_bingo_num


if __name__ == '__main__':
    numbers, boards = read_input('input_4_test.txt')
    # print(numbers)
    # print(boards)
    result = part1(numbers, boards)
    # print(result)
    assert result == 4512, f"Result was: {result} epected: 4512"

    numbers, boards = read_input('input_4.txt')
    result = part1(numbers, boards)
    print(f"part1 result: {result}")

    numbers, boards = read_input('input_4.txt')
    result = part2(numbers, boards)
    print(f"part2 result: {result}")
