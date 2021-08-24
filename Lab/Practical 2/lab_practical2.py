from tools import *
#open file and read the lines
text_file_cali = open("california.txt", "r")
lines_cali = text_file_cali.readlines()
text_file_cali.close()

#strips the lines and formats around the \t
cali_stats = {}
for i in range(len(lines_cali)):
    candidate, votes = lines_cali[i].strip().split("\t")
    cali_stats[candidate] = int(votes.replace(",",""))

#run the outer loop until we're out of data
while cali_stats:
    #get an element from the unsorted list
    candidate = cali_stats.pop()
    #set a boolean flag to tell us if we inserted the person
    inserted = False
    #go through the sorted list to find out where the element we took out of hte
    #unsorted list belongs
    for i in range(len(sorted_cali)):
        if int(candidate[1]) < int(sorted_cali[i][1]):
            sorted_cali.insert(i, candidate)
            i#as soon as the candidate is inserted, we can change our flag and
            #stop the inner loop
            inserted = True
            break
    if not inserted:
        sorted_cali.append(candidate)
for entry in sorted_cali:
    print(entry)

#open the file and read the lines
text_file_texas = open("texas.txt", "r")
lines_texas = text_file_texas.readlines()
text_file_texas.close()

#strips the lines and formats around the \t
texas_stats = {}
for i in range(len(lines_texas)):
    candidate, votes = lines_texas[i].strip().split("\t")
    texas_stats[candidate] = int(votes.replace(",",""))

while texas_stats:
    #get an element from the unsorted list
    candidate = texas_stats.pop()
    #set a boolean flag to tell us if we inserted the person
    inserted = False
    #go through the sorted list to find out where the element we took out of hte
    #unsorted list belongs
    for i in range(len(sorted_texas)):
        if int(candidate[1]) < int(sorted_texas[i][1]):
            sorted_texas.insert(i, candidate)
            i#as soon as the candidate is inserted, we can change our flag and
            #stop the inner loop
            inserted = True
            break
    if not inserted:
        sorted_cali.append(candidate)
for entry in sorted_cali:
    print(entry)

#run a loop asking which state the user wants info for
while True:
    state = input("Which state's totals would you like to compute (or STOP)? ")
    print("The candidates earned this many votes: ")
    if state.lower() == "california":
        print(table_print(("Candidate", "Vote"), cali_stats, 15))
    if state.lower() == "texas":
        print(lines_texas[i], texas_stats, 15)
    if state.upper() == "STOP":
        break
    print("The breakdown by percent: ")
    
    
    
