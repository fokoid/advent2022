import functools
import heapq


def read_lines():
    with open("input.txt") as f:
        yield from map(str.strip, f)


def groups(lines):
    done = False

    def line_group():
        for line in lines:
            if not line:
                break
            yield line
        else:
            nonlocal done
            done = True

    while not done:
        yield line_group()


def elves(lines):
    yield from map(functools.partial(map, int), groups(map(str.strip, lines)))


def elf_totals(lines):
    yield from map(sum, elves(lines))


def solution1(lines):
    return max(elf_totals(lines))


def solution2(lines):
    heap = []
    for total in elf_totals(lines):
        if len(heap) < 3:
            heapq.heappush(heap, total)
        else:
            heapq.heappushpop(heap, total)

    return sum(heap)


if __name__ == "__main__":
    print(f"Part 1: {solution1(read_lines())}")
    print(f"Part 2: {solution2(read_lines())}")
