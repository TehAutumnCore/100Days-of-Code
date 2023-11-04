#Welcome to the Band Name Generator
#Ask the user of the name of the city they grew up in
city = input("What's the name of the city you grew up in?\n")
#Ask the user for the name of their pet's name
pet_name = input("What is the name of your pet?\n")
#output should be "Your band name could be city name and pet name
print(f"Your band name could be the {city} {pet_name}s")
print("Your band name could be the " + city + " " + pet_name + "s")
print("Your band name could be the {} {}s".format(city, pet_name))
