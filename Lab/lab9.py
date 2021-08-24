### LAB 9 GROUP WORK
### PROBLEM 2

class Robot(object):
    
    """this is a blueprint for a program that models virtual fighting robots"""

    robot_list = []

    @staticmethod
    def contenders():

        if len(Robot.robot_list) == 0:
            print("There are 0 robots.")

        else:
            print("There are " + str(len(Robot.robot_list)) + " robots.")

            print("Here's a list of them:")
            
            for robot in Robot.robot_list:
                print(robot)
        

    def __init__(self, name, weapon, strength, status = "ONLINE"):
        self.name = name
        self.weapon = weapon
        self.strength = strength
        self.status = status
        print("Robot created!" + self.name)

        Robot.robot_list.append(self)

        
    def __str__(self):
        reply = "-" * 20 + "\n"
        reply += "Fighting Robot\n"
        reply += "Name: " + self.name + "\n"
        reply += "Weapon: " + self.weapon + "\n"
        reply += "Strength: " + str(self.strength) + "\n"
        reply += "Status: " + self.status + "\n"
        reply += "-" * 20
        return reply


# main
Robot.contenders()

r2d2 = Robot("Optimus", "Fists", 2)
c3po = Robot("C3PO", "Conversation", 2)

##print(r2d2)
##print(c3po)

Robot.contenders()
