print("Welcome to Calculator!")
operator = input("Choose an operator (+ - / *): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    ans = num1 + num2
    print(f"Your answer is {ans}")
elif operator == "-":
    ans = num1 - num2
    print(f"Your answer is {ans}")
elif operator == "/":
    ans = num1 / num2
    print(f"Your answer is {ans}")
elif operator == "*":
    ans = num1 * num2
    print(f"Your answer is {ans}")