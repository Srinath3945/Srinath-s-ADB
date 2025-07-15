 # functions | methods in python we don't call function we called it as methods

# def funName():
#     code                 basic syntax for def a function

# def add(a, b):
#     return a + b     # like this if we use it won't give any output.
# print(add(19, 41))   # i can call my function as many times i want.
# print(add(139, 491))   # i can call my function as many times i want.


# we can use greet function     greet is a static function

# def greet():
#     return "Good Morning"

# print(greet())  

# suppose if we use the input from user i.e., name:

# name = input("Enter the name ")

# def greet(name):
#     return f"Good Morning {name}"
# print(greet(name))
# print(greet("Lucky"))


# x = 3 > 2
# y = 5 < 1
# print(x, y)

# print even numbers up to 100
# for i in range(2, 101):
#     if i%2==0:
#         print(i)

# # print odd numbders upto 100
# for i in range(1, 101):

#     if i%2!=0:
#         print(i)

# a = int(input("Enter the number"))

# if a%2 == 0:
#     print("Even number")
# else:
#     print("odd number") 


# functions with default parameters : default parameter is a parameter that something u passed at the function
# # even though u don't pass any parameters.

# def greet(age,height, n = 'Ganesh'):    # this is default we are giving the parameter. see this parameter should be at the end of the list.
#     return f" Good morning  {n} and his age is {age} and his height is {height}"

# print(greet(n='Srinath', age= 27, height= 180))
# print(greet())

# why it is giving ganesh even if we don't define anything also means it is considered as default parameter.

# Arbitrary arguements 

# a,b, *rest =5,6,7,8
# print(a,b,*rest)


# def add_all_nums(*numbers):         # when we give *numbers means it will convert the numbers into tuple and total it
#     l = numbers
#     print(type(l)) 
#     total = sum(numbers)
#     return total

# print(add_all_nums(1, 2, 3, 4, 5))
# print(add_all_nums(10,20,30,40,50,60))   #if we just give numbers without any tuple or list but when defining
                                        #  as numbers it takes 1 positional arguement but 6 were given throwing error



# def add_all_nums(*numbers):
#     a = numbers
#     print(type(a))
#     total =sum(numbers)
#     return total

# print(add_all_nums(1,2,3,4,5))
# print(add_all_nums(10,40,60,90,100,50))

# Arbitrary keyword arguements

# def student_details(**info):          #keyword arguemnts we will define **
#     return info                    
#     print(type(info))
#     # for key, value in info.items():
#     #     print(f"{key}: {value}")
# print(student_details(name= 'amit', age=27, city="Bangalore"))



# Lambda functions -> anonymous functions | single line functions
 
# add = lambda a, b: a+b    # after colon a+b will be the logic
# print(add(10,60))          # and variable name add will become the function.

# if we want to know the number is even or odd

# even_odd = lambda a:f"{a} is even"  if a%2==0 else f"{a} is odd"
# print(even_odd(34))
# print(even_odd(37))

# # without using lambda function means:
# def even_odd(n):
#     if n%2==0:
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")


# for dictionary items:
# dic_items = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4}
# even_lambda = lambda x : [f"{key} : {value}" for key , value in x.items() if value%2 == 0]
# print(even_lambda(dic_items))

# we cannot use the for loop directly in lambda functions we can create like list and we can use it.

# function calling other function 
# def multiply(a, b):
#     return a*b
# print(multiply(18, 6))

# # find area of rectangle
# def area_of_rectangle(length, breadth):
#     return multiply(length, breadth)

# print(area_of_rectangle(8,4))

def outer():
    print("This is an outer function")
    
    def inner():
        print("This is an inner function")

    print("I'm part of this function")
    inner()
    

print(outer())
    



      