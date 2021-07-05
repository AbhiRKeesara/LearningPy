#Q-1 : Give the Big-O performance of the following code fragment:
for i in range(n):
   for j in range(n):
      k = 2 + 2
#Ans: O(n2)

#Q-2 : Give the Big-O performance of the following code fragment:
for i in range(n):
     k = 2 + 2
#Ans: O(n)

#Q-3 : Give the Big-O performance of the following code fragment:
i = n
while i > 0:
   k = 2 + 2
   i = i // 2
#Ans: O(n logn)

#Q-4 : Give the Big-O performance of the following code fragment:
for i in range(n):
   for j in range(n):
      for k in range(n):
         k = 2 + 2
#Ans: O(n3)

#Q-5 : Give the Big-O performance of the following code fragment:
for i in range(n):
   k = 2 + 2
for j in range(n):
   k = 2 + 2
for k in range(n):
   k = 2 + 2
#Ans: O(n)