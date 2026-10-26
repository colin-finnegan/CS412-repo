"""
    name: Colin Finnegan

"""


def mergesort(A):
    if len(A) > 1:
        m = len(A) // 2

        left, right = A[:m], A[m:]

        inv_left = mergesort(left)
        inv_right = mergesort(right)

        inv_merge = merge(A, left, right)

        return inv_left + inv_right + inv_merge
    return 0


def merge(A, left, right):
    i = j = k = 0
    inversions = 0
    nL, nR = len(left), len(right)
    
    while i < nL and j < nR:
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            inversions += nL - i 
            j += 1
        k += 1

    while i < nL:
        A[k] = left[i]
        i += 1
        k += 1
    while j < nR:
        A[k] = right[j]
        j += 1
        k += 1

    return inversions


def main():
    A = [int(s) for s in input().split(" ")]
    print(mergesort(A))


if __name__ == "__main__":
    main()