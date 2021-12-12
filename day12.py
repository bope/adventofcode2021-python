from collections import defaultdict


def parse(input):
    ret = defaultdict(list)
    for row in input.strip().splitlines():
        a, b = row.split('-')
        ret[a].append(b)
        ret[b].append(a)
    return ret


def walk_paths1(path, input):
    if path[-1] == 'end':
        return [path]

    ret = []
    for room in input[path[-1]]:
        if room.lower() == room and room in path:
            continue
        p = path[:]
        p.append(room)
        ret.extend(walk_paths1(p, input))
    return ret


def part1(input):
    input = parse(input)
    paths = walk_paths1(['start'], input)
    return len(paths)


def is_small_cave(room):
    return room.lower() == room


def can_visit(path, room):
    if room == 'end':
        return True

    if room == 'start':
        return False

    if not is_small_cave(room):
        return True

    if room not in path:
        return True

    for visited in path:
        if is_small_cave(visited) and path.count(visited) == 2:
            return False
    return True


def walk_paths2(path, input):
    if path[-1] == 'end':
        return [path]

    ret = []
    for room in input[path[-1]]:
        if not can_visit(path, room):
            continue

        p = path[:]
        p.append(room)
        ret.extend(walk_paths2(p, input))
    return ret


def part2(input):
    input = parse(input)
    paths = walk_paths2(['start'], input)
    return len(paths)


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:.20f})')
