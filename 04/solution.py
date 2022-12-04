def read_lines():
    with open("input.txt") as f:
        yield from map(str.strip, f)


def ranges(lines):
    def parse_range(s):
        start, stop = map(int, s.split("-"))
        return range(start, stop + 1)

    for line in lines:
        yield tuple(map(parse_range, line.split(",")))


def solution1(lines):
    return sum((xs.start <= ys.start and xs.stop >= ys.stop)
               or (ys.start <= xs.start and ys.stop >= xs.stop)
               for xs, ys in ranges(lines))


def solution2(lines):
    return sum(xs.start in ys or ys.start in xs for xs, ys in ranges(lines))


if __name__ == "__main__":
    print(f"Part 1: {solution1(read_lines())}")
    print(f"Part 2: {solution2(read_lines())}")
