def parse(input):
    input = input.strip().split('\n\n')
    numbers = list(map(int, input.pop(0).split(',')))
    boards = [[list(map(int, r.split())) for r in b.split('\n')] for b in input]
    return numbers, boards


def has_won(board, drawn):
    height = len(board)
    width = len(board[0])

    for row in range(height):
        if all(board[row][col] in drawn for col in range(0, width)):
            return True

    for col in range(width):
        if all(board[row][col] in drawn for row in range(0, height)):
            return True

    return False


def part1(input):
    numbers, boards = parse(input)
    for i in range(1, len(numbers)):
        for board in boards:
            if has_won(board, numbers[:i]):
                return numbers[i-1] * sum(sum(n for n in row if n not in numbers[:i]) for row in board)


def part2(input):
    numbers, boards = parse(input)
    won = []
    for i in range(1, len(numbers)):
        for j, board in enumerate(boards):
            if j not in won and has_won(board, numbers[:i]):
                won.append(j)
                if len(won) == len(boards):
                    return numbers[i-1] * sum(sum(n for n in row if n not in numbers[:i]) for row in board)


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:.20f})')
