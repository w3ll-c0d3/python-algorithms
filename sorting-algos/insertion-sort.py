#!/usr/bin/python3
import sys

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
       while A[j-1] > A[j] and j > 0:               #Using While Loop
           A[j-1], A[j] = A[j], A[j-1]
           j -= 1



if __name__ == '__main__':
    n = sys.stdin.readline().split()
    # insertion_sortf(n)
    # print(n)
    insertion_sortw(n)
    print(n)