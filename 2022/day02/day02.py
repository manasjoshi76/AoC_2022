import random, math

def load():
	with open('day02/day02Input.txt') as file:
		data = file.readlines()
		d = [line.strip() for line in data]
	return d

inpt = load()

select_scores_ = {"X": 1, "Y": 2, "Z": 3}
round_scores_ = {"X": {"A": 3, "B": 0, "C": 6}, "Y": {"A": 6, "B": 3, "C": 0}, "Z": {"A": 0, "B": 6, "C": 3}}

def part1(inpt):
    _total = 0
    for rps_round in inpt:
        _opp, _you = rps_round.split()
        _score = select_scores_[_you] + round_scores_[_you][_opp]
        _total += _score
    return _total

select_scores_rnd2_ = {"X": 0, "Y": 3, "Z": 6}
round_scores_rnd2_ = {"X": {"A": 3, "B": 1, "C": 2}, "Y": {"A": 1, "B": 2, "C": 3}, "Z": {"A": 2, "B": 3, "C": 1}}

def part2(inpt):
    _total = 0
    for rps_round in inpt:
        _opp, _you = rps_round.split()
        _score = select_scores_rnd2_[_you] + round_scores_rnd2_[_you][_opp]
        _total += _score
    return _total

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')