from math import log
from typing import Tuple


class Plane:
    SEAT_ROWS = 128
    SEAT_COLUMNS = 8

    @classmethod
    def decode_boarding_pass(cls, boarding_pass: str) -> Tuple[int, int, int]:
        row_index = cls._decode_row_index(boarding_pass)
        col_index = cls._decode_column_index(boarding_pass)
        return row_index, col_index, cls.get_seat_id(row_index, col_index)

    @classmethod
    def _decode_row_index(cls, boarding_pass) -> int:
        row_range = 0, cls.SEAT_ROWS - 1
        for row_region_index in range(int(log(cls.SEAT_ROWS, 2))):
            if boarding_pass[row_region_index] == "F":
                row_range = cls._lower_half(*row_range)
            elif boarding_pass[row_region_index] == "B":
                row_range = cls._upper_half(*row_range)
            else:
                raise ValueError(f"Invalid row region character {repr(boarding_pass[row_region_index])}")

        if row_range[0] != row_range[1]:
            raise ValueError("Invalid boarding pass.")

        return row_range[0]

    @classmethod
    def _decode_column_index(cls, boarding_pass: str) -> int:
        col_range = 0, cls.SEAT_COLUMNS - 1
        iterations = int(log(cls.SEAT_COLUMNS, 2))
        for column_char in boarding_pass[-iterations:]:
            if column_char == "R":
                col_range = cls._upper_half(*col_range)
            elif column_char == "L":
                col_range = cls._lower_half(*col_range)
            else:
                raise ValueError(f"Invalid column region character {repr(column_char)}")

        if col_range[0] != col_range[1]:
            raise ValueError("Invalid boarding pass.")

        return col_range[0]

    @classmethod
    def _lower_half(cls, beginning: int, end: int) -> Tuple[int, int]:
        return beginning, beginning + (end - beginning) // 2

    @classmethod
    def _upper_half(cls, beginning: int, end: int) -> Tuple[int, int]:
        return beginning + (end - beginning + 1) // 2, end

    @classmethod
    def get_seat_id(cls, row_index: int, col_index: int) -> int:
        return row_index * cls.SEAT_COLUMNS + col_index


if __name__ == "__main__":
    with open("input.txt") as f:
        boarding_passes = f.read().split("\n")

    boarding_passes_ids = [Plane.decode_boarding_pass(boarding_pass)[2] for boarding_pass in boarding_passes]

    print(max(boarding_passes_ids))

    # part 2
    boarding_passes_ids.sort()

    for previous, current in zip(boarding_passes_ids, boarding_passes_ids[1:]):
        if current - previous > 1:
            print(previous, current)
            break
