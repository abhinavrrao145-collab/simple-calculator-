#introduction to my calculator project 
print("Welcome to abhinav's calculator project")
print("This is a simple calculator that can perform basic arithmetic operations.")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c =int(input("Enter the operation you want to perform: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))

if c == 1:
    print("The sum of", a, "and", b, "is:", a + b)
elif c == 2:
    print("The difference of", a, "and", b, "is:", a - b)
elif c == 3:
    print("The product of", a, "and", b, "is:", a * b)
elif c == 4:
    print("The quotient of", a, "and", b, "is:", a / b)
else:
    print("Invalid operation")
    
    