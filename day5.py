#!/bin/python

import sys
import utils


def parseInput(data):
    ranges = []
    ids = []
    i = 0
    while True:
        if len(data[i]) == 0:
            break
        left, right = data[i].split("-")
        ranges.append([int(left), int(right)])
        i += 1
    i += 1
    while True:
        if i == len(data) or len(data[i]) == 0:
            break
        ids.append(int(data[i]))
        i += 1
    return ranges, ids


def part1(ranges, ids):
    result = 0
    for e in ids:
        for r in ranges:
            if e >= r[0] and e <= r[1]:
                result += 1
                break
    return result


# l1,r1 = base range, v/l2,r2 range to be tested/added
def v_in_range(l1, r1, v):
    return v >= l1 and v <= r1


def range_in_range(l1, r1, l2, r2):  # assume valid ranges
    return l2 >= l1 and r2 <= r1


def merge_range(l1, r1, l2, r2):
    new_range = [l1, r1]
    if l2 < l1:
        new_range[0] = l2
    if r2 > r1:
        new_range[1] = r2
    return new_range


def range_overlap(l1, r1, l2, r2):
    return v_in_range(l1, r1, l2) or v_in_range(l1, r1, r2)


def interval_union(intervals):
    e = [[low, -1] for (low, _) in intervals]
    e += [[high, +1] for (_, high) in intervals]
    n_open = 0
    last = None
    ret = []
    print(sorted(e))
    for x, _dir in sorted(e):
        if _dir == -1:
            if n_open == 0:
                last = x
            n_open += 1
        else:
            n_open -= 1
            if n_open == 0:
                ret.append((last, x))
    return ret


def part2(ranges, ids):
    result = 0
    merged_ranges = interval_union(ranges)
    for r in merged_ranges:
        result += r[1] - r[0] + 1  # inclusive
    return result


if __name__ == "__main__":
    data = utils.read_lines("inputs/day5.txt")
    ranges, ids = parseInput(data)
    ret = part1(ranges, ids)
    print("Result 1: ", ret)
    ret = part2(ranges, ids)
    print("Result 2: ", ret)
    sys.exit()
