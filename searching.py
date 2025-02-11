def binary_search(arr: list[int], k: int) -> int:
    l, r = 0, len(arr)

    while (l <= r):
        m = (l + r) // 2

        if arr[m] > k:
            r = m - 1
        elif arr[m] < k:
            l = m + 1
        else:
            return m
        
    return -1 

def k_jump_search(arr: list[int], k: int, target: int) -> int:
    n = len(arr)

    prev = 0
    while arr[min(k, n) - 1] < target:
        prev = k 
        k += k
        if prev >= n:
            return -1 
        
    for i in range(prev, min(k, n)):
        if arr[i] == target:
            return i 
        
    return -1 