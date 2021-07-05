import time


def sum_of_n(n):
    the_sum = 0

    for i in range(1, n + 1):
        the_sum = the_sum + i

    return the_sum


# function returns a tuple consisting of the result
# and the amount of time ( in secs)
def sum_of_n_2(n):
    """[function returns sum of n numbers]

    Args:
        n ([integer]): [sum of numbers to be added]

    Returns:
        [tuple]: [the result and the amount of time ( in secs) required for calculation]
    """
    start = time.time()

    the_sum = 0

    for i in range(1, n + 1):
        the_sum = the_sum + i
    end = time.time()

    return the_sum, end - start


def sum_of_n_3(n):
    start = time.time()

    the_sum = 0
    the_sum = (n * (n + 1)) / 2
    end = time.time()

    return the_sum, end - start


for i in range(5):
    print("Sum is %d required %10.15f seconds" % sum_of_n_2(10000))
