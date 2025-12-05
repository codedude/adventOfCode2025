#!/bin/python

import sys
import utils


def part1(data):
    result = 0
    for line in data:
        visited = {digit: set() for digit in line}
        for i in range(len(line)):
            for j in range(0, i):
                visited[line[j]].add(line[i])  # add all possibilities to others
        visited = [[k, v] for k, v in visited.items()]  # dict to array
        visited.sort(key=lambda e: e[0], reverse=True)  # sort array desc
        for e in visited:
            if len(e[1]) == 0:
                continue
            result += int(f"{e[0]}{max(e[1])}")
            break
    return result


MAX_DIGITS = 12


def part2(input_file):
    result = 0
    for line in input_file:
        soluce = []
        cursor = 0
        for i in range(MAX_DIGITS):  # Find 12 digits
            currentMax = line[cursor]
            for j in range(
                cursor + 1, len(line) - (MAX_DIGITS - i - 1)
            ):  # Find current max digit
                if line[j] > currentMax:
                    currentMax = line[j]
                    cursor = j
            soluce.append(currentMax)
            cursor += 1
        r = int("".join(soluce))
        result += r
    return result


if __name__ == "__main__":
    data = utils.read_lines("inputs/day3.txt")
    ret = part1(data)
    print("Result 1: ", ret)
    ret = part2(data)
    print("Result 2: ", ret)
    sys.exit()
