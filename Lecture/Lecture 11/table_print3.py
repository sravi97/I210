# Table Print v2

def table_print(headers, data, width):

    # Add your code here!
    output = "{:>{}} {:>{}}"

    print(output.format(headers[0], width, headers[1], width))    
    print()
    
    print("-"*25)

    for pair in scores:
        print(output.format(pair[0], width, pair[1], width))
            
    print()
    
    # Nothing else in the file should change

#main - Don't change this part!
labels = ["Name", "Score"]
scores = [("Abe", 200), ("Bill", 180), ("Mary", 215)]

table_print(labels, scores, 6)

labels2 = ["Capital", "State"]
state_data = [("Atlanta", "GA"), ("Boise", "ID"), ("Boston", "MA"), ("Austin", "TX")]

table_print(labels, state_data, 8)
