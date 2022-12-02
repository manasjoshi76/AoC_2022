from itertools import groupby
import random, math

def load():
	with open('day01Input.txt') as file:
		data = file.readlines()
		d = [line.strip() for line in data]
	return d

inpt = load()

def part1(inpt):
    _cal = [list(g) for k, g in groupby(inpt, lambda x: x != '') if k]
    _mid = list(map(lambda line: list(map(lambda p: int(p), line)), _cal))
    _max = max(sum(l) for l in _mid)
    return _max

def part2(inpt):
    _cal = [list(g) for k, g in groupby(inpt, lambda x: x != '') if k]
    _mid = list(map(lambda line: list(map(lambda p: int(p), line)), _cal))
    _max = sum(sorted([sum(l) for l in _mid], reverse=True)[:3])
    return _max

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')