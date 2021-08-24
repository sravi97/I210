def vowelCount(string):
    string = string.lower()
#counts the number of a's in every string
    a_count = 0
#counts the number of e's in every string
    e_count = 0
#counts the number of i's in every string
    i_count = 0
#counts the number of o's in every string
    o_count = 0
#counts the number of u's in every string
    u_count= 0
#counter 
    for letter in string:
        if letter in "aA":
            a_count = a_count + 1
        elif letter in "eE":
            e_count = e_count + 1
        elif letter in "iI":
            i_count = i_count + 1
        elif letter in "oO":
            o_count = o_count + 1
        elif letter in "uU":
            u_count = u_count + 1
#formatted print statement
    return ("a, e, i, o, and u appear, respectively, {0},{1},{2},{3},{4} times.".format(a_count, e_count, i_count, o_count, u_count))

print(vowelCount("Le Tour de France"))
