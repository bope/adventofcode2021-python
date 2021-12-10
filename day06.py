def parse(input):
    return list(map(int, input.strip().split(',')))


def part1(input, days):
    input = parse(input)
    for _ in range(days):
        for i in range(len(input)):
            input[i] -= 1
            if input[i] < 0:
                input[i] = 6
                input.append(8)
    return len(input)


def part2(input, days):
    input = parse(input)
    groups = [0] * 9

    for i in input:
        groups[i] += 1

    for i in range(days):
        groups[(i+7) % 9] += groups[i % 9]

    return sum(groups)


if __name__ == '__main__':
    import sys
    import utils
    input = sys.stdin.read()

    days = None
    if len(sys.argv) == 2:
        days = int(sys.argv[1])

    p1, t1 = utils.time(part1, input, days or 80)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input, days or 256)
    print(f'part2: {p2} ({t2:.20f})')
