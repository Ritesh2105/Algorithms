data = [1, 7, 2, 3, 4, 9, 34, 7, 17, 87, 79, 74, 97]
target = 87


# linear search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return print(True)
    return print(False)


# binary_search_iterative
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return print(True)
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1


# binary search recursive
def binary_search_recursive(data, target, low, high):
    if low>high:
        return print(False)
    while low<=high:
        mid = (low+high)//2
        if target == data[mid]:
            return print(True)
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)


if __name__ == '__main__':
    linear_search(data, target)
    binary_search_iterative(data, target)
    binary_search_recursive(data, target, 0, len(data)-1)
