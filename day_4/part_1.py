with open("input.txt") as f:
    data = f.read()


def format_data(loaded_data: str) -> dict:
    clean_passwords = (password.replace("\n", " ") for password in loaded_data.split("\n\n"))
    passwords_entries = (password.split() for password in clean_passwords)
    passwords_dict = {}
    for index, entry in enumerate(passwords_entries):
        passwords_dict[index] = {}
        for key_value in entry:
            key, value = key_value.split(":")
            passwords_dict[index][key] = value

    return passwords_dict


def password_has_required_fields(_password_data: dict) -> bool:
    required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    return all(required in _password_data for required in required_keys)


if __name__ == "__main__":
    valid_counter = 0
    for password_num, password_data in format_data(data).items():
        if password_has_required_fields(password_data):
            valid_counter += 1

    print(valid_counter)
