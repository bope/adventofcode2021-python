def parse(input):
    return list(map(int, input.strip().split(',')))


def part1(input):
    input = parse(input)
    ma = max(input)
    mi = min(input)

    fs = []
    for p in range(mi, ma+1):
        f = 0
        for i in input:
            f += abs(i - p)
        fs.append(f)
    return min(fs)


def part2(input):
    input = parse(input)
    return int(min(sum(abs(i - p) * (abs(i - p) + 1) / 2 for i in input) for p in range(min(input), max(input)+1)))


if __name__ == '__main__':
    import sys
    import utils
    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:0.20f})')
