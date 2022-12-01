class Done(Exception):
    """eww"""
    pass


def make_groups(lines):
    def inner():
        try:
            while line := next(lines):
                yield int(line)
        except StopIteration:
            raise Done()

    try:
        while True:
            yield list(inner())
    except Done:
        pass


def solution():
    with open("input.txt") as f:
        lines = map(str.strip, f)
        groups = make_groups(lines)
        return max(map(sum, groups))


if __name__ == "__main__":
    print(solution())
