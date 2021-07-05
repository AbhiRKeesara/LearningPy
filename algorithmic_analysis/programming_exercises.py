import matplotlib.pyplot as plt
from timeit import Timer
import random
import pandas as pd


#Q-1: Devise an experiment to verify that the list index operator is O(1) #######
# for i in range(1_000_000, 100_000_001, 1_000_000):
#     t= Timer("x[random.randrange(%d) in x]"%i,
#                     "from __main__ import random,x")
#     x= list(range(i))
#     lst_time = t.timeit(number=1000)
#     print(f"{i:<10d}{lst_time:>15.5f}")

#ValueError: x and y must have same first dimension, but have shapes (10000001,) and (10,)
#sol- https://stackoverflow.com/questions/26690480/matplotlib-valueerror-x-and-y-must-have-same-first-dimension
#try displaying results on a plot


#Q-2: Devise an experiment to verify that get item and set item are 𝑂(1) for dictionaries. ####

# for i in range(1_000_000, 100_000_001, 1_000_00):
#     t = Timer("x[random.randrange(%d) in x]"%i, "from __main__ import random,x")
#     x = {j: "Aloha" for j in range(i)}
#     dict_time = t.timeit(number=1000)
#     print(f"{i:<10d}{dict_time:>15.5f}")


#Q-3: Devise an experiment that compares the performance of the del operator on lists and dictionaries.#####

#we are trying to show that is delete operation 
# - on list is O(n)
# - on dictionary is O(1)

# del_operation_dict_times = {}
# del_operation_list_times = {}
# sizes = range(1_000_000, 100_000_001, 1_000_0)

# def del_dict_items(x):
#     random_index = random.randrange(len(x)-1)
#     try:
#         del x[random_index]
#     except KeyError:
#         x.setdefault(random_index, None)
#         del x[random_index]

# def del_list_items(x):
#     if(len(x)==1):
#         random_index = random.randrange(len(x))
#     else:
#         random_index = random.randrange(len(x)-1)
#     del x[random_index]

# for size in sizes:
#     t_list = Timer("del_list_items(x)", "from __main__ import random, x, del_list_items")
#     t_dict = Timer("del_dict_items(x)", "from __main__ import random, x,del_dict_items")
#     x  = list(range(size))
#     del_operation_list_times[size] = t_list.timeit(number=1000)
#     x= {j:"Aloha" for j in range(size)}
#     del_operation_dict_times[size] = t_dict.timeit(number=1000)

# df = pd.DataFrame({"size": sizes, "dict_times": list(del_operation_dict_times.values()),
#                     "list_times": list(del_operation_list_times.values())})

# #plotting a line graph
# print("Line graph:")
# plt.plot(df["size"], df["list_times"], 'g')
# plt.plot(df["size"], df["dict_times"], 'b')
# plt.show()

#Q-4: Given a list of numbers in random order, write an algorithm that works in 𝑂(𝑛log(𝑛)) to 
# find the kth smallest number in the list.

# sizes = range(10_000, 100_001, 10_000)
# smallest_number_search_times = {}

# def smallest_number_search(x):
#     if(len(x)==1):
#         k_smallest_element = random.randrange(len(x))
#     else:
#         k_smallest_element = random.randrange(len(x)-1)
#     x.sort()
#     x[k_smallest_element]

# for size in sizes:
#     t_list = Timer("smallest_number_search(x)", "from __main__  import random, x, smallest_number_search")
#     x  = list(range(size))
#     random.shuffle(x)
#     smallest_number_search_times[size] = t_list.timeit(number=1000)

# df = pd.DataFrame({"size": sizes,"list_times": list(smallest_number_search_times.values())})

# #plotting a line graph
# print("Line graph:")
# plt.plot(df["size"], df["list_times"], 'g')
# plt.show()

#TODO: solve this question later
#Q-5 Can you improve the algorithm from the previous problem to be linear? Explain.
