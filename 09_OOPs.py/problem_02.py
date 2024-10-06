"""
Create Account class with 2 attributes - balance & account no.
Create methods for debit,credit & printing the balance
"""

class bank:
    def info(self):
        balance = int(input("Please enter you total ammount : "))
        condition = input("Your want to credit or debit your money : ")
        if(condition == "debit"):
            debit = int(input("Enter the ammount you want to debit : "))
        elif(condition == "credit"):
            credit = int(input("Enter the ammount you want to credit : "))
        print(f"Your bank acount is {balance}RS")
        if(debit >> 0):
            print(f"Now {balance - debit}Rs left in your account")
        elif(credit>> 0):
            print(f"Now {balance + credit}Rs  in your account")
p1 = bank()
p1.info()
