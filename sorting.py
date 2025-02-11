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