def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum


def list_sum_recursive(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_recursive(num_list[1:])


if __name__ == "__main__":
    print(list_sum([1, 3, 5, 7, 9]))
    print(list_sum_recursive([1, 3, 5, 7, 9]))
