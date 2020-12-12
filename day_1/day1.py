GOAL_SUM = 2020

with open("input.txt") as f:
    data = list(map(int, f.read().split("\n")))


# Part 1
for first_index in range(len(data)):
    for second_index in range(first_index, len(data)):
        if data[first_index] + data[second_index] == GOAL_SUM:
            print(data[first_index] * data[second_index])


# Part 2
for first_index in range(len(data)):
    for second_index in range(first_index, len(data)):
        for third_index in range(second_index, len(data)):
            if data[first_index] + data[second_index] + data[third_index] == GOAL_SUM:
                print(data[first_index] * data[second_index] * data[third_index])


# My comment: good for big O , bad for DRY
