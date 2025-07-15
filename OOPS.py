# OOPS:--->>   Object oriented programming


# 1) Encapsulation
# class BankAccount():
#     def __init__(self, balance):
#         self.__balance = balance     #---> self.__balance = private variable   
# # we cannot use __balance i.e., private variable outside of the class.
#     def __deposit(self, amount):   # we can Encapsulate deposit by giving __deposit like as private
#         if amount > 0:
#             self.__balance += amount

#     def add_amount(self, amount):
#         temp = self.__deposit(amount)
#         return temp
# # add_amount is a method name we can encapsulate by __before the method.
#     def get_balance(self):
#         return self.__balance
    

# account = BankAccount(20000)
# print(f"Current balance before deposit - {account.get_balance()}")
# account.add_amount(30000)
# print(f"Current balance after deosit - {account.get_balance()}")

# print(account.get_balance())

# Bank Example for the Encapsulation:

class BankAccount():
    def __init__(self, balance):
        self.__balance = balance
        
    def __deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def add_money(self, amount):
        temp = self.__deposit(amount)
        return temp

    def get_balance(self):
        return self.__balance 
    

# account = BankAccount(20000)
# print(f"Current balance before the deposit - {account.get_balance()}")
# account.add_money(30000)
# print(f"Current balance after the deposit - {account.get_balance()}")


# 2) Inheritance:

'''
In Inheritance we have
1) parent class (base class) and 2) child class (derived class)
'''

class Animal():       # --->> Parent class
    def speak(self):
        "This animal makes a sound"

class Dog():         # ----> Child class
    def speak(self):
        return "Dog barks!!"
    def show_details(self):
        return "Hi my name is chintu and I am a dog!"
    
class cat():
    def speak(self):
        return "cat makes a meow's"

    def show_details(self):
        return "Hi my name is Rita and I am a cat!"
    
chintu = Dog()
print(chintu.speak())
print(chintu.show_details())

Rita = cat()
print(Rita.speak())
print(Rita.show_details())


'''
we have three types of inheritances
1)Multiple inheritance
2)Multilevel inheritance
3) Hybrid  inheritance
'''

# Multiple inheritance:
class Fatherparent():
    pass

class Motherparent():
    pass

class child(Fatherparent, Motherparent):
    pass

# Multilevel inheritance

class grandparent():
    pass

class Fatherparent(grandparent):
    pass

class child(Fatherparent):
    pass


# Hybrid inheritance:
# it's the combination of both multiple and multilevel inheritances

'''
3) Polymorphism
'''
class Phonepay():
    def make_payment(self, amount):
        return f"Paid {amount} to user via phonepay"

class GooglePay():
    def make_payment(self, amount):
        return f"Paid {amount} to user via Gpay"
    

class Amazonpay():
    def make_payment(self, amount):
        return f"Paid {amount} to user via Amazonpay"
    
phnpay = Phonepay()
Gpay = GooglePay()
amzpay = Amazonpay()

instances =[Phonepay(),GooglePay(),Amazonpay()]
for instance in instances:
    print(instance.make_payment(1000))


# Abstact class :: --> it cannot be used it on own it is like blue print.it does not do
# anything at all. it will be an unimplemented class.

     
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine started"
    def move(self):
        return "Car started moving"
    
class Bike(Vehicle):
    def start(Vehicle):
        return "Bike engine started"
    

    def move(self):
        return "Bike started moving"


car = Car()
bike = Bike()

print(car.start())
print(bike.move())