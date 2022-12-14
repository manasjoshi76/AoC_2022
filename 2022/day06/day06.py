import random, math

def load(filename):
	with open(filename) as file:
		data = file.readline()
	return data

inpt_example = load('day06Example.txt')
inpt_problem = load('day06Input.txt')

def part1(inpt):
    for i in range(0, len(inpt)):
        #print(inpt)
        stream_ = inpt[i:i+4]
        #print(stream_)
        if len(set(stream_)) == len(stream_):
            return i+4
    return -1

def part2(inpt):
    for i in range(0, len(inpt)):
        #print(inpt)
        stream_ = inpt[i:i+14]
        #print(stream_)
        if len(set(stream_)) == len(stream_):
            return i+14
    return -1

print(f'EXAMPLE\nPart1: {part1(inpt_example)}\nPart2: {part2(inpt_example)}')
print(f'PROBLEM\nPart1: {part1(inpt_problem)}\nPart2: {part2(inpt_problem)}')