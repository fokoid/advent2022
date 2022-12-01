def make_groups(lines):
    group = []
    for line in lines:
        if line:
            group.append(line)
        else:
            yield group
            group.clear()


def solution():
    with open("input.txt") as f:
        lines = map(str.strip, f)
        groups = make_groups(lines)
        groups = map(lambda group: map(int, group), groups)
        return max(map(sum, groups))


if __name__ == "__main__":
    print(solution())
