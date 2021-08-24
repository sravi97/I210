def evenrow(lst):
#checking if every number in the list has a remainder
    for i in lst:
        if sum(i) % 2 == 1:
            return False
#if there is not a remainder print True
    else:
        return True
    
print(evenrow([[1, 3], [2, 4], [0, 6]]))
