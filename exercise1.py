# name = input("Enter the name: ")

# nisha -- [a,e,i,o,u] we need to find out how many vowels are there in the name nisha.

# vowels = ['a', 'e', 'i', 'o', 'u']
# count = 0

# for i in name.lower():
#     if i in vowels:
        # count+=1
# print(f"{name} has {count} vowels in it")

# why it is not 3 when we give Aravind name even it has 3 vowels it is showing 2 because of A capital letter

# it is iterating through the name so if we want to find out the vowels in the name means we use the if condition

# x = 1

# if x > 8:
#     print('fast')
# elif x < 8:
#     print('slow')

# print numbers from 1 to 50 not on the separate line because it will take default next line while we use loops.

# for i in range(1, 51):
#     print(i)

    # so  now i don't want to print numbers in next line i want to print like this 1,2,3,4........50

# for i in range(1, 51):
#     print(i, end=',')     # instead of new line it ended with comma(','). even we can end it with pipe symbol(|)

# for i in range(1, 51):
#     print(i, end='|')

# next thing i want to print the two table: using loop

# for i in range(1, 11):
#     print(f"2 * {i}  = {2*i}")

# print the 5 th table using the for loop.

# for i in range(1,16):
#     print(f"5 * {i} = {5*i}")

# print 12 th table using the for loop. up to 12*20
# for i in range(1, 21):
    # print(f"12 * {i} = {12*i}")

# # print 20 th table using the for loop upto 20*20
# for i in range(1, 21):
#     print(f"20 * {i} = {20*i}")


# suppose i want 2table and 3table and 4th and 5th table by separating ---------- by using nested loops
# for i in range(2, 6):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")
#     print("--------------------------")

# python programming for printing pyramids
#  half pyramid pattern:
# rows = 5
# for rows in range(1, 6):
#     print(rows * '*')

# inverted half pyramid: by using range function i.e., start stop and end syntax we use in step -1 to decrease
# from top to bottom i.e., 6 stars to 1 star.

# for i in range(6, 0, -1):
#     print(i*' *')
 
# a ='7'
# a+='2'
# t = int(a) * 2
# print(float(t))

# print 10th table
# for i in range(1, 11):
#     print(f"10 * {i} = {10 * i}")

# # print 15 th table

# for i in range(1, 15):
#     print(f"15 * {i} = {15*i}")

    # Now print 10 th , 15 th , 20 th and 25 th table
# for i in range(5, 26, 5):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")
#     print("-----------------------------")


# Now find vowels
# vowels = ['a','e','i','o','u']

# name = input("Enter the name: ")
# count =0

# for i in name:
#     if i in vowels:
#         count+=1
# print(f"{name} has {count} of vowels in it.")


# to find vowels   for finding how many vowels means we use count to count the vowels in the string.
# name = input('Enter the name: ')
# count =0
# vowels = ['a','e','i','o','u']

# for i in name:
#     if i in vowels:
#         count+=1
#     print(f"{name} has {count} of vowels in it.")



# def func(a,b,c):
#     print(a,b,c)

# my_list = [1,2,3]
# func(*my_list)



# a = int("20", 8)
# print(a)

# print(list(map(lambda x: x*2, [1,2,3])))

# this is a beginner question that lambda and map functions are used in the list to multiply

# a = '10'
# b = 5
# print(a + b)
# it will multiply the string 5 times

# x = 7
# y = 2
# print(x + y)
# just add both the variables i.e., 9

# num = 5
# print(num + "5")
# unsupported operand type(s) for +: 'int' and 'str'

# result = (8/4)+(3*2)-1   #8-1 = 7 bodmas rule
# print(result)

# x = [1,2,3,4,5,6]
# print(x[2:])

# correct output
# print(type(x))   it will give the which type of datatype it is:

# a=10
# print(~a)

# print(-18//4)  
# because // operation shows floor division so -18//4 = floor(-4.5) == -5 it will round of to next nearest value.

# lang = ['python', 'java', 'javascript']
# print(max(lang))

# a= (0,1,2,3,4)
# b= slice(0,2)
# print(a[b])

# print 8th table up to 10
# for i in range(1, 11):
#     print(f"8 * {i} = {8*i}")

#count the number of vowels in the name
# name = input("Enter the name: ")

# count =0
# vowels = ['a','e','i','o','u']

# for i in name.lower():
#     if i in vowels:
#         count+=1
# print(f" {name} has {count} of vowels in it.")


# print the number is even or odd

# num = int(input("Enter the number: "))

# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

# by using the functions
# def even_odd(n):
#     if n%2==1:
#         print(f"{n} is odd number")
#     else:
#         print(f"{n} is even number")

# print(even_odd(25))
# print(even_odd(18))

# by using lambda function we can print the result on  using single line.

# even_odd = lambda x: f"{x} is even" if x%2==0 else f"{x} is odd"
# print(even_odd(12))
# print(even_odd(9))

# x = (1,2,3)
# y = x
# y[0] = 10   
# print(x)
  
# in tuple we cannot change because it is immutable
# in list we can change it because it is mutable.

# x =1
# if x > 8:
#     print("big")
# else:
#     print("small")

# i =0
# while i < 10:
#     if i == 7:
#         break
#     i = i +1
# print(i)

# text = "codecrafter"
# print(text[>-]))

# print("{:,}".format(1234567))