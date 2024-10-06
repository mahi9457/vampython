number = int(input("Enter the number : "))
try:
    i = 0
    while (i<= 10):
        print(f"{number} X {i} = {number*i}")
        i += 1
except:
    print("Invalid Input")

print("Here program is END")