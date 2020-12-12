from day_7 import part_1


"""def can_bag_contain_bag(container_bag: str, starting_bag: str) -> bool:
    if starting_bag in bag_rules[container_bag]:
        return True

    for possible_container_bag in bag_rules[container_bag].keys():
        # don't return recursion result because you'll halt it sooner
        if can_bag_contain_bag(possible_container_bag, starting_bag):
            return True

    return False"""


def how_many_bags_does_bag_contain(starting_bag: str, start_sum: int = 0) -> int:
    for container_bag, bag_count in part_1.bag_rules[starting_bag].items():
        for _ in range(bag_count):
            start_sum = how_many_bags_does_bag_contain(container_bag, start_sum + 1)

    return start_sum


if __name__ == "__main__":
    print(how_many_bags_does_bag_contain("shiny gold"))
