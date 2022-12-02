def plays(lines):
    """Map code to plays:
        A, X - rock
        B, Y - paper
        C, Z - scissors
    """
    for line in lines:
        opponent, you = line.split()
        yield ord(opponent) - ord("A"), ord(you) - ord("X")


def corrected_plays(plays):
    """The second value means lose, draw or win not rock, paper or scissors.
        0 (X) - lose
        1 (Y) - tie
        2 (Z) - win
    """
    # the second value means lose, draw or win not rock, paper, scizzors
    for opponent, you in plays:
        yield opponent, (opponent + you - 1) % 3


def scores(plays):
    for opponent, you in plays:
        yield 1 + you + ((you - opponent + 1) % 3) * 3


def solution1(lines):
    return sum(scores(plays(lines)))


def solution2(lines):
    return sum(scores(corrected_plays(plays(lines))))


if __name__ == "__main__":
    with open("input.txt") as f:
        print(f"Part 1: {solution1(f)}")
    with open("input.txt") as f:
        print(f"Part 2: {solution2(f)}")
