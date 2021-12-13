def parse(input):
    d, f = input.strip().split('\n\n')
    dots = set()
    folds = []

    for r in d.splitlines():
        dots.add(tuple(map(int, r.split(','))))

    for r in f.splitlines():
        a, v = r.rsplit(' ', 1)[-1].split('=')
        folds.append((a, int(v)))

    return dots, folds


def part1(input):
    dots, folds = parse(input)

    fold = folds[0]

    for dot in dots.copy():
        if fold[0] == 'x' and dot[0] > fold[1]:
            dots.remove(dot)
            d = (fold[1] - (dot[0] - fold[1]), dot[1])
            dots.add(d)
        elif fold[0] == 'y' and dot[1] > fold[1]:
            dots.remove(dot)
            d = (dot[0], fold[1] - (dot[1] - fold[1]))
            dots.add(d)

    return len(dots)


def str_dots(dots):
    max_x, max_y = tuple(map(max, zip(*dots)))
    ret = '\n'
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            ret += '#' if (x, y) in dots else ' '
        ret += '\n'
    return ret


def part2(input):
    dots, folds = parse(input)

    for fold in folds:
        for dot in dots.copy():
            if fold[0] == 'x' and dot[0] > fold[1]:
                dots.remove(dot)
                d = (fold[1] - (dot[0] - fold[1]), dot[1])
                dots.add(d)
            elif fold[0] == 'y' and dot[1] > fold[1]:
                dots.remove(dot)
                d = (dot[0], fold[1] - (dot[1] - fold[1]))
                dots.add(d)

    return str_dots(dots)


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:.20f})')
