def parse(input):
    ret = {}
    for y, row in enumerate(input.strip().splitlines()):
        for x, char in enumerate(row):
            ret[(x, y)] = int(char)
    return ret


def neighbors(p):
    for x in range(p[0] - 1, p[0] + 2):
        for y in range(p[1] - 1, p[1] + 2):
            if (x, y) == p:
                continue
            yield (x, y)


def check_flash(p, input, flashed):
    if p in flashed:
        return

    if input[p] <= 9:
        return

    flashed.add(p)

    for n in neighbors(p):
        if n not in input:
            continue
        input[n] += 1
        check_flash(n, input, flashed)


def part1(input, steps):
    input = parse(input)

    flashes = 0
    for step in range(steps):
        for p in input:
            input[p] += 1

        flashed = set()
        for p in input:
            check_flash(p, input, flashed)

        flashes += len(flashed)

        for p in flashed:
            input[p] = 0
    return flashes


def part2(input):
    input = parse(input)

    step = 0
    while True:
        step += 1
        for p in input:
            input[p] += 1

        flashed = set()
        for p in input:
            check_flash(p, input, flashed)

        if len(flashed) == len(input):
            return step

        for p in flashed:
            input[p] = 0


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input, 100)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:.20f})')
