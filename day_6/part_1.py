from collections import defaultdict


with open("input.txt") as f:
    groups = f.read().split("\n\n")


answer_counter = defaultdict(lambda: 0)


for group in groups:
    clean_group = "".join(set(group.replace("\n", "")))
    for char in clean_group:
        answer_counter[char] += 1


print(sum(answer_counter.values()))
