def reverse_string(string: str) -> str:
    def helper(s: str, end: int) -> str:
        if end < 0:
            return ""
        else:
            return s[end] + helper(s, end - 1)

    return helper(string, len(string) - 1)


def reverse_string_one(string: str) -> str:
    if len(string) == 0:
        return ""
    else:
        return reverse_string_one(string[1:]) + string[0]


def reverse_string_two(string: str) -> str:
    if len(string) == 0:
        return ""
    else:
        return string[len(string) - 1] + reverse_string_two(string[0:len(string) - 1])


if __name__ == "__main__":
    strings: str = "This string will be reversed"
    print(reverse_string(strings))
    print(reverse_string_one(strings))
    print(reverse_string_two(strings))
