import random, math

def load(filename):
    with open(filename) as file:
        data = [line for line in file.readlines()]
        index = data.index('\n')
        _stack, _operations = data[:index], data[index+1:]
    return _stack, _operations

eg_inpt_stack, eg_inpt_operations = load('day05Example.txt')
que_inpt_stack, que_inpt_operations = load('day05Input.txt')

def part1(inpt, operations):
    stacks_ = {}
    for crates_ in inpt[:-1]:
        for stack_no_, supply_ in enumerate(crates_[1::4]):
            if supply_ == " ":
                continue
            current_stack_ = len(stacks_)
            while current_stack_ <= stack_no_:
                stacks_[current_stack_] = []
                current_stack_ += 1
            stacks_[stack_no_].insert(0, supply_)
    tops_ = ""
    cnt = 0
    for stack_ in stacks_:
        stacks_[cnt].reverse()
        cnt += 1
    for operation_ in operations:
        operation_ = operation_.replace("move", "").replace(" from ", ":").replace(" to ", ":")
        cnt_, src_, tgt_ = map(int, operation_.split(":"))
        move_ = stacks_[src_-1][:cnt_]
        for element_ in move_:
            stacks_[tgt_-1].insert(0, element_)
        stacks_[src_-1] = stacks_[src_-1][cnt_:]
    cnt = 0
    for top_ in stacks_:
        if stacks_[cnt][0]:
            tops_ += stacks_[cnt][0]
        else: 
            tops_ = " "
        cnt += 1
    return tops_

def part2(inpt, operations):
    stacks_ = {}
    for crates_ in inpt[:-1]:
        for stack_no_, supply_ in enumerate(crates_[1::4]):
            if supply_ == " ":
                continue
            current_stack_ = len(stacks_)
            while current_stack_ <= stack_no_:
                stacks_[current_stack_] = []
                current_stack_ += 1
            stacks_[stack_no_].insert(0, supply_)
    tops_ = ""
    cnt = 0
    for stack_ in stacks_:
        stacks_[cnt].reverse()
        cnt += 1
    for operation_ in operations:
        operation_ = operation_.replace("move", "").replace(" from ", ":").replace(" to ", ":")
        cnt_, src_, tgt_ = map(int, operation_.split(":"))
        move_ = stacks_[src_-1][:cnt_]
        move_.reverse()
        for element_ in move_:
            stacks_[tgt_-1].insert(0, element_)
        stacks_[src_-1] = stacks_[src_-1][cnt_:]
    cnt = 0
    for top_ in stacks_:
        if stacks_[cnt][0]:
            tops_ += stacks_[cnt][0]
        else: 
            tops_ = " "
        cnt += 1
    return tops_

print(f'EXAMPLE\nPart1: {part1(eg_inpt_stack, eg_inpt_operations)}\nPart2: {part2(eg_inpt_stack, eg_inpt_operations)}')
print(f'PROBLEM\nPart1: {part1(que_inpt_stack, que_inpt_operations)}\nPart2: {part2(que_inpt_stack, que_inpt_operations)}')