import random
char="!@#$%&*abcdefghijklmnopqrstuvwxyz1234567890"
password=""
for i in range(9):
    password+=random.choice(char)
print("Genrated Password is:",password)
