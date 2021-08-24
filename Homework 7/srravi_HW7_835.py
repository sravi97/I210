#implement class Stack that has a subclass of object
class Stack(object):
    
    #defining constructor
    def __init__(self):
        #create a list to store the values
        self.items = []

    #function that will return the length of the stack
    def __len__(self):
        return len(self.items)

    #the function that will insert an element in the stack
    def push(self, item):
        #appends the items in the stack to the items list
        self.items.append(item)

    #remove and return the item at the top of the stack
    def pop(self):
        return self.items.pop()

    #function to check if the stack is empty or not    
    def isEmpty(self):
        #check the length of the stack and return True if the stack is empty
        if (len(self.items) == 0):
            return True
        #False otherwise 
        else:
            return False
        
    #function to display the stack
    def __repr__(self):
        return str(self.items)
    

