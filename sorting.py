'''
Dominating operation: compairson of 2 elements
Data size: arr length

W(len) = Θ((len)^2) = A(len)

The algorithm will always do the same ammount of work, no matter how does the input array looks.
'''
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[j], arr[min_index] = arr[min_index], arr[i]

'''
Dominating operation: comparing 2 elements 
Data size: arr length (n) 

W(n) = Θ(n^2) (when the array is sorted inversely)
A(n) = Θ(n^2)
'''
def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key

'''
Dominating operation: compairson of 2 elements or indicies 
Data size: length of S

There are Θ(log2(len)) levels of recursion and on every level every call to merge function 
has Θ(len) complexity.

Summarizing we get:
W(len) = A(len) = Θ(len · log(len))
'''
def merge_sort(S):
    if len(S) <= 1:
        return S  # Base case: already sorted

    mid = len(S) // 2
    left_half = merge_sort(S[:mid])   # Sort left half
    right_half = merge_sort(S[mid:])  # Sort right half

    return merge(left_half, right_half)

'''
Dominating operation: compairson of 2 elements or 2 indicies 
Data size: the size of 2 arrays n = len1 + len2 

W(n) = A(n) = Θ(n)

Space complexity is high, but can be better if linked lists are used 
S(n) = Θ(n) 
'''
def merge(a1, a2):
    i = j = 0
    result = []  # Resulting merged sorted list

    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1

    # Add remaining elements from left half (if any)
    while i < len(a1):
        result.append(a1[i])
        i += 1

    # Add remaining elements from right half (if any)
    while j < len(a2):
        result.append(a2[j])
        j += 1

    return result