"""Same principle as first part but with different data type.
Now it's not a list of chars but a dict like dict[row_index][col_index] with chars.
A bit uglier creating initial data but a bit faster to work with. """

with open("input.txt") as f:
    plane = {}
    number_of_rows = 0
    number_of_cols = 0
    for row_i, line in enumerate(f.read().split("\n")):
        plane[row_i] = {}
        number_of_rows += 1
        for col_i, char in enumerate(line):
            plane[row_i][col_i] = char
            if number_of_rows == 1:
                number_of_cols += 1

ROTATIONS = [
    (-1, -1), (-1,  0), (-1,  1),
    ( 0, -1),           ( 0,  1),
    ( 1, -1), ( 1,  0), ( 1,  1)
]

FLOOR = "."
SEAT_EMPTY = "L"
SEAT_OCCUPIED = "#"


def number_of_surrounding_seats(row: int, col: int, *, max_count: int) -> int:
    """max_count: for speed, do not check further if we get to this number of surrounding seats."""
    count = 0

    for relative_location in ROTATIONS:
        surrounding_row, surrounding_col = (row + relative_location[0], col + relative_location[1])
        while True:
            try:
                if plane[surrounding_row][surrounding_col] == SEAT_OCCUPIED:
                    count += 1
                    if count == max_count:
                        return count
                    break
                elif plane[surrounding_row][surrounding_col] == SEAT_EMPTY:
                    break
                surrounding_row, surrounding_col = (surrounding_row + relative_location[0], surrounding_col + relative_location[1])
            except KeyError:
                break

    return count


def seat_passengers():
    # list of (row_index, col_index, what_to_change_to)
    to_change = []
    for row_index in range(number_of_rows):
        for col_index in range(number_of_cols):
            if plane[row_index][col_index] == FLOOR:
                continue
            elif plane[row_index][col_index] == SEAT_EMPTY:
                if number_of_surrounding_seats(row_index, col_index, max_count=1) == 0:
                    to_change.append((row_index, col_index, SEAT_OCCUPIED))
            else:
                # Seat is occupied
                if number_of_surrounding_seats(row_index, col_index, max_count=5) == 5:
                    to_change.append((row_index, col_index, SEAT_EMPTY))

    # Update the plane
    for change in to_change:
        plane[change[0]][change[1]] = change[2]

    return len(to_change) > 0


while True:
    if not seat_passengers():
        break


occupied_seats = 0
for row in plane.values():
    for char in row.values():
        if char == SEAT_OCCUPIED:
            occupied_seats += 1

print(occupied_seats)
