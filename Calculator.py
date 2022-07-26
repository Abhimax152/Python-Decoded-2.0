import math
print(".........WELCOME USER.........")
print("Available Operations:\n" \
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Division\n" \
        "4. Multiplication\n"
        "5. Exponent\n"
        "6. Logarithm\n")
opn = int(input("Select operations form 1, 2, 3, 4, 5, 6 :"))
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if opn == 1:
        print("Sum= ", x+y)
elif opn == 2:
        print("Difference= ", x-y)
elif opn == 3:
        print("Quotient= ", x/y)
elif opn == 4:
        print("Product= ", x*y)
elif opn == 5:
        print("Exponent= ", x**y)
elif opn == 6:
        print("Logarithm= ", math.log(x,y) )
else:
        print("Invalid input")