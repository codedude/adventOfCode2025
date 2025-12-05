#!/bin/python

import sys
import utils


def part1():
    data = utils.read_lines("inputs/day2.txt")
    ranges = data[0].split(",")
    total = 0
    for idrange in ranges:
        left, right = idrange.split("-")
        for i in range(int(left), int(right) + 1):
            istr = str(i)
            if len(istr) % 2 != 0:
                continue
            if istr[: len(istr) // 2] == istr[len(istr) // 2 :]:
                total += i
    return total


def part2():
    data = utils.read_lines("inputs/day2.txt")
    ranges = data[0].split(",")
    total = 0
    for idrange in ranges:
        left, right = idrange.split("-")
        for i in range(int(left), int(right) + 1):
            istr = str(i)
            powerstr = len(istr) // (istr + istr).find(istr, 1)
            total += i if powerstr > 1 else 0
    return total


if __name__ == "__main__":
    ret = part1()
    print("Result 1: ", ret)
    ret = part2()
    print("Result 2: ", ret)
    sys.exit()
