# list : mutable datatype  starts with []
# tuple immutable datatype even starts with []
# set : is a datatype that starts with {}
# dictionary : dictionary is also datatype that stars with first key and then Value
# key : value

# datatypes in python is important topic
# variables can store different datatypes , and different datatypes do different things
# python has the following datatypes built in by default ,  in these categories:

'''
Text = str
Numeric types = int, float, complex
Sequence types = list, tuple, range
Mapping type = dict
Set types = set, frozen set
Boolean type = bool
Binary types = bytes , bytearray, memoryview
None type = None
'''

# Getting the datatype :: --> You can get the datatype of any object using the type() function.

# x =5
# print(type(x))

# Setting the datatype
# In python datatype is set when you assign a value to variable:
# x = "hello , world"
# print(x)
# print(type(x))

# y = 5
# print(y)
# print(type(y))

# a = 20.5
# print(a)
# print(type(a))
 
# b = 1j
# print(b)
# print(type(b))

# c = ["apple", "banana", 2, 5]
# print(c)
# print(type(c))

# d = ("apple", "orange", 2, 10)
# print(d)
# print(type(d))

# e = range(6)
# print(e)
# print(type(e))

# f = {"car", "bike", "cycle"}
# print(f)
# print(type(f))

# g = {"name": "srinath" , "age": 27}
# print(g)
# print(type(g))

# i = frozenset({"car", "bike", "cycle"})
# print(i)
# print(type(i))


# j = True
# print(j)
# print(type(j))

# k = b"Hello"
# print(k)
# print(type(k))

# Type conversion
# x= 1
# y = 2.8
# z = 5j

# # convert from int to float
# a = float(x)
# print(a)

# # convert float to int
# b = int(y)
# print(b)

# # convert from  int to complex
# c = complex(x)
# print(c)

# Random numbers
# directly we don't have built in random() function but we habe random module so that we can have built in 
# import random module we can use for random numbers

# import random
# print(random.randrange(1, 1000))


# Python strings :
# python strings are surrounded by a single or double quotation marks. you can display the strings with print()

# print("hello")
# print('hello')

# Quotes inside quotes
# print("This is an print function and I'm printing it to output")
# print("he is called 'jhonny' ")
# print('This is called "Strings" ')

# we want multiline strings means
# q ='''
# this is called as multine strings
# so that we can add the three single quotes
# in between we can type anything what we need.
# even we can use three double quotes also.
# '''

# print(q)


# Strings are arrays 
# Like other many programming languages , strings in python are arrays of bytes representing unicode characters
# how ever python does not have a character datatype , a single character is simply a string with a length of 1
# Square brackets are used to access elements of strings.
# get the character at position 1 
# a = "hello, world"
# print(a[1])

# since strings are arrays , we can loop through the characters in a string , with a for loop
# for x in "banana":
#     print(x)

# string length:
# a = "srinath reddy"
# print(len(a))

# # check the string
# a = 'iam checking the string in a variable'
# print('the' in a)  # ok it is checking an giving the answer.

# string slicing

# modify the strings

# a = "hello world!"
# print(a.upper())

# v = "HELLo WOrld!"
# print(v.lower())

# f = "  hello  world!  "
# print(f.strip())     # it will remove the unwanted spaces in the strings.

# Split string

# The split() method returns a list where the text between the specified separator becomes the list items.
 
# The split() method split the string into sub strings if it finds the instances of the separator.
# a = "Hello, World!"
# print(a.split(','))

# Replace the strings 
# The Replace() method is replaces a string with another string
# a = "Bahubali the beginnig"
# print(a.replace("B", "D"))

# String concatenation : To concatenate , combine , two strings you can use the + operator.

# merge variable a with variable b into variable c

# a = "Hello,"
# b = " World!"
# c = a + b
# print(c)

# # to add a space between them
# a = "Hello,"
# b = "World!"
# c = a + b

# print(a + " " + b)

# Fromat strings

# age = 26
# txt = "My name is srinath, I am " + age
# print(txt)                 # we cannot combine strings and integers like this.

# f"string is now the preffered way of formatting the strings.
# age = 26
# txt = f"My name is srinath and I am {age} old."
# print(txt)

# Place holders and modifiers

# a palce holder can contain variables , operations , functions , and modifiers to format the value
# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# a place holder can have a modifier to format the value.
# a modifier is included by adding a : colon followed by a legal formatting type, like .2f which means fixed point
# with 2 decimals.

# price = 39
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# A place holder can contain pythoncode, like math operations
# price = 50
# txt = f"The price is {20*50} dollars"
# print(txt)

