import random
print("Welcome to our Password Generator--")
print("-----------------------------------")

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*1234567890"

number = input("Enter the amount of passwords to be displayed on--")
number = int(number)

length = int(input('Enter the length of characters for Password Generator:'))

print('\n here is your password')
for pwd in range(number):
    Passwords = ''
    for c in range(length):
        Passwords += random.choice(chars)
    print(Passwords)
