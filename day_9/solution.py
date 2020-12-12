with open("input.txt") as f:
    numbers = tuple(int(number) for number in f.read().split("\n"))


preamble_size = 25


def solve_one() -> int:
    for index in range(preamble_size, len(numbers)):
        is_valid = False
        for i in range(index, index-preamble_size-1, -1):
            for j in range(index, index-preamble_size-1, -1):
                if numbers[i] + numbers[j] == numbers[index]:
                    is_valid = True
                    break

            if is_valid:
                break

        if not is_valid:
            return numbers[index]


def solve_two(wanted_sum: int) -> int:
    for i in range(len(numbers)):
        temp = []
        for j in range(i, len(numbers)):
            temp.append(numbers[j])
            sum_temp = sum(temp)
            if sum_temp > wanted_sum:
                break
            elif sum_temp == wanted_sum:
                return min(temp) + max(temp)


solution_one = solve_one()
print(solution_one)
print(solve_two(solution_one))