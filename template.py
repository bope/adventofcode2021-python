def parse(input):
    return input.splitlines()


def part1(input):
    input = parse(input)


def part2(input):
    input = parse(input)


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:.20f})')
