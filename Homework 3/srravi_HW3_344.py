def distance(time):
    #asking for how many seconds it has been
    time = eval(input("Time elapsed: "))
    #getting distance traveled
    sound = 340.29 * time
    #getting distance in kilometers
    dist = sound/1000
    #display results
    return(dist)


print(distance(3))
    
