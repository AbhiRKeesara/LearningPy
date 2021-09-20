def palindrome_checker(string: str) -> bool:
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return palindrome_checker(string[1:-1])
        else:
            return False


def palindrome_checker_one(string: str) -> bool:
    def palindrome_helper(s: str, start: int, end: int) -> bool:
        if start >= end:
            return True
        else:
            if s[start] == s[end]:
                return palindrome_helper(s, start + 1, end + 1)
            else:
                return False

    return palindrome_helper(string, 0, len(string) - 1)


if __name__ == "__main__":
    str1: str = "kayak"
    str2: str = "aibohphobia"

    print(palindrome_checker(str1))
    print(palindrome_checker(str2))
    print(palindrome_checker_one(str1))
    print(palindrome_checker_one(str2))
