from typing import Tuple, List


input_data_type = List[Tuple[str, int]]


class BootCode:
    def __init__(self):
        self._accumulator = 0

    @classmethod
    def load_data(cls):
        with open("input.txt") as f:
            return [cls.parse_instruction(line) for line in f.read().split("\n")]

    @classmethod
    def parse_instruction(cls, instruction: str) -> Tuple[str, int]:
        operation, argument = instruction.split()
        return operation, int(argument)

    def execute(self, lines: input_data_type):
        visited_indexes = set()
        index = 0

        while True:
            if index in visited_indexes:
                return index, self._accumulator
            elif index == len(lines):
                return index, self._accumulator
            else:
                visited_indexes.add(index)

            operation, argument = lines[index]

            if operation == "acc":
                self._accumulator += argument
                index += 1
            elif operation == "jmp":
                index += argument
            else:
                index += 1

    @classmethod
    def _swap(cls, input_list: input_data_type, index: int, n_1: str, n_2: str):
        """Returns whether swap happened or not"""
        operation, argument = input_list[index]
        if operation == n_1:
            input_list[index] = n_2, argument
        elif operation == n_2:
            input_list[index] = n_1, argument

    def _is_valid_fix(self, lines: input_data_type) -> bool:
        index, _ = self.execute(lines)
        return index == len(lines)

    def fix(self, lines: input_data_type):
        corrupted_instructions = ("nop", "jmp")
        corrupted_indexes = []

        for index in range(len(lines)):
            operation, argument = lines[index]
            if operation in corrupted_instructions:
                corrupted_indexes.append(index)

        for corrupted_index in corrupted_indexes:
            self._accumulator = 0
            self._swap(lines, corrupted_index, *corrupted_instructions)

            if self._is_valid_fix(lines):
                return self._accumulator
            else:
                # swap back to original state as it did not fix it
                self._swap(lines, corrupted_index, *corrupted_instructions)


boot_code = BootCode()
data = boot_code.load_data()
assert(boot_code.execute(data)[1] == 1420)
print("Found corrupted, accumulator is", boot_code.fix(data))

