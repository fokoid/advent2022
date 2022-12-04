import { open } from 'node:fs/promises';
import { createInterface } from 'node:readline';

async function* read_lines() {
    const file = await open('input.txt');
    const stream = await file.createReadStream();
    const rl = createInterface({input: stream, clrfDelay: Infinity});
    for await (const line of rl) {
        yield line;
    }
    stream.close();
    file.close();
}

async function* ranges(lines) {
    const parseRange = s => {
        const [start, end] = s.split('-').map(x => parseInt(x, 10));
        return {start, end};
    }

    for await (const line of lines) {
        yield line.split(',').map(parseRange);
    }
}

const solution1 = async lines => {
    const isContainedSymmetric = ([range1, range2]) => {
        return (range1.start <= range2.start && range1.end >= range2.end)
            || (range2.start <= range1.start && range2.end >= range1.end);
    }

    return await sum(await map(isContainedSymmetric, ranges(lines)));
}

const solution2 = async lines => {
    const isOverlapping = ([range1, range2]) => {
        return (range1.start <= range2.start && range2.start <= range1.end)
            || (range2.start <= range1.start && range1.start <= range2.end);
    }

    return await sum(await map(isOverlapping, ranges(lines)));
}

// unfortunately, no native map/reduce over async generators
const sum = async asyncGenerator => {
    let total = 0;
    for await (const value of asyncGenerator) {
        total += value;
    }
    return total;
}

const map = async function*(f, asyncGenerator) {
    for await (const value of asyncGenerator) {
        yield f(value);
    }
}

console.log(`Part 1: ${await solution1(read_lines())}.`);
console.log(`Part 2: ${await solution2(read_lines())}.`);
