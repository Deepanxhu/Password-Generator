import random
import string

pass_len = 15
charValues = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(pass_len):
    password += random.choice(charValues)

print("Your Random Password is :",password)