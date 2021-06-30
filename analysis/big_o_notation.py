# Problem Statement- Write two Python functions to find the minimum number in a list.
# The first function should compare each number to every other number on the list. O(n2).
# The second function should be linear O(n)

# Example list - [5,4,2,1,0]

from random import randrange
import time


def find_minimum_n2(alist):
    overall_min = alist[0]

    for i in alist:
        is_smallest = True
        for j in alist:
            if i > j:
                is_smallest = False
                break
        if is_smallest:
            overall_min = i

    return overall_min


def find_minimum_n(alist):
    min_so_far = alist[0]

    for i in alist:
        if i < min_so_far:
            min_so_far = i

    return min_so_far


# print(find_minimum_n([5, 4, 1, 1, 0]))
# print(find_minimum_n2([5, 4, -1, 10, 1]))


for list_size in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(list_size)]
    start = time.time()
    print(find_minimum_n2(alist))
    end = time.time()
    print("size: %d time: %f" % (list_size, end - start))

for list_size in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(list_size)]
    start = time.time()
    print(find_minimum_n(alist))
    end = time.time()
    print("size: %d time: %f" % (list_size, end - start))
