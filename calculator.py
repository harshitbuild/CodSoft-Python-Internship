#python program to create a simple calculator
#Function to add two numbers
def add(num1, num2):
    return num1 + num2

#Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

#Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

#Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

#Function to calculate the average of two numbers
def avg(num1, num2):
    return (num1 + num2) / 2

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Average")

select = int(input("Enter choice(1/2/3/4/5): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif select == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
elif select == 5:
    print("Average of", num1, "and", num2, "is", avg(num1, num2))
else:
    print("Invalid input")