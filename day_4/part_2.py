import re
from typing import Any

from day_4 import part_1


def _is_valid_height(height: str) -> bool:
    if height.endswith("cm"):
        number = height.split("cm")[0]
        minimum, maximum = 150, 193
    elif height.endswith("in"):
        number = height.split("in")[0]
        minimum, maximum = 59, 76
    else:
        return False

    try:
        number = int(number)
    except ValueError:
        return False

    return minimum <= number <= maximum


def is_field_valid(field_key: Any, field_value: Any) -> bool:
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    """
    field_checks = {
        "byr": lambda value: 1920 <= int(value) <= 2002,
        "iyr": lambda value: 2010 <= int(value) <= 2020,
        "eyr": lambda value: 2020 <= int(value) <= 2030,
        "hgt": _is_valid_height,
        "hcl": lambda value: len(value) != 6 and re.match(r"#(\d|[a-f]){6}", value),
        "ecl": lambda value: value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda value: len(value) == 9 and value.isnumeric(),
        "cid": lambda _: True
    }
    return field_checks[field_key](field_value)


valid_counter = 0
for password_num, password_data in part_1.format_data(part_1.data).items():
    if part_1.password_has_required_fields(password_data):
        if all(is_field_valid(field_key, field_value) for field_key, field_value in password_data.items()):
            valid_counter += 1


print(valid_counter)
