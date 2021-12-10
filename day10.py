pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

points1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

points2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def parse(input):
    return input.splitlines()


def part1(input):
    input = parse(input)
    ret = 0
    for line in input:
        stack = []
        for char in line:
            if char in pairs:
                stack.append(pairs[char])
                continue
            if char != stack[-1]:
                ret += points1[char]
                break
            stack.pop()
    return ret


def part2(input):
    input = parse(input)
    scores = []
    for line in input:
        stack = []
        for char in line:
            if char in pairs:
                stack.append(pairs[char])
                continue
            if char != stack[-1]:
                break
            stack.pop()
        else:
            score = 0
            for char in reversed(stack):
                score *= 5
                score += points2[char]
            scores.append(score)
    scores.sort()
    return scores[len(scores)//2]


if __name__ == '__main__':
    import sys
    import utils

    input = sys.stdin.read()

    p1, t1 = utils.time(part1, input)
    print(f'part1: {p1} ({t1:.20f})')

    p2, t2 = utils.time(part2, input)
    print(f'part2: {p2} ({t2:.20f})')
