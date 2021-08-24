#import the tools file so we can use swap
from tools import *

#define a function called selection_sort that takes a list of items
def selection_sort(items):
    # make a copy of the list so we don't destroy the original data
    # because lists (like items) pass by reference
    ordered = items.copy()

    # sort the copy using the Selection Sort algorithm
    
    # YOUR CODE GOES HERE
    #walk through the list
    for i in range(len(ordered)):
        #store a current smallest position (index value)
        smallest = -1
        #walk through the unsorted portion
        for j in range(i, len(ordered)):
            if ordered[j] < ordered[smallest]:
                smallest = j;
        swap(ordered, smallest, i)


        #is there anything smaller than our current smallest thing
        #update the value of current smallest
        #swap out the elements
        
    return ordered



#main
print(selection_sort([3,1,7,2,6,5,0,4]))

# NOTE TO STUDENTS
# If you're having a trouble understanding the algorithm, check out this link:
# https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm
# You need to implement the solution yourself, however.
