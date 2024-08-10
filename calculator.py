print("Simple Calculator")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
choice = int(input("Enter your operation choice (1-4): "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operation choice")