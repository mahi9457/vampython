def sum(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    return n*sum(n-1)
n = int(input("Enter the number : "))
print(sum(n))