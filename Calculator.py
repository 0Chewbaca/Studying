class Calculator:
    def Calculate(self, number1, number2, operation):
        if(operation == 1):
            return number1 + number2
        elif(operation == 2):
            return number1 - number2
        elif(operation == 3):
            return number1 * number2
        elif(operation == 4):
            return number1 / number2
        else:
            print("")
            print("Please type a number that is in the range")
            exit()


calculator = Calculator()

try:
    number1 = float(input("First Number: "))
    number2 = float(input("Second Number: "))
except:
    print("Please type an appropriate number!")
    exit()

print("""
------------------------------------------------
Please decide the operation you want to use
------------------------------------------------
Type 1 if you want to add these numbers

Type 2 if you want to substract these numbers

Type 3 if you want to multiply these numbers

Type 4 if you want to divide these numbers
------------------------------------------------
""")

try:
    op = int(input("Type the number that belongs to the operation you want to use: "))
except:
    print("Please type a number that is in the range")
    exit()

result = calculator.Calculate(number1, number2, op)
print("")
print("The result is: " + str(result))