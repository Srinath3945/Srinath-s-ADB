# # # variables: variableS are containers storing the values.


# # name = input("Enter name: ")

# # age = input("Your age is: ")

# # # print("Enter name: ", name)
# # # print("Your age is: ", age)

# # print("Goodmorning ", name, "Your age is: ", age)

# # #Modern approach : string formatters

# # # --> we can use string formatters instead of writing the code like this.
# # print("Good Morning {0}, Your age is: {1}".format(name, age))
# # print(f"Goodmornig {name}, Your age is: {age}")

# # we use the static typing and dynamic typing both at a time where the text under the single or dou
# #quotes that is static variable and  the what ever we have defined name as dynamic variable

# # Even we can use fromatters 

# # ---> we can use examples for our practice purpose

# a = input("My University name is: ")
# b = input("I'm studying: ")
# c = input("Result in final semister: ")

# print("your university name= ", a,"which year your studying= ", b,"whats my result= ", c)

# print("your University name= {Universityname}, which year your studying= {Studyingyear}, whats my result= {Result}". format(Universityname=a, Studyingyear=b, Result=c))

# print(f"your university name= {a}, which year your studying= {b}, whats 
# # instead of giving positions we can also give names



# we can assign many values to multiple variables in a single line.

# x,y,z ="orange","banana","apple"

# print(x)
# print(y)
# print(z)
# make sure the number of variables  matches the number of values , or else you will get an error


# one value to multiple variables in one line
# x=y=z= "multiple variables"
# print(x)
# print(y)
# print(z)

# Unpack acollection
# if you have collection of a values in  a list, tuple etc. python allows you to extract the values into
# variables . this is called unpacking.

# list = ['apple','banana','orange']

# x,y,z = list
# print(x)
# print(y)
# print(z)

# # Global variables are created out side of the function
# x = 'srinath'
# def myfun():
#     print('python is learning by ' + x)
# myfun()    
  

#   # if we create inside the function some variable means it will be local variable and global variable reamins 
#   # same

# x = 'Kiran'
 
# def myfun():
#     x = 'raju'
#     print('best friends are ' + x)
# myfun()

# print("raju's best friend is " + x)


# python allows you to assign values to multiple variables in one line.
# x,y,z = "orange", 'Tree', "car"
# print(z)

# # it allows multiple variables to one value
# x=y=z= "car"
# print(z)
# print(x)


# Unpack a collection
# fruits = ["irish","Kiwi","Lichi"]
# x,y,z = fruits
# print(x)
# print(y)

# python output variables
# the python print() function is often used to output variables
# x = "python is awesome"
# print(x)

# # in the print() function , you output multiple varaibles , separated by comma
# x = "python"
# y = "is"
# z = "awesome"
# print(x,y,z)
# # even we can use the + opeartor to output multiple variables
# x = "python "
# y = "is "
# z = "awesome "
# print(x + y + z)

# In python when u try to add int and str like 
# x=5
# y="abc"
# print(x+y) # when we try to add str and int in print() function it will throw an error

# note: we can use , instead of arithmetic characters 
# x =7
# y ='str'
# print(x, y)

# Python global variables
# The variables that are created outside of the function is called as global variables
# create a variable out side the function and use it in the inside the function

# i = "srinath"

# def car():
#     print("car is driven by " + i)

# car()

# if we create any variable with the same namevariable inside the function() means local variable, and can only
# be used it inside the function. The global variable with same name will remain as it was , global and with the 
# original value.

# create a variable inside a function , with same name as the golbal variable

# x = "awesome"
# def myfun():
#     x = "fantastic"
#     # print("python is " +x)

# myfun()
# print("python is " + x)

# NOTE:- if we want to create a global variable inside the function we use the global keyword:
# def my_fun():
#     global x
#     x = "fantastic"
#     # print("python is " + x)
# my_fun()
# print("python is " + x)   # we can use it now outside the function also because we have defined using global keyword


# note: even if we want to change the global variable inside the function we can declare the global keyword 
# we can change it

# x = "awesome"
# def my_function():
#     global x
#     x = "fantastic"
#     print("python is " +x)
# my_function()
# print("python is " + x)

