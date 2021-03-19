try:
    def decimalToBinary(n):
        if n > 1:
            decimalToBinary(n//2)

        print(n%2, end='')

    def binaryToDecimal(n):
        print(int(n,2))

    print("""
    ---------------------
    1- Decimal To Binary
    2- Binary To Decimal
    ---------------------
    """
    )

    choice = int(input("Choose what to do: "))
    if choice != 1 and choice != 2:
        print("Please type a number that is in range")
        exit()
    number = str(input("Type your number: "))

    if choice == 1:
        decimalToBinary(number)
    elif choice == 2:
        binaryToDecimal(number)

except Exception as err:
    print(err)
