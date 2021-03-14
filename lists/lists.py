# Lists: ordered, mutable, allows duplicate elements
myList = ["1","0","-1","banana","cheery","apple"]
# print(myList)

#create a empty list
# myList2 = list()
# print(myList2)

#add different type of data types and duplicate elements
# duplicateList = list()
# duplicateList=["5",5,"apple"]
# print(duplicateList)

#acess the elements
#item=myList[0]
# print(item)
#access with negative index
# item1=myList[-1]
# print(item1)
#index error : list index out of range
# item2=myList[3]
# print(item2)

#iterate over the list
# for item in myList:
#     print(item)

#check if a item exist in list
# if "banana" in myList:
#     print("yes")
# else:
#     print("no")

# number of elements inside list 
# print(len(myList))

#append elements to list 
myList.append("lemon")
print(myList)

#insert at a specific location/index
myList.insert(1,"blueberry")
print(myList)

#remove elements 
# item = myList.pop()
# print(item)
# print(myList)

#remove specific elements from list 
# item=myList.remove("cheery")
# print(item)

#remove element not in list, ValueError: list.remove(x): x not in list
# item=myList.remove("cheery")
# print(item)

#remove all elements from list
# item= myList.clear()
# print(myList)

#reverse a list
# myList.reverse()
# print(myList)

#sort original list
# myList.sort()
# print(myList)

#sort and create a new list 
# new_list = sorted(myList)
# print(new_list)
# #original list
# print(myList)

#create a list with same element
myNewList = [0]*5
print(myNewList)

#concatenate
myList2=[1,2,3,4]
print(myNewList + myList2)