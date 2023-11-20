# def my_function():
#    #Do this
#    #Then do this
#    #Finaly do this
#my_function()

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
# greet()

#function that allows for input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
# greet_with_name("Gary")

#functions with more than 1 input
def greet_with(name, location): #positional arguement
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


#Functions with keyword arguements
# def greet_with(location = "US",name = "Gary"): #positional arguement

greet_with(location = "The US", name = "Gary")