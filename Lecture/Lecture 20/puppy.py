class Puppy(object):
    def __init__ (self, name, counter):
        self.name = name
        self.counter = 0
    def __str__(self):
        reply = "Puppy Object\n"
        reply += "Name:" + self.name + "\n"
        reply += "Bark Counter: " + str(self.counter) + "times\n"

    def bark(self):
        bark1 = print("Bark!")
        self.counter += 1
        print(self.name, "has barked", self.counter, "time(s).")



#main
puppy1 = Puppy("Spot", 5)
for i in range(5):
    puppy1.bark()
    print()
    print(puppy1)
        

