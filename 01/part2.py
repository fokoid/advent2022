import heapq;


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
    heap = []

    with open("input.txt") as f:
        lines = map(str.strip, f)
        groups = make_groups(lines)
        for group in groups:
            heapq.heappush(heap, -sum(group))

    return -sum(heapq.heappop(heap) for _ in range(3))


if __name__ == "__main__":
    print(solution())
