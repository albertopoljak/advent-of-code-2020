from typing import Tuple, Any, Sequence


class CyclicIndex:
    __slots__ = ("_iterable_ref",)

    def __init__(self, iterable: Sequence):
        self._iterable_ref = iterable

    def __getitem__(self, index: int) -> Any:
        cyclic_index = index % len(self._iterable_ref)
        return self._iterable_ref[cyclic_index]


with open("part_1_input.txt") as f:
    lines = tuple(CyclicIndex(line) for line in f.read().split("\n"))


class SlopeMap:
    OPEN_SPACE = "."
    TREE = "#"

    @classmethod
    def get_tree_obstacle_count(cls, slope_map: Tuple[CyclicIndex, ...], slope_right: int, slope_down: int) -> int:
        tree_counter = 0
        skipped_y = 0

        if slope_down < 1:
            raise ValueError("Invalid slope down value.")

        for line_index, line in enumerate(slope_map):
            if line_index % slope_down != 0:
                skipped_y += 1
                continue

            if line[line_index * slope_right - skipped_y] == cls.TREE:
                tree_counter += 1

        return tree_counter


# Part 1
part_1__1_3 = SlopeMap.get_tree_obstacle_count(lines, 3, 1)
print(part_1__1_3)

# Part 2
part_2__1_1 = SlopeMap.get_tree_obstacle_count(lines, 1, 1)
part_2__5_1 = SlopeMap.get_tree_obstacle_count(lines, 5, 1)
part_2__7_1 = SlopeMap.get_tree_obstacle_count(lines, 7, 1)
part_2__1_2 = SlopeMap.get_tree_obstacle_count(lines, 1, 2)
print(part_2__1_1 * part_1__1_3 * part_2__5_1 * part_2__7_1 * part_2__1_2)
