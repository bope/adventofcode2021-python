def parse(input):
    input = input.strip().replace(' -> ', ',').split('\n')
    return [list(map(int, r.split(','))) for r in input]


def iter_axis(a, b):
    if a < b:
        return range(a, b + 1)
    return range(a, b - 1, -1)


def iter_lines(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return ((x, y) for x in iter_axis(x1, x2) for y in iter_axis(y1, y2))
    return zip(iter_axis(x1, x2), iter_axis(y1, y2))


def part1(input):
    input = parse(input)
    points = set()
    overlap = set()
    for x1, y1, x2, y2 in input:
        if x1 != x2 and y1 != y2:
            continue
        line = set(iter_lines(x1, y1, x2, y2))
        overlap |= (points & line)
        points |= line

    return len(overlap)


def part2(input):
    input = parse(input)
    points = set()
    overlap = set()

    for p in input:
        line = set(iter_lines(*p))
        overlap |= (points & line)
        points |= line
    return len(overlap)


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:.20f})')
