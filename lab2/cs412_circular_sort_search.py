"""
    name: Colin Finnegan

"""


def binarySearch(arr, low, high, key):
    if high < low:
        return -1

    mid = (low + high) // 2

    if key == arr[mid]:
        return mid

    if arr[low] <= arr[mid]:
        if arr[low] <= key <= arr[mid]:
            return binarySearch(arr, low, mid - 1, key)
        else:
            return binarySearch(arr, mid + 1, high, key)
    else:
        if arr[mid] <= key <= arr[high]:
            return binarySearch(arr, mid + 1, high, key)
        else:
            return binarySearch(arr, low, mid - 1, key)


def main():
    circular = [int(s) for s in input().split()]
    number = int(input())
    print(binarySearch(circular, 0, len(circular) - 1, number))


if __name__ == "__main__":
    main()