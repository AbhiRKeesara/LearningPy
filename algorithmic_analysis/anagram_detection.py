def anagram_solution_1(string1, string2):
    still_ok = True
    if(len(string1) != len(string2)):
        still_ok = False
    
    chars_in_string2 = list(string2)

    string1_char_pos  =0

    while string1_char_pos < len(string1) and still_ok:
        string2_char_pos = 0
        found = False
        while string2_char_pos < len(chars_in_string2) and not found:
            if string1[string1_char_pos] == chars_in_string2[string2_char_pos]:
                found = True
            else :
                string2_char_pos =string2_char_pos +1 

        if found:
            chars_in_string2[string2_char_pos] = None 
        else:
            still_ok = False

        string1_char_pos = string1_char_pos + 1 
    return still_ok

# O(n2) is the execution time for this solution
# print(anagram_solution_1("apple", "pleap"))  # expected: True
# print(anagram_solution_1("abhinay", "yanhiba"))  # expected: True
# print(anagram_solution_1("abcd", "dcda")) # expected: False


def anagram_solution_2(string1, string2):
    char_string1 = list(string1)
    char_string2 = list(string2)

    char_string1.sort()
    char_string2.sort()

    char_pos = 0
    char_matches = True

    while char_pos < len(char_string1) and char_matches:
        if char_string1[char_pos] == char_string2[char_pos]:
            char_pos = char_pos + 1
        else:
            char_matches = False
    return char_matches


# O(n2) is the execution time for this solution
print(anagram_solution_2("apple", "pleap"))  # expected: True
print(anagram_solution_2("abhinay", "yanhiba"))  # expected: True
print(anagram_solution_2("abcd", "dcda")) # expected: False


def anagram_solution_3(string1, string2):
    string1_char_counter = [0] * 26
    string2_char_counter = [0] * 26

    for i in range(len(string1)):
        pos = ord(string1[i]) - ord("a")
        string1_char_counter[pos] = string1_char_counter[pos] + 1
    
    for i in range(len(string2)):
        pos = ord(string2[i]) - ord("a")
        string2_char_counter[pos] = string2_char_counter[pos] + 1

    
    j=0
    still_ok = True

    while j< 26 and still_ok:
        if string1_char_counter[j] == string2_char_counter[j]
            j = j +1 
        else:
            still_ok = False

    return still_ok

# O(n) is the execution time for this solution
print(anagram_solution_3("apple", "pleap"))  # expected: True
print(anagram_solution_3("abhinay", "yanhiba"))  # expected: True
print(anagram_solution_3("abcd", "dcda")) # expected: False