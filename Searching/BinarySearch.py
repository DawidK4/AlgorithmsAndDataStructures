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