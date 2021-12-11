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


def add_energy(p, input, flashed):
    if p in flashed:
        return

    input[p] += 1
    if input[p] <= 9:
        return
    input[p] = 0

    flashed.add(p)

    for n in neighbors(p):
        if n not in input:
            continue
        add_energy(n, input, flashed)


def part1(input, steps):
    input = parse(input)

    flashes = 0
    for step in range(steps):
        flashed = set()
        for p in input:
            add_energy(p, input, flashed)

        flashes += len(flashed)

    return flashes


def part2(input):
    input = parse(input)

    step = 0
    while True:
        step += 1
        flashed = set()
        for p in input:
            add_energy(p, input, flashed)

        if len(flashed) == len(input):
            return step


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input, 100)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:.20f})')
