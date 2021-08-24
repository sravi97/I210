def dasher2(argument, length = 20):
    return_value = "-"
    dashes = length - len(argument)
    if len(argument) > 20:
        print("Error")
    else:
       return_value += (return_value * int(dashes/2)) + argument + (return_value * int(dashes/2))

    formatted = "-" * int(dashes/2) + argument + "-" * int(dashes/2)
    if (dashes % 2 == 1):
        formatted += "-"
    return formatted

    return return_value

print(dasher2("Hello", 10))
print(dasher2("Welcome", 15))

