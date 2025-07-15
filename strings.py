# string datatypes
# name = 'Harish'

# print(type(name))
#  
# even that is string or whatever in programming languages indesx start with 0 and in sequence i.e., 0,1,2,3,4...
# -- if we want to extract hari name from harish
# print(name[0:3])
#see if we if we want hari  name that and we use from index to i.e., 0 to  3 it will only print 
# 3 characters so we need to add +1 0r n+1 we use means we will get the correct answer.
# print(name[0:4])

# syntax for indexing is:
# index = [start: stop : step=1] # if we used like this means it will exagarate only one value h to a and a to r
# like this 
# index = [start: stop: step=2]# if we exclude 1 and have given 2 means
# it will exclude 1 value and go to next value
# print(name[0:4:2])
# it will exlude 1 value in between because we have given 2 in step value and it will definitely 
# exclude  the i value because that is the last so if we have give the stop value as 5 means
# print(name[0:5:2])# it will exclude the a value and i value because we have given step value as 2.

# what if 0 position is not given means i.e., like this means [:4:2]
# print(name[:4:2])
# print(name[::2])
# print(name[:3])
# print(name[::])
# print(name[:])


# let's say with the exmple
# marvel =input("Enter any character: ").strip()    # strip will cut the unwanted spaces

# "Un wanted  Spaces     "   # these unwanted spaces will be removed by using the .strip() function
#indexes for ironman
# I -0, R -1, O -2, N -3, M -4, A -5, N -6    this is positive index
# suppose i need only man from marvel
# print(marvel[4:])   # 4 is the start position and and we can define the last position we can't also means
                    # it automatically by default it will take the last position

# I- (-7), R- (-6), O- (-5), N- (-4), M- (-3), A- (-2), N- (-1)       

# print(marvel[-3])
# print(marvel[:-4])
# print(marvel[-1])

# we are using the .strip() function so that it removes all kinds of spaces any where in the sentence 
#  so if we use negative index so that my last word will come as output.

#Index will give the first occurence 
# --- if we want to find out the position of the character means.

# marvel = "antmantstvunmta"
# index will give the first occurence we have seen and we want to skip first a means. we use step to skip
# for next a.

# print(marvel.index('a'))

# print(marvel.upper())
# print(marvel.replace('$', ''))

# print(marvel.index('t',7 ))



               
