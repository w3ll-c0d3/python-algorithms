
#MergeSort is recursive (method that calls itself)
#Divide-and-conquer algorithm 
#Very efficient for large data sets

#MergeSort does log n merge steps because each merge step doubles the list size.
#It does n work for each merge step because it must look at every item.
#So it runs in O(n * log(n))

#STEPS:
#1. Split array in half
#2. Call Merge Sort on each half to sort them recursively
#3. Merge both sorted halves into one sorted array

def mergeSort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]
    
        # Recursion
        mergeSort(left_arr)
        mergeSort(right_arr)

        # Merge
        i = 0 # left_arr index
        j = 0 # right_arr index
        k = 0 # merged array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
    
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

if __name__ == '__main__':
    array = [2, 444, 3, 6, 2, 4, 908, 665, 745, 324, 23, 1254, 55]
    mergeSort(array)
    print(array)