from collections import defaultdict


def parse(input):
    ret = []
    input = input.splitlines()
    for line in input:
        parts = line.split(' | ')
        ret.append(
            [[set(c) for c in parts[0].split()], [set(d) for d in parts[1].split()]]
        )
    return ret


def part1(input):
    input = parse(input)
    ret = 0
    for _, output in input:
        for i in output:
            if len(i) in (2, 4, 3, 7):
                ret += 1
    return ret


def part2(input):
    input = parse(input)
    ret = 0
    for notes, digits in input:
        lens = defaultdict(list)

        for n in notes:
            lens[len(n)].append(n)

        cf = lens[2][0]
        bcdf = lens[4][0]
        acf = lens[3][0]
        abcdefg = lens[7][0]

        a = acf - cf
        bd = bcdf - cf
        eg = abcdefg - a - bd - cf

        # 2 = a cde g
        # 3 = a cd fg
        # 5 = ab d fg
        # all contain: adg
        dg = (lens[5][0] & lens[5][1] & lens[5][2]) - a
        g = dg & eg
        e = eg - g
        d = dg - g

        # 0 = abc efg
        # 6 = ab defg
        # 9 = abcd fg
        # all contain abfg
        bf = (lens[6][0] & lens[6][1] & lens[6][2]) - a - g
        b = bf - cf
        f = bf - b
        c = cf - f

        s = {
            frozenset(a | b | c | f | e | g): 0,
            frozenset(c | f): 1,
            frozenset(a | c | d | e | g): 2,
            frozenset(a | c | d | f | g): 3,
            frozenset(b | c | d | f): 4,
            frozenset(a | b | d | f | g): 5,
            frozenset(a | b | d | f | e | g): 6,
            frozenset(a | c | f): 7,
            frozenset(a | b | c | d | f | e | g): 8,
            frozenset(a | b | c | d | f | g): 9,
        }

        ds = ''
        for d in digits:
            ds += str(s[frozenset(d)])
        ret += int(ds)
    return ret


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input[:])
    print(f'part1: {p1} ({t1:.20f})')
    p2, t2 = utils.time(part2, input[:])
    print(f'part2: {p2} ({t2:.20f})')
