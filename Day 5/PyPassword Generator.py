#Welcome to the PyPassword Generator
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']
print('Welcome to a PyPassword Generator')
letters_wanted = int(input("How many letters would you like in your password? \n"))
symbols_wanted = int(input("How many symbols would you like? \n"))
numbers_wanted = int(input("How many numbers would you like? \n"))

random_letters = random.sample(letters,letters_wanted)
random_numbers = random.sample(numbers,numbers_wanted)
random_symbols = random.sample(symbols,symbols_wanted)
random_combined = random_letters + random_numbers + random_symbols
random.shuffle(random_combined)
password = ''.join(random_combined)

print(f"Here is your password: {password}")
