

#Selection Sort is not a fast sorting algorithm,
#because it uses nested loops to sort.

#It is useful only for small data sets.
#It runs in O(n²) Quadratic running time


def selection_sort(A):
    for i in range(0, len(A) -1):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[i]:
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]               #swap


if __name__ == '__main__':
    arr = [2, 6, 7, 3, 9, 8, 50]
    selection_sort(arr)
    print(arr)