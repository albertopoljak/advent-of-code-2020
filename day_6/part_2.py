from collections import defaultdict


with open("input.txt") as f:
    groups = f.read().split("\n\n")


answer_counter = defaultdict(lambda: 0)


for group in groups:
    group_answers = list(set(answer) for answer in group.split("\n"))
    common_items = set.intersection(*group_answers)
    for item in common_items:
        answer_counter[item] += 1


print(sum(answer_counter.values()))
