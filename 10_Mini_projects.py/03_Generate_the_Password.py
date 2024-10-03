import random
import string
pass_len = int(input("Enter your password length : "))
char_value = string.ascii_letters + string.digits 
password = ""
for i in range(pass_len):
    password += random.choice(char_value)
print(f"So your password is {password}")