try:
    year = int(input("Write a year: "))
except:
    print("Please write an appropriate year")
    exit()

if year%4 == 0:
    print("")
    print(str(year) + " is a leap year.")
else:
    print("")
    print("This is not a leap year.")