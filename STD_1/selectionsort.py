'''SELECTION SORT
   input: unsorted array
   output: sorted array
   Implements selection sort with direct swap
'''
def selection_sort(A):
    for i in range (len(A)-1):      #Loops over every value/element in unsorted array A
        min = i                     #stores the index of the current value as minimum value
        for j in range(i+1, len(A)):#Loops over every value in A except the current value
            if A[j] < A[min]:       #if the next value (value of index j) < current min value 
                min = j             #store the index of next value as the minimum ELSE go to next value in array
        A[i] , A[min] = A[min], A[i]#directly swap the current value with the new minimum value 
    return A

unsorted_array = [11,22,14,67,2,9]

print(selection_sort(unsorted_array))