from typing import List, Dict

with open("part_1_input.txt") as f:
    input_lines = f.read().split("\n")


def clean_string(input_string: str):
    return input_string.lstrip().rstrip()


def parse_input(data: List[str]) -> Dict[str, Dict[str, int]]:
    # Example input: light red bags contain 1 bright white bag, 2 muted yellow bags.
    result = {}
    for input_line in data:
        # We'll get ["light red", "bags contain 1 bright white bag, 2 muted yellow bags."]
        bag_color, remains = [clean_string(word) for word in input_line.split("bags contain")]

        # ['1 bright white bag', '2 muted yellow bags.']
        contains_bags = [clean_string(word) for word in remains.split(",")]

        contains_dict = {}
        for bag in contains_bags:
            # bag will be in format '1 bright white bag' with optional . at end
            # or in format "no other bags"
            try:
                # if no error bag will be in format '1 bright white bag' with optional . at end
                how_many = int(bag[0])
                # We want to remove the bag part, only want color
                bag_index = bag.index("bag")
                what_color = clean_string(bag[1:bag_index])
                contains_dict[what_color] = how_many
            except ValueError:
                # bag will be in format 'no other bags'
                continue

        result[bag_color] = contains_dict

    return result


bag_rules = parse_input(input_lines)


def can_bag_contain_bag(container_bag: str, starting_bag: str) -> bool:
    if starting_bag in bag_rules[container_bag]:
        return True

    for possible_container_bag in bag_rules[container_bag]:
        # don't return recursion result because you'll halt it sooner
        if can_bag_contain_bag(possible_container_bag, starting_bag):
            return True

    return False


if __name__ == "__main__":
    print(sum([can_bag_contain_bag(bag_color, "shiny gold") for bag_color in bag_rules]))