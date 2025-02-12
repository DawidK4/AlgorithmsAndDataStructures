import searching
import sorting
import random as rd 

a = []
num = rd.randint(5, 10)
for i in range(num):
    a.append(rd.randint(0, 10))
key = 20

# searching.binary_search(arr=a, k=key)

# sorting.selection_sort(a)

sorting.insertion_sort(a)