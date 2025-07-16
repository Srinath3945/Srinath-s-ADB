# try except --> error handling

# Basic Try-Except     
# num =int(input("Enter the number:" ))

# try:
#     num =int(input("Enter the number:" ))
#     result = 10/num
#     print(result)

# except ValueError:
#     print("Input is invalid, enters only integers > 1")

# except ZeroDivisionError:
#     print("You can't divide by zero!")

# finally:
#     print("This always runs")


# Custom error handling

# class NegativeNumberError(Exception):
#     pass

# try:
#     num =int(input("Enter the number:" ))
#     if num < 0:
#         raise  NegativeNumberError("Negative numbers are not allowed")
#     result = 10/num
#     print(result)
# except Exception as e:
#     print(f"Exception : {e}")