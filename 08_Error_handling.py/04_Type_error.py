amount = 500
name = "Mahi"
try:
    total = amount + name
    print(total)
except TypeError:
    print("You can't add a string and interger")