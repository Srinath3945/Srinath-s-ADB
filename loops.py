# loops : repeating the actions again and again

# Water a plant 5 times.
# print("Water plant 1")    water plant is static and what is changing here is number.
# print("Water plant 2")
# .
# .
# print("Water plant 5")   
#ninstead of repeating so many times manually like usinng print statement changing the number we can directly 
# use for loop

# types of loops : for loop | while loop

# range() function gives a sequence of numbers
# syntax for range(start, end, step)
#                         here 'end' means (exclusive) not inclusive

#syntax for 'for loop':
# for -keyword we are giving a variable name i.e., i in range(1, n+1): we use n+1 because it is exclusive
                                                  # i as temporary variable.
# for i in range(1, 6):
    # print(f"water plant {i}")  # The static string "water plant" is not changing and the numbers are changing

# we can use for loop in iterable items.
# string , list[], tuple[], dictionary{}  these are all iterable items but not set{} it is unordered
# we can convert set into list or tuple then we can iterate.
# suppose for list
# fruits = ["apple", "mango", "banana"]
# print(fruits)     # it will  just print the list what we have defined

# if we want fruit by fruit means how we can do first like 
# print("apple")
# print("mango")
# print("banana")   like this we execute manually if we use fro loop instead see
# or we can use it through indexes.
#print(fruits[0])
#print(fruits[1])
#print(fruits[2])
# for i in fruits:
    # print(i, end='\n')   # this means it will print on the next line --'\n'

# for i in fruits:
#     print(i, end=',')  if we use comma means it will not print on the next line but one after another using comma it will print
#   

# see if we use in a print statement i.e.,
# print("This is a first line\nThis is a second line")  # we are giving the single line print but how it will print
# see by using the '\n' is forced to print on the next line 

# we can loop to our string items:

# name = "srinath"   # how can we loop this

# for i in name:
#     print(i)

#-------------------------------------------------

#While loop : while loop is also a loop which is used to execute the programming instructions.

# syntax for 'while loop'
# while condition - True:
    # code means             
# suppose if the condition is true it will execute repeated times and when the condition gets 
# false it will stop executing 
# if the condition is true untill it will execute if the condition gets false
# it will check for whether the given condition is true.
# i = 1
# while i <= 10:
#     print(i)
#     i +=1

      # like this we will give means it just show 1 we need 2 or 3 like this increment means i = i+1

                # in every programming language we use it for increment in python we have pythonic increment i.e., i+=1

# Note: if we know the number of iterations means we can go for "for loop"
# if we don't know how many times my while loop will execute to define the output at that time we use
# while loop.


# conditional statements:
# if condition : 
#     # this code will be executed 
# else: 
#     # this code will be executed

# check whether the 10 is even number or not.
# only one if condition and else condition we can execute and we can execute multiple elif conditions

# age = int(input("Enter the age :"))
# if age > 18 and age < 60:
#     print("The citizen has right to vote")
# elif age >= 60:
#     print("The citizens who are aged above 60 will now have right to vote online")
# else:
#     print("The citizen has no right to vote")


# num = int(input("Enter a number:"))

# if num == 0:
#     print("You have entered 0 - this is a whole number")
# elif num%2 == 0:
#     print(f"{num}  is even number")


# else:
#     print(f"{num} is odd number")

# there is no mandatory thing that we need to execute the elif and else condition if we are done with the 
# "if condition" is satisfied with our answer.

# if condtion:
#      print("fhkfjskf")

numbers = [9,10,11,12]
for num in numbers:
    print(num)