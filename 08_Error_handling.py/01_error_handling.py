try:
    i = 0
    number = int(input("Enter the number : "))
    while (i<= 10):
        print(f"{number} X {i} = {number*i}")
        i += 1
except ValueError:
    print("Invalid Input")

print("Here program is END")