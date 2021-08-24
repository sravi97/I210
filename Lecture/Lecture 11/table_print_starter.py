# Table Print v2

def table_print(headers, data):

    # Add your code here!
    for label in labels:
        print(label, end = "\t")
    print()
    print("-"*25)
    for i in range(len(scores)):
        print(i, scores[i][0], scores[i][1], sep="\t")
    print()
    
    # Nothing else in the file should change

#main - Don't change this part!
labels = ["i", "Name", "Score"]
scores = [("Abe", 200), ("Bill", 180), ("Mary", 215)]

table_print(labels, scores)

labels = ["i", "Capital", "State"]
scores = [("Atlanta", "GA"), ("Boise", "ID"), ("Boston", "MA"), ("Austin", "TX")]

table_print(labels, scores)
