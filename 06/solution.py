import collections
import functools


def prime(coro):
    @functools.wraps(coro)
    def inner(*args, **kwargs):
        result = coro(*args, **kwargs)
        next(result)
        return result

    return inner


def get_result(coro):
    try:
        next(coro)
    except StopIteration as e:
        return e.value
    else:
        raise RuntimeError(f"coroutine {coro!r} did not return a value")


@prime
def make_solution(n):
    count = 0
    ring = collections.deque(maxlen=n)

    while len(ring) < n or len(set(ring)) < n:
        ring.append((yield))
        count += 1
    while (yield):
        pass

    return count


def read_chars():
    with open("input.txt") as f:
        while c := f.read(1):
            yield c


def main():
    solutions = [make_solution(n) for n in [4, 14]]
    for c in read_chars():
        for solution in solutions:
            solution.send(c)
    for i, solution in enumerate(solutions, 1):
        print(f"Part {i}: {get_result(solution)}")


if __name__ == "__main__":
    main()
