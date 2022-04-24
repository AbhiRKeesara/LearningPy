def to_str(number, base):
    convert_to_string = "0123456789ABCDEF"
    if number < base:
        return convert_to_string[number]
    else:
        return to_str(number // base, base) + convert_to_string[number % base]


if __name__ == "__main__":
    print(to_str(10, 2))
