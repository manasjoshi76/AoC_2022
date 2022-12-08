import random, math

def load(filename):
    with open(filename) as file:
        data = file.readlines()
        d = [[int(c) for c in line.strip()] for line in data]
    return d

inpt_example = load('day08Example.txt')
inpt_problem = load('day08Input.txt')

def part1(inpt):
    visible_ = 2 * len(inpt) + 2 * (len(inpt) - 2)
    for i in range(1, len(inpt) - 1):
        for j in range(1, len(inpt[0]) - 1):
            if all(inpt[k][j] < inpt[i][j] for k in range(0, i)):
                visible_ += 1
                continue
            if all(inpt[i][k] < inpt[i][j] for k in range(j + 1, len(inpt[i]))):
                visible_ += 1
                continue
            if all(inpt[k][j] < inpt[i][j] for k in range(i + 1, len(inpt))):
                visible_ += 1
                continue
            if all(inpt[i][k] < inpt[i][j] for k in range(0, j)):
                visible_ += 1
                continue
    return visible_


def part2(inpt):
    scenic_ = []
    for i in range(len(inpt)):
        for j in range(len(inpt[0])):
            north_ = 0
            for k in range(i - 1, -1, -1):
                north_ += 1
                if inpt[k][j] >= inpt[i][j]:
                    break
            east_ = 0
            for k in range(j + 1, len(inpt[i])):
                east_ += 1
                if inpt[i][k] >= inpt[i][j]:
                    break
            south_ = 0
            for k in range(i + 1, len(inpt)):
                south_ += 1
                if inpt[k][j] >= inpt[i][j]:
                    break
            west_ = 0
            for k in range(j - 1, -1, -1):
                west_ += 1
                if inpt[i][k] >= inpt[i][j]:
                    break
            scenic_.append(north_ * east_ * south_ * west_)
    return max(scenic_)

print(f'EXAMPLE\nPart1: {part1(inpt_example)}\nPart2: {part2(inpt_example)}')
print(f'PROBLEM\nPart1: {part1(inpt_problem)}\nPart2: {part2(inpt_problem)}')