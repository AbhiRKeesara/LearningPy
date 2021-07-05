from timeit import Timer

#creating a list with concatenation
def test1():
    a_list = []
    for i in range(1000):
        a_list = a_list + [i]

#creating a list with append
def test2():
    a_list=[]
    for i in range(1000):
        a_list.append(i)

#creating a list with list comprehension
def test3():
    a_list = [i for i in range(1000)]

#creating a list - range function wrapped by a call to list constructor
def test4():
    a_list = list(range(1000))

# t1 = Timer("test1()", "from __main__ import test1")
# print(f"concatenation: {t1.timeit(number=1000):15.2f} milliseconds")

# t2= Timer("test2()", "from __main__ import test2")
# print(f"appending: {t2.timeit(number=1000):19.2f} milliseconds")

# t3 =Timer("test3()", "from __main__ import test3")
# print(f"list comprehension: {t3.timeit(number=1000):10.2f} milliseconds")

# t4 =Timer("test4()", "from __main__ import test4")
# print(f"list constructor: {t4.timeit(number=1000):18.2f} milliseconds")


# difference between pop(), pop(i)

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

# x = list(range(2000000))
# print(f"pop(0): {pop_zero.timeit(number=1000):10.5f} milliseconds")

# x= list(range(2000000))
# print(f"pop(): {pop_end.timeit(number=1000):11.5f} milliseconds")

print(f"{'n':10s}{'pop(0)':>15s}{'pop()':>15s}")

for i in range(1_000_000, 100_000_001, 1_000_000):
    x = list(range(i))
    pop_zero_t = pop_zero.timeit(number=1000)
    x = list(range(i))
    pop_end_t = pop_end.timeit(number=1000)
    print(f"{i:<10d}{pop_zero_t:>15.5f}{pop_end_t:>15.5f}")