# Escape characters :
# To insert the characters that are illegal in a string, use an escape character
# An escape character is a backslash \ followed by the character you want to insert
# An example of an illegal character is a double quote inside a string that is surrounded by the double quotes.

# a = "The string now iam going to print is "Escape characters""
# this is illegal to print the double quotes inside the double quotes.

# To fix the problem, use the escape character \":

# txt = "I am the srinath and iam \"printing\" Escape character"
# print(txt)

# Python Booleans 
# Boolean represent the one of two values: True or False
# In programming you often need to know the if an expression is True or False.
# when you compare two values , the expression is evaluated and python return the boolean answer.

# print(10>5)
# print(10 == 5)
# print(6 < 9)

# when you run a condition in if statement , python returns true or false.

# a = 15
# b = 50
# if a > b:
#     print("a is not greater than b")
# else:
#     print("a is greater than b")

# Evaluate values and variables
# print(bool("hello"))

# print(bool(15))
# The bool() function allows u to evaluate any value and give you true or false in return
# a = "helo"
# b = 15
# print(bool(a))
# print(bool(b))

# Almmost any value is evaluated to true if it has some sort of content
# Any string is true , except empty strings
# Any number is true , except 0
# Any list , tuple, set, dict are true , except empty ones.

# print('{0:.2%}'.format(2/5))
# map = {1: 'one', 2: 'two', 3:'three'}
# print(map[1])

# a = [5,1,5,6]
# a.sort()
# print(a)

# a = {1,2,3}
# a[0] = 4
# print(a)

# Python operators are used to perform operations on variables and values
# In the example , we use + operator to add together two values.
# print(10 + 5)
# python divides the operators in the following groups:
'''
1) Arithmetic operators
2) Assignment operators
3) Comparision operators
4) Logical operators
5) Identity operators
6) Membership operators
7) Bitwise operators
'''

# print(10**3)

# List : list are used to store multiple items in a single variable.
# lists are one of 4 built in datatypes in python used to store collections of data,  the other three are tuple,set
# and dictionary

# ---------->>>Lists are created using square brackets.
# my_list = ["cars","furits","veggetables", "cars"]
# print(my_list)
# # note: list items are ordered, changeable, and allow duplicates.
# # list items are indexed , the first item has index [0] and followed by the second item [1]
# # ordered::-- list is ordered , it means items that the items have a define order , and that order will not change
# # if you add new items to list it will add at the end of the list.
# # note: There are some list items that will change the order, but in general: the order of items will not change

# #  ----->>> Changeable
# # The list is changeable , meaning that we can change , add , and remove items in a list after it has been created
# #------>>> Allow duplicates.
# # list allow duplicates 

# # List length:
# # The len() function is used to  determine the how many items arre there.
# print(len(my_list))

# # list items can be any of datatypes.
# '''
# str , int and boolean datatypes
# list1 = ['apple', 'banana', 'orange']
# list2 = [1,2,3,4,5]
# list3 = [True, False, False]
# '''

# # Alist can conntain different datatypes.
# mylist1 = [1,'car',3,4,'fruits',True, False]
# print(mylist1)
# print(type(mylist1))
# '''
# The list() constructor
# it is also possible to use the list() constructor when creating a new list
# '''
# thislist = list(('apple',1,2,'car',True,False))
# print(thislist)

'''
Access itmes
'''
# list = ['apple','banana','orange',1,4,7,True]
# print(list[0])
# print(list[4])
# the first item has index 0
# negative indexing means starts from the end.
# -1 refers to the last item, -2 refers to the second last item
# print(list[-4])

'''
Range of indexes 
you can specify the range of indexes by specifying where to start the range and where to end the range.
when specifying a range , the return value will be the a new list with the specified items.
'''

# print(list[2:6])
# # if we want from first i.e., from index[0] means
# print(list[:5])
# # to the end if we want means without describing any index value means:
# print(list[3:])

# '''
# Range of negative indexes
# '''
# print(list[-1:])
# print(list[:-1])
# print(list[-4:-1])

# '''
# Check if items exists:
# '''

# if True in list:
#     print("Yes, there is true in list")
# else:
#     ("no")

'''
Cahnge item value
To change the value of a specific item, refer to the indee number
'''

# list = ['car','bus','train','plane']
# list[1] = 'Airbus'
# print(list)

# change the range of item values.
# list = ['car','bus','train','plane','phone','tv','fridge']
# list[1:4] = ['Airbus','3']
# print(list)
'''
# note :---> the length of the list will change when the number of items inserted do not match the number of items
replaced
If you insert less items than you replace , the new items will be inserted where you specified and the reaminig
items will move accordingly
'''

# Insert items :
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "orange")
# print(thislist)

