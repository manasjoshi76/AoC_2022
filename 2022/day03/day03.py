import random, math

def load(filename):
	with open(filename) as file:
		data = file.readlines()
		d = [line.strip() for line in data]
	return d

inpt_example = load('day03Example.txt')
inpt_problem = load('day03Input.txt')

def part1(inpt):
    total_ = 0
    for rucksack_ in inpt:
        cmpt_size_ = len(rucksack_) // 2
        left_cmpt_, right_cmpt_ = rucksack_[:cmpt_size_], rucksack_[cmpt_size_:]
        item_ = str(set(left_cmpt_) & set(right_cmpt_))[2]
        item_score_ = (ord(item_) - 96) if item_.islower() else (ord(item_) - 38)
        total_ = total_ + item_score_
    return total_

def part2(inpt):
    total_ = 0
    rucksacks_ = [inpt[n:n+3] for n in range(0, len(inpt), 3)]
    for rucksack_ in rucksacks_:
        item_ = str(set(rucksack_[0]) & set(rucksack_[1]) & set(rucksack_[2]))[2]
        item_score_ = (ord(item_) - 96) if item_.islower() else (ord(item_) - 38)
        total_ = total_ + item_score_
    return total_

print(f'EXAMPLE - Part1: {part1(inpt_example)}\nPart2: {part2(inpt_example)}')
print(f'PROBLEM - Part1: {part1(inpt_problem)}\nPart2: {part2(inpt_problem)}')