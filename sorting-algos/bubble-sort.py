
def bubble_sort(A):
    sorted = False
    while not sorted:
        sorted = True
        for j in range(0, len(A) - 1):
            if A[j] > A[j+1]:
                sorted = False
                A[j], A[j+1] = A[j+1], A[j]


if __name__ == '__main__':
    arr = [2, 5, 3, 6, 7, 4, 9]
    bubble_sort(arr)
    print(arr)