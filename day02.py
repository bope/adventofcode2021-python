_p1_map = {
    'forward': lambda p, v: (p[0] + v, p[1]),
    'down': lambda p, v: (p[0], p[1] + v),
    'up': lambda p, v: (p[0], p[1] - v),
}

_p2_map = {
    'down': lambda p, v: (p[0], p[1], p[2] + v),
    'up': lambda p, v: (p[0], p[1], p[2] - v),
    'forward': lambda p, v: (p[0] + v, p[1] + (p[2] * v), p[2]),
}


def parse(input):
    ret = []
    for line in input.strip().splitlines():
        a, b = line.split(' ')
        ret.append((a, int(b)))
    return ret


def part1(input):
    input = parse(input)
    p = (0, 0)
    for d, v in input:
        p = _p1_map[d](p, v)
    return p[0] * p[1]


def part2(input):
    input = parse(input)
    p = (0, 0, 0)
    for d, v in input:
        p = _p2_map[d](p, v)
    return p[0] * p[1]


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:.20f})')
