# This is a simple password generator that creates a random password of a specified length.
import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+[]{}|;:,.<>?"
length_password = int(input("Enter the length of the password: "))
a = "".join(random.sample(password, length_password)) #random password generator
print("Your password is: ", a)
print("Password length is: ", length_password)
