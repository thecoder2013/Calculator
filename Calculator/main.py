print("Welcome to Calculator!")
operator = input("Choose an operator (+ - / * % //): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    ans = num1 + num2
    print(f"Your answer is {ans}")
elif operator == "-":
    ans = num1 - num2
    print(f"Your answer is {ans}")
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by 0!")
    else:
        ans = num1 / num2
        print(f"Your answer is {ans}")
elif operator == "*":
    ans = num1 * num2
    print(f"Your answer is {ans}")
elif operator == "%":
    ans = num1 % num2
    print(f"Your answer is {ans}")
elif operator == "//":
    ans = num1 // num2
    print(f"Your anser is {ans}")
else:
    print("Choose a Valid Operator")
finish = input("Do you want to quit? (Yes/No) ")
while finish.lower() == "no":
    operator = input("Choose an operator (+ - / * % //): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if operator == "+":
        ans = num1 + num2
        print(f"Your answer is {ans}")
    elif operator == "-":
        ans = num1 - num2
        print(f"Your answer is {ans}")
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by 0!")
        else:
            ans = num1 / num2
            print(f"Your answer is {ans}")
    elif operator == "*":
        ans = num1 * num2
        print(f"Your answer is {ans}")
    elif operator == "%":
        ans = num1 % num2
        print(f"Your answer is {ans}")
    elif operator == "//":
        ans = num1 // num2
        print(f"Your anser is {ans}")
    else:
        print("Choose a Valid Operator")
    again = input("Do you want to quit? (Yes/No) ")
    if again.lower() == "yes":
        break
print("Goodbye")