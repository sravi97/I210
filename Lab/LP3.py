#Section 1 - Setting up Place
class Place(object):
    #list to store locations that have been created
    locations_list = []
    #static method
    @staticmethod
    #class attribute to help keep track of what locations have been created
    def locations():
        #count the number of locations
        num_locations = len(Place.locations_list)
        #if there are none, print the following statement
        if num_locations == 0:
            print("No locations exist at this time.")
        #otherwise print all the locations that have been created
        else:
            print("The following locations exist: ")
            for place in Place.locations_list:
                print(place)
            
    #constructor
    def __init__(self, name, location = None):
        print(name, "created.")
        self.__name = name
        self.__location = location
        self.__visited = False
        Place.locations_list.append(self)
    #to-string method
    def __str__(self):
        if self.__location == None:
            reply = self.__name
        else:
            reply = self.__name + ", located in " + self.__location.get_name()

        if self.__visited == False:
            reply += " (not visited)."
        else:
            reply += "(visited)."
        return reply

    #getter method for name   
    def get_name(self):
        return self.__name
    
    #getter method for location
    def get_location(self):
        return self.__location

    #visitation
    def visit(self):
        #if a place has been visited, output a different message
        if self.__visited == True:
            print (self.__name + "has already been visited.")
        else:
            print ("You visit " + self.__name + ".")
            self.__visited = True
            if self.__location:
                print ("That means...", end = " ")
                self.__location.visit()
                
#child class Home
class Home(Place):
    def __init__ (self, name, location, bedrooms, occupancy):
        super().__init__(name, location)
        self.bedrooms = bedrooms
        self.occupancy = occupancy
    def __str__(self):
        reply = super().__str__()
        reply += " This house has " + str(self.bedrooms) + ", of which " + str(self.occupancy) + " are occupied."
        return reply
#child class City        
class City(Place):
    def __init__ (self, name, location, population, mayor):
        super().__init__(name, location)
        self.population = population
        self.mayor = mayor
    def __str__(self):
        reply = super().__str__()
        reply += " This city has " + str(self.population) + " residents, and the mayor is " + self.mayor + "."
        return reply
    
#main - section 1
iu = Place("IU Campus")
library = Place("Wells Library", iu)

print()
print(iu)
print(library)

#main - section 2
Place.locations()

iu = Place("IU Campus")
library = Place("Wells Library", iu)
Place.locations()

#main - section 3
Place.locations ()

indiana = Place("Indiana")
indy = City("Indianapolis", indiana, 853173, "Joseph Hogsett")
btown = City("Bloomington", indiana, 80405, "John Hamilton")
iu = Place("IU Campus", btown)
library = Place("Wells Library", iu)
rental = Home("Rental House", btown, 5, 4)
historic = Home("Elias Abel House", btown, 4, 0)

Place.locations()

#main - section 4
indiana = Place("Indiana")
indy = City("Indianapolis", indiana, 853173, "Joseph Hogsett")
btown = City("Bloomington", indiana, 80405, "John Hamilton")
iu = Place("IU Campus", btown)
library = Place("Wells Library", iu)
rental = Home("Rental House", btown, 5, 4)
historic = Home("Elias Abel House", btown, 4, 0)

print()
library.visit()
indiana.visit()



