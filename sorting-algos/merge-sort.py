
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


