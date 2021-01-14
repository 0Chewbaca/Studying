import random as rm

def guessing(a, range_number):

    if(range_number != 10 and range_number != 50 and range_number != 100):
        print("Please write an integer that is in range. Quit!!!")
        exit()
    
    if(range_number == 10):
        chances = 3
    elif(range_number == 50):
        chances = 7
    else:
        chances = 10

    print("You have" +" "+ str(chances)+" " + "chances be careful!")

    while(chances > 0):
        guess = int(input("Try to guess the number: "))
        chances = chances-1
        if a > guess:
            print("The number is bigger. Sorry")
        elif(a < guess):
            print("The number is smaller. Please type a smaller number...")
        else:
            print("Yes. It is correct. Please play again...")
            exit()
        
    print("Unfortunately, you could not guess the correct number. The number was"+" "+ str(a)+" "+ "Try Again")        

def range():
    try:
        range_number = int(input(""" 
-------------------------
Choose the range
-------------------------
Type 10 if you want the range to be 10
Type 50 if you want the range to be 50
Type 100 if you want the range to be 100

Type your choice: """))
    except:
        print("Please write an integer number")
        exit()
    a = rm.randrange(1, range_number)
    guessing(a,range_number)

range()
