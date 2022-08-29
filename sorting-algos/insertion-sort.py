#!/usr/bin/python3

#Insertion Sort is not a fast sorting algorithm because it uses nested loops to sort.
#It is useful only for small data sets
#It runs in O(n²)

def insertion_sortf(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):              #Using For Loop
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
 
def insertion_sortw(A):
   for i in range(1, len(A)):
       j = i
       while A[j-1] > A[j] and j > 0:              #Using While Loop
           A[j-1], A[j] = A[j], A[j-1]
           j -= 1


if __name__ == '__main__':
    arr = [5, 4, 4356, 3, 18, 90, 100, 299, 554]
    # insertion_sortf(arr)
    # print(arr)
    insertion_sortw(arr)
    print(arr)