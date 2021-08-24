class Worker:
    #initialize variables
    name = "";
    payrate = 0.0;
    #constructor that takes as input the worker's name and the hourly payrate
    def __init__ (self,name,payrate):
        self.name = name;
        self.payrate = payrate;
    #takes the new pay rate as input and changes the worker's pay rate
    #to the new hourly rate
    def changeRate (self, newRate):
        self.payrate = newRate;
    #takes the number of hours worked as input and prints "Not Implemented"
    def pay (self, hour):
        print("Not Implemented");

class HourlyWorker(Worker):
    def __init__ (self,name,payrate):
        self.name = name;
        self.payrate = payrate;
    #compute the weekly pay for the worker
    def pay(self,hour):
        #overtime hours over 40
        #paid double
        if hour > 40:
            print(hour*2*self.payrate)
        #hourly rate for actual hours worked
        else:
            print(hour*self.payrate)

class SalariedWorker(Worker):
    def __init__ (self,name,payrate):
        self.name = name;
        self.payrate = payrate;
    #paid for 40 hours regardless of the number of bours worked
    def pay(self, hour=40):
            print (40*self.payrate)

w1 = Worker ("Joe", 15)
w1.pay(35)

w2 = SalariedWorker("Sue", 14.50)
w2.pay()
w2.pay(60)

w3 = HourlyWorker("Dana", 20)
w3.pay(25)
w3.changeRate(35)
w3.pay(25)
