with open("input.txt") as f:
    plane = tuple(list(line) for line in f.read().split("\n"))


ROTATIONS = [
    (-1, -1), (-1,  0), (-1,  1),
    ( 0, -1),           ( 0,  1),
    ( 1, -1), ( 1,  0), ( 1,  1)
]

FLOOR = "."
SEAT_EMPTY = "L"
SEAT_OCCUPIED = "#"

number_of_rows = len(plane)
number_of_cols = len(plane[0])


def number_of_surrounding_seats(row: int, col: int, *, max_count: int) -> int:
    """max_count: for speed, do not check further if we get to this number of surrounding seats."""
    count = 0

    for relative_location in ROTATIONS:
        try:
            surrounding_row, surrounding_col = (row + relative_location[0], col + relative_location[1])
            # it can go backward ree
            if surrounding_row < 0 or surrounding_col < 0:
                continue
            if plane[surrounding_row][surrounding_col] == SEAT_OCCUPIED:
                count += 1
                if count == max_count:
                    return count

        except IndexError:
            continue

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
                if number_of_surrounding_seats(row_index, col_index, max_count=4) == 4:
                    to_change.append((row_index, col_index, SEAT_EMPTY))

    # Update the plane
    for change in to_change:
        plane[change[0]][change[1]] = change[2]

    return len(to_change) > 0


while True:
    if not seat_passengers():
        break


occupied_seats = 0
for line in plane:
    for char in line:
        if char == SEAT_OCCUPIED:
            occupied_seats += 1

print(occupied_seats)
