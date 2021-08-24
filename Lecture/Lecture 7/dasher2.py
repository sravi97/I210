def dasher2(argument):
    return_value = "-"
    dashes = 20 - len(argument)
    if len(argument) > 20:
        print("Error")
    else:
       return_value += (return_value * int(dashes/2)) + argument + (return_value * int(dashes/2))

    return return_value

print(dasher2("Hello"))
print(dasher2("Greetings"))
print(dasher2(dasher2("TEST?")))
