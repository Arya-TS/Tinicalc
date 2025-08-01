def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


action = True
while action:
    x = int(input("Enter num1: "))
    y = int(input("Enter num2: "))

    choice = input("What do you want to do? (+,-,*,/): ")

    if choice == '+':
        result = add(x, y)
    elif choice == '-':
        result = subtract(x, y)
    elif choice == '*':
        result = multiply(x, y)
    elif choice == '/':
        if y == 0:
            result = "Can't divide by zero!"
        else:
            result = divide(x, y)
    else:
        print("Invalid operator!")

    print(f"Your output is {result}!")

    while True:
        keep_going = input("Do you want to try again? (y/n): ").lower()
        if keep_going == 'y':
            action = True
            break
        elif keep_going == 'n':
            action = False
            break
        else:
            print("Please enter only 'y' or 'n'. Let's try that again!")

print("See you later!")
