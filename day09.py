import operator as op
import functools


def parse(input):
    ret = {}
    for y, line in enumerate(input.strip().splitlines()):
        for x, val in enumerate(line):
            ret[(x, y)] = int(val)
    return ret


def neighbors(p):
    return [
        (p[0]+1, p[1]),
        (p[0]-1, p[1]),
        (p[0], p[1]+1),
        (p[0], p[1]-1)
    ]


def low_point(p, input):
    return all(input[p] < input.get(np, 9) for np in neighbors(p))


def basin_size(p, input, checked):
    if p in checked:
        return 0

    if input.get(p, 9) == 9:
        return 0

    checked.add(p)
    size = 1

    for np in neighbors(p):
        size += basin_size(np, input, checked)

    return size


def part1(input):
    input = parse(input)
    ret = 0
    for p in input:
        if low_point(p, input):
            ret += input[p] + 1
    return ret


def part2(input):
    input = parse(input)
    checked = set()
    basins = []
    for p in input:
        if p in checked:
            continue
        basins.append(basin_size(p, input, checked))
    basins.sort(reverse=True)
    return functools.reduce(op.mul, basins[:3])


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input)
    print(f'part1: {p1} ({t1:0.20f})')
    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:.20f})')
