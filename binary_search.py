
def binary_search(arr, target):
    return binary_search_helper(arr, 0, len(arr), target)

def binary_search_helper(arr, start_idx, end_idx, target):
    middle_idx = (end_idx + start_idx) / 2
    if arr[middle_idx] == target:
        return middle_idx
    if start_idx == end_idx:
        return -1
    elif arr[middle_idx] < target:
        return binary_search_helper(arr, middle_idx + 1, end_idx, target)
    else:
        return binary_search_helper(arr, start_idx, middle_idx - 1, target)

numbers = [2, 8, 19, 31, 86, 125, 360, 450, 600, 749, 890, 999, 1234, 1423]
n = 360
idx = binary_search(numbers, n)
print "%d was found in index %r" % (n, idx)
