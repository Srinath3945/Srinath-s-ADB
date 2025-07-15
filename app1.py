# Build a calculator app

# def add(a, b):
#     return a+b

# def sub(a, b):
#     return a-b

# def multiply(a, b):
#     return a*b

# def divide(a, b):
#     return a/b


# def calculator():
#     print("Select operation: ")
#     print("1. add")
#     print("2. sub")
#     print("3. multiply")
#     print("4. divide")


#     choice = input("enter the choice (1|2|3|4): ")
#     if choice in ['1', '2', '3', '4']:
#         num1 = int(input("Enter the first num: "))
#         num2 = int(input("Enter the second num: "))

#         if choice == '1':
#             print(f"Result : {add(num1, num2)}")

#         elif choice == '2':
#             print(f"Result : {sub(num1, num2)}")

#         elif choice == '3':
#             print(f"Result: {multiply(num1, num2)}")

#         elif choice == '4':
#             print(f"Result: {divide(num1, num2)}")

#     else:
#         print(f"Operation not avaliable for choice {choice} ")

# print(calculator())

# def add(a, b):
#     return a+b

# def sub(a, b):
#     return a-b

# def multiply(a, b):
#     return a*b

# def divide(a, b):
#     return a/b

# def calculator():
#     print("Select operation: ")
#     print("1. add")
#     print("2. sub")
#     print("3. multiply")
#     print("4. divide")


#     choice = input("Enter the choice (1|2|3|4): ")
#     if choice in ['1','2','3','4']:
#         num1 = int(input("Enter the frist num: "))
#         num2 = int(input("Enter the second num: "))

#         if choice == '1':
#             print(f"Result: {add(num1, num2)}")

#         elif choice == '2':
#             print(f"Result: {sub(num1, num2)}")

#         elif choice == '3':
#             print(f"Result: {multiply(num1, num2)}")

#         elif  choice == '4':
#             print(f"Result: {divide(num1, num2)}")

#     else:
#         print(f"Operation  not avaliable for choice {choice}")


# print(calculator())


def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b


def calculator():
    print("Select the operation: ")
    print("1. add")
    print("2. sub")
    print("3. multiply")
    print("4. divide")

    choice = input("Enter the choice (1|2|3|4): ")
    if choice in ['1','2','3','4']:
        num1 = int(input("Enter the first num: "))
        num2 = int(input("Enter the second num: "))

        if choice == '1':
            print(f"Result: {add(num1, num2)}")

        elif choice == '2':
            print(f"Result: {sub(num1, num2)}")

        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")

        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")

    else:
        print("Operation not avaliable for choice {choice}")

print(calculator())