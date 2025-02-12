def binary_search(arr: list[int], k: int) -> int:
    l, r = 0, len(arr) - 1  # Fix: r should be len(arr) - 1

    print("Initialization:")
    print(f"l: {l}, r: {r}, len: {len(arr)}")  # Fix: Proper string formatting
    print(arr)

    while l <= r:  # Fix: Keep within bounds
        m = (l + r) // 2
        print(f"m: (l + r) // 2 = {m}")

        if arr[m] > k:
            r = m - 1
            print(f"arr[m] > k => r = m - 1: {r}")
        elif arr[m] < k:
            l = m + 1
            print(f"arr[m] < k => l = m + 1: {l}")
        else:
            return m

        print(arr)
        print("--------------")
    
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