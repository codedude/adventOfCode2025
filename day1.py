#!/bin/python

import sys
import utils

def main():
    data = utils.read_lines("inputs/day1.txt")
    zeros = 0
    value = 50
    for line in data:
        if len(line) == 0:
            continue
        offset = int(line[1:])
        value += offset if line[0] == "R" else -offset
        zeros += abs(value // 100)
        value %= 100
    return zeros

if __name__ == '__main__':
    ret = main()
    print(ret)
    sys.exit()
