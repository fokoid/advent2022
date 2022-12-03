import functools
import operator


def read_lines():
    with open("input.txt") as f:
        yield from map(str.strip, f)


def solution1(lines):
    return sum(map(score, mismatched_items(read_lines())))


def solution2(lines):
    return sum(map(score, badges(read_lines())))


def mismatched_items(lines):
    for line in lines:
        mid = len(line) // 2
        items = set(line[:mid])
        for char in line[mid:]:
            if char in items:
                yield char
                break
        else:
            # if we fall off here without ever breaking, something went wrong
            raise RuntimeError(f"No mismatched item found: {line}")


def badges(lines):
    for elves in zip(lines, lines, lines):
        charset = functools.reduce(operator.and_, map(set, elves))
        if len(charset) != 1:
            raise RuntimeError(f"expected 1 badge got {charset}")
        yield charset.pop()


def score(char):
    result = ord(char) + 1
    if result > ord('a'):
        result -= ord('a')
    else:
        result -= ord('A')
        result += 26
    return result


if __name__ == "__main__":
    print(f"Part 1: {solution1(read_lines())}")
    print(f"Part 2: {solution2(read_lines())}")
