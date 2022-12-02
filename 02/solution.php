<?php
function lines(): Generator
{
    $file = fopen('input.txt', 'r');
    while (($line = fgets($file)) !== false) {
        yield trim($line);
    }
    fclose($file);
}

function plays($lines): Generator
{
    foreach($lines as $line) {
        [$opponent, $you] = explode(" ", $line);
        yield [ord($opponent) - ord("A"), ord($you) - ord("X")];
    }
}

function corrected_plays($plays): Generator
{
    // now map X, Y, Z onto lose/tie/win instead of rock/paper/scissors
    foreach($plays as [$opponent, $you]) {
        yield [$opponent, ($opponent + $you - 1 + 3) % 3];
    }
}

function scores($plays): Generator
{
    foreach($plays as $play) {
        list($opponent, $you) = $play;
        // PHP modulus operator returns same sign as first operand. To get
        // positive value out ensure we put positive value in.
        yield 1 + $you + (($you - $opponent + 1 + 3) % 3) * 3;
    }
}

function iterator_sum($iterator): int
{
    $total = 0;
    foreach($iterator as $item) {
        $total += $item;
    }
    return $total;
}

function solution1(): int
{
    return iterator_sum(scores(plays(lines())));
}

function solution2(): int
{
    return iterator_sum(scores(corrected_plays(plays(lines()))));
}

echo "Part 1: " . solution1() . "\n";
echo "Part 2: " . solution2() . "\n";