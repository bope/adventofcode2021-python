
def parse(input):
    return input.strip().splitlines()


def part1(input):
    input = parse(input)

    gamma = 0
    epsilon = 0
    bit_size = len(input[0])
    rows = len(input)

    for pos in range(bit_size):
        tot = 0
        for row in range(len(input)):
            tot += int(input[row][pos])

        shift = bit_size - pos - 1
        g = round(tot/rows)
        gamma |= g << shift
        epsilon |= (1 - g) << shift

    return gamma * epsilon


def part2(input):
    input = parse(input)

    bit_size = len(input[0])
    values = [int(v, 2) for v in input]

    om = 0b0
    cm = 0b0
    fm = 0b0
    oxy = None
    co2 = None

    for pos in range(bit_size-1, -1, -1):
        oc = 0
        cc = 0
        for value in values:
            if ((value ^ om) & fm) == 0:
                oc += 1 if value & (1 << pos) else -1
                oxy = value

            if ((value ^ cm) & fm) == 0:
                cc += 1 if value & (1 << pos) else -1
                co2 = value

        if oc >= 0:
            om |= 1 << pos

        if cc < 0:
            cm |= 1 << pos

        fm |= 1 << pos

    return oxy * co2


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:.20f})')
