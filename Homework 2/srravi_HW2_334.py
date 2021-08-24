def pay(wage, hours):
    overtime = 40 - hours
    if hours > 40:
        salary = 40 * wage #salary until 40 hours
        salary = salary + wage * (hours-40) * 1.5 #salary after 40 hours
    else:
        salary = wage * hours 
    return salary
        
print(pay(10, 35))
print(pay(10, 45))
