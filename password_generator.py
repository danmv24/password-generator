import random

lenght = int(input("Enter password length: "))
upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_chars = "abcdefghijklmnopqrstuvwxyz"
special = "[]{}()*;:/_^%$#~`№@!-"
numbers = "1234567890"
together = upper_chars + lower_chars + special + numbers
password = "".join(random.sample(together, lenght))
print(password)