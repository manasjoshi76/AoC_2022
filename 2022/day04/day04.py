import random, math

def load(filename):
	with open(filename) as file:
		data = file.readlines()
		d = [line.strip() for line in data]
	return d

inpt_example = load('day04Example.txt')
inpt_problem = load('day04Input.txt')

def part1(inpt):
    total_ = 0
    for assignments_ in inpt:
        pair1_, pair2_ = assignments_.split(',')
        pair1_, pair2_ = list(map(int, pair1_.split('-'))), list(map(int, pair2_.split('-')))
        assignment1_ = list(range(pair1_[0], pair1_[1]+1))
        assignment2_ = list(range(pair2_[0], pair2_[1]+1))
        total_ += 1 if (set(assignment1_).issubset(assignment2_)) or (set(assignment2_).issubset(assignment1_)) else 0
    return total_

def part2(inpt):
    total_ = 0
    for assignments_ in inpt:
        pair1_, pair2_ = assignments_.split(',')
        pair1_, pair2_ = list(map(int, pair1_.split('-'))), list(map(int, pair2_.split('-')))
        assignment1_ = list(range(pair1_[0], pair1_[1]+1))
        assignment2_ = list(range(pair2_[0], pair2_[1]+1))
        total_ += 1 if (set(assignment1_).intersection(set(assignment2_))) or (set(assignment2_).intersection(set(assignment1_))) else 0
    return total_

print(f'EXAMPLE\nPart1: {part1(inpt_example)}\nPart2: {part2(inpt_example)}')
print(f'PROBLEM\nPart1: {part1(inpt_problem)}\nPart2: {part2(inpt_problem)}')