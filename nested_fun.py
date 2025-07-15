# def greet(name):
#     def message():
#         print(f"Hello, Good Morning  {name} ")
#     return message()
# print(greet("Harish"))

# Inner functions is able to access the parameters that are defined on the outer function.

# def greet(name):
#     def message():
#         print(f"Hello, Good Morning  {name}")
#     return message()
# print(greet("srinath"))

# another scenario

def make_multiplier(x):
    def multiply(y):
        return x*y
    return multiply
times3 = make_multiplier(3)
print(times3(y=6))

times5 = make_multiplier(5)
print(times5(2))