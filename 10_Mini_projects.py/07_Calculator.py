first_number = int(input())
operation = input()
second_number = int(input())

match operation:
    case "+":
        print(f"{first_number+second_number}")
    case "-":
        print(f"{first_number-second_number}")
    case "*":
        print(f"{first_number*second_number}")
    case "/":
        print(f"{first_number-second_number}")