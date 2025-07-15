# python classes

# in python every thing is object.
# what ever u defined in python like variable , function etc it is object  in python

# class is like a blueprint 

# class person:
#     def show_details(self):
#         return "This is a person class" 
    

# person1 = person()
# print(person1.show_details())
    


# class person():   
#                                                       # we need to specify the self because class should identify that this function belong to the class
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender   # it wont recognise the name variable and gender variable we need to specify that.
#     def show_details(self):
#         return f"Hello, I'm {self.name} and my gender is {self.gender} "
    
# person2 = person("Srinath", "Male")
# print(person2.show_details())
# even we can define parameters for class not like how we define for functions i.e., def fun(age,name,n=variable)
# we use constructor  def  __init__


# class person():
#     def __init__(self , name, profession):    # class will not recognise anything at all self is the key word that recognise the parameters that are given to class 
#         self.name = name
#         self.profession = profession
#         print("I'm the constructor method for the person class")

#     def show_details_of_chef(self):
#         return f"Hello, my name is {self.name} and Iam the  {self.profession} in five star Hotel"
    
# chef = person("Srinath", "Chef")    # In order to access this class we need to create an object instance 
# print(chef.show_details_of_chef( ))   # we can use this class as many times as we need.

# print('\n') 

# person2 = person("Lakshmi sri", "chef")
# print(person2.show_details_of_chef())


# class lover:
#     def __init__(self, name, name1):
#         self.name = name
#         self.name1 = name1
#         # print("I'm the constructor method for defining variables to the class")

#     def show_details_love(self):
#         return f"{self.name} is loving the {self.name1}."
    
# love = lover("Srinath", "Lucky chowdary i.e., Lakshmi sri")
# print(love.show_details_love())

# print('\n')

# love1 = lover("Lakshmi sri i.e., Lucky chowdary " ,"srinath")
# print(love1.show_details_love())
        