'''
python list add items 

Append items:
to add items at the end of the list , use append() method.
'''
# my_list = ["orange", "apple",]
# my_list.append("kiwi")
# print(my_list)

'''
insert items
to insert an list item at a specified index , use the insert() method
'''
# my_list = ["orange", "apple",]
# my_list.insert(0,"kiwi")
# print(my_list)

'''
Etend items
To append elements from another list to the current list , use the extend() method.
the elements added to the end of the list.
'''

# list1 = ["cars","buses","cycles"]
# list2 = ["tyres","engine","mirrors"]
# list1.extend(list2)
# print(list1)

'''
Add any iterable
The extend method does not have to append lists,you can add any iterable object (tuples
sets, and dictionaries etc.)
'''

# list1 = ["cars","buses","cycles"]
# tuple1 = ("tyres","engine","mirrors")
# list1.extend(tuple1)
# print(list1)

'''
Remove list items
The remove() method removes the specified item.

'''

# a = [1,2,3,4,5]
# a.remove(4)
# print(a)
# # If there are more than one item with the specified value , the remove() method first
# removes the occurence.

# a = [1,2,3,4,5,6,7,5,3]
# a.remove(3)
# print(a)

'''
Remove specified index
the pop() method is used to remove the specified index from the list.

'''

# a = [1,2,3,4,5,6,7]
# a.pop(3)
# print(a)

# note :--> if we don't want to specify the index the pop() method removes the last item


# a = [1,2,3,4,5,6,7]
# a.pop()
# print(a)

'''
The del keyword also removes the specified index.
# '''
# a = [1,2,3,4,5]
# del a[2]
# print(a)

'''
Clear the list
it will remove the content , but list still remains
'''

# a = [1,1,2,4,6]
# a.clear()
# print(a)

'''
Loop through a list
You can loop through the list items by using for loop.
'''

# b = [1,2,"car","bus",True]
# for i in b:
#     print(i)

'''
Loop through the index numbers 
You can also loop through the list items by referring to the index numbers
Use the range() and len() function to create a suitable iterable
'''

# c = [1,1,1,1,1,1,2]
# for i in range(len(c)):
#     print(i)

# it will create the iterable from index 0 to length of the iterable items

'''
Using a while loop
you can loop through the list items by using a while loop.

use len() function to determine the length of the list , then starts at 0 and loop your
way through the list items by referring their indexes 


remember to increase the index by 1 after each iteration

'''

# d = [1,2,3,4,5]
# i = 0
# while i < len(d):
#     print(d[i])
#     i+=1

'''
List comprehension
list comprehension offers a shorter syntax when you want to create a new list based on
the values of an existing list.

Based on a list of fruits , you want a new list , containig only fruits with letter "a"
in the name 

without list comprehension you will have to write a for statement with a condition inside

'''

# fruits = ["apple","orange","kiwi","lichi","banana","mango"]
# new_lst = []

# for i in fruits:
#     if "a" in i:
#         new_lst.append(i)
# print(new_lst)

# with list comprehension

# fruits = ["apple","banana","lichi","kiwi","Dragon"]
# new_lst = [i for i in fruits if "a" in i]
# print(new_lst)

'''
syntax for list comprehension : [expression for item in iterable if condition == True]
'''

# only accept items that are not "apple"

# newlist = [i for i in fruits if i != "apple"]

# The condition if i != "apple" will return true for all elements other than "apple", making
# the newlist contain all fruits other than "apple".
# The condition is optional and can be omitted:
# with no if statement
# fruits = ["apple","guava"]
# newlist = [i for i in fruits]
# print(newlist)

'''
Sort the list
sort list alphanumerically

list object have a sort() method that will sort the list alphanumerically , ascending 
by default
'''

# a = ["apple","banana","guava","dragon","kiwi","avacado"]
# a.sort()
# print(a)

# a = ["apple","banana","guava","dragon","kiwi","avacado"]
# a.sort(reverse=True)
# print(a)

'''
copy method
'''

# a = ["apple","banana","guava","dragon","kiwi","avacado"]
# b = a.copy()
# print(b)
 # Use the list method -->> Another way to make a copy is to use the built-in list() method

# a = ["apple","banana","guava","dragon","kiwi","avacado"]
# b = list(a)
# print(b)

# you can also make acopy by using the : slice operator
# a = ["apple","banana","guava","dragon","kiwi","avacado"]
# b = a[:]
# print(b)

"""
Tuple : Ordered , Unchangeable, allow duplicates
"""

tuple = ("orange","apple",1,3,1,5)
print(tuple)
print(len(tuple))

# Create tuple with one item
a = ("orange",)
print(type(a))

a = ("orange")     # --->> without comma it is not the tuple
print(type(a))