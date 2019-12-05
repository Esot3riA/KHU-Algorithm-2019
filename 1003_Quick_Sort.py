def quick_sort(s, low, high):
    if high > low:
        pivot_point = partition(s, low, high)
        quick_sort(s, low, pivot_point-1)
        quick_sort(s, pivot_point+1, high)
    return s


def partition(s, low, high):
    pivot_item = s[low]
    j = low
    for i in range(low+1, high+1):
        if s[i] < pivot_item:
            j += 1
            s[i], s[j] = s[j], s[i]
    pivot_point = j
    s[low], s[pivot_point] = s[pivot_point], s[low]
    return pivot_point


arr = [3, 5, 2, 9, 10, 14, 4, 8]
quick_sort(arr, 0, 7)
print(arr)
