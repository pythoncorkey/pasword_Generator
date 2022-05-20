
import random as rand  # here we are importing the random module
import time
print('\U0001F512 password generator \U0001F512')  # we are displaying the name of the program to the user

chars = '1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()'  # we are creating a string with random characters
number = int(input('how many passwords would you like to generate?'))  # we are asking user for password amount
length = int(input('how long would you like your password'))

print('constructing passwords...')
time.sleep(3)

for pwd in range(number):
    passwords = ''
    for i in range(length):
        passwords += rand.choice(chars)

    print(passwords)