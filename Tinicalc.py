import math

print("Welcome to Tini calculator!🧸")
print("Available operators: + - * / ** % sq sqrt fact")

while True:
    op = input("Enter the op: ").lower()

    # One-number operations
    if op in ["sq", "square", "sqrt", "fact", "factorial"]:
        try:
            num = float(input("Enter your number: "))

            if op in ["sq", "square"]:
                result = num ** 2

            elif op == "sqrt":
                if num >= 0:
                    result = math.sqrt(num)
                else:
                    result = "Can't take the square root of a negative number🥺"

            elif op in ["fact", "factorial"]:
                if num >= 0 and num.is_integer():
                    result = math.factorial(int(num))
                else:
                    result = "Factorial only works for non-negative whole numbers😣"

        except:
            result = "😣 Invalid input!"

    # Two-number operations
    else:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Can't divide by zero🥺"
            elif op == "**":
                result = num1 ** num2
            elif op == "%":
                result = num1 % num2
            else:
                result = "Invalid operator🥺"

        except:
            result = "😣 Invalid input!"

    # Output & Emoji Feedback
    print("🧠 Result = ", result)

    if isinstance(result, (int, float)):
        if result == 0:
            print("🤐 That's a zero... Mysterious!")
        elif result < 5:
            print("🐣 So tiny!")
        elif result <= 100:
            print("😃 Well done!")
        else:
            print("😲 That's a big brain number!")
    elif isinstance(result, str) and "invalid" in result.lower():
        print("🫣 Did you mean something else?")

    again = input("Wanna try again 😼?(yes/no): ")
    if again.lower() != "yes":
        print("Bye for now 👋 You're amazing 😽")
        break
