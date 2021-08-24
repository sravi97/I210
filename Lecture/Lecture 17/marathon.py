import random

#open the first file
text_file_RT = open("top100moviesRT.txt", "r")
#read in the contents and convert thme to a set
lines_RT = text_file_RT.readlines()
RT = set(lines_RT)
#close the first file
text_file_RT.close()

#open the second file
text_file_AFI = open("top100moviesAFI.txt", "r")
#read in the contents and convert them to a set
lines_AFI = text_file_AFI.readlines()
AFI = set(lines_AFI)
#close the second file
text_file_AFI.close()

movie_list = list(RT | AFI)
for movies in movie_list:
    movie_list = (movies, end="")
    print(random.choice(movie_list))

num_movies = print(eval(input("How many movies in your marathon? ")))




print("Your custom", num_movies, "movie marathon: ")
