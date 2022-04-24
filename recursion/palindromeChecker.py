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
                return palindrome_helper(s, start + 1, end - 1)
            else:
                return False

    return palindrome_helper(string, 0, len(string) - 1)


def remove_white(s):
    return ''.join(e for e in s if e.isalnum())

if __name__ == "__main__":
    str1: str = "kayak"
    str2: str = "aibohphobia"
    str3: str = "madam i'm adam"
    print(palindrome_checker(remove_white(str1)))
    print(palindrome_checker(remove_white(str2)))
    print(palindrome_checker(remove_white(str3)))
    print(palindrome_checker_one(remove_white(str1)))
    print(palindrome_checker_one(remove_white(str2)))
    print(palindrome_checker_one(remove_white(str3)))
