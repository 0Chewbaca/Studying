def Factorial(number):
    a = 1

    for c in range (1, number+1):
        a = a * c
    
    print("")
    print("The result is: " + str(a))

print("""
----------------
Factroial App
----------------
""")
number = int(input("Please type your number that you want to learn the factorial of: "))

Factorial(number)