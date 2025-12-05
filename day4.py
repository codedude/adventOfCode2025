#!/bin/python

import sys
import utils


def makeGrid(data):
    return [[e for e in line] for line in data]


def nOfRollAround(grid, y, x):
    n = 0
    if x != 0:
        if grid[y][x - 1] == "@":
            n += 1
        if y != 0:
            if grid[y - 1][x - 1] == "@":
                n += 1
        if y < len(grid) - 1:
            if grid[y + 1][x - 1] == "@":
                n += 1
    if x < len(grid[0]) - 1:
        if grid[y][x + 1] == "@":
            n += 1
        if y != 0:
            if grid[y - 1][x + 1] == "@":
                n += 1
        if y < len(grid) - 1:
            if grid[y + 1][x + 1] == "@":
                n += 1
    if y != 0:
        if grid[y - 1][x] == "@":
            n += 1
    if y < len(grid) - 1:
        if grid[y + 1][x] == "@":
            n += 1
    return n


def part1(data):
    result = 0
    grid = makeGrid(data)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@" and nOfRollAround(grid, i, j) < 4:
                result += 1
    return result


def part2(data):
    result = 0
    grid = makeGrid(data)
    run = True
    while run is True:
        n_removed = 0
        grid_cpy = [[e for e in line] for line in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@" and nOfRollAround(grid, i, j) < 4:
                    grid_cpy[i][j] = ","
                    result += 1
                    n_removed += 1
        grid = grid_cpy
        if n_removed == 0:
            run = False
    return result


if __name__ == "__main__":
    data = utils.read_lines("inputs/day4.txt")
    ret = part1(data)
    print("Result 1: ", ret)
    ret = part2(data)
    print("Result 2: ", ret)
    sys.exit()
