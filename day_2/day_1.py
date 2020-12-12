with open("day_1_input.txt") as f:
    # ((min, max), 'char', 'word'), ((min, max), 'char', 'word', ...
    data = tuple(
        (tuple(map(int, entry[0].split("-"))), entry[1].replace(":", ""), entry[2])
        for entry in (line.split() for line in f.read().split("\n"))
    )


# Part 1
print(sum(True for entry in data if entry[0][0] <= entry[2].count(entry[1]) <= entry[0][1]))


# Part 2
print(
    sum(
        True for entry in data if (
            (entry[2][entry[0][0]-1] == entry[1]) != (entry[2][entry[0][1]-1] == entry[1])
        )
    )
)

# My comment: Too simple not to code golf a bit
