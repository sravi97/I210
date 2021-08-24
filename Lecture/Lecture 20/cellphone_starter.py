class CellPhone(object):
    """A virtual cell phone"""

    #add your code here, as described below
    """A cell phone has these attributes:
       owner (string) 
       minutes remaining (integer)

    1) Write a constructor to set the attributes listed above.
    
    2) Add an info() method that outputs the name of the
    owner and the number of minutes remaining."""
    def __init__(self, owner, minutes):
        self.minutes = minutes
        self.owner = owner
        
    def info(self):
        print("My owner is", self.owner,".", self.owner, "has", self.minutes, "minutes left.")
        
#main section of the code
phone1 = CellPhone("Amelia", 500)
phone1.info()

phone2 = CellPhone("Bob", 300)
phone2.info()

""" The output of the main section should be:

My owner is Amelia. Amelia has 500 minutes left.
My owner is Bob. Bob has 300 minutes left. """




