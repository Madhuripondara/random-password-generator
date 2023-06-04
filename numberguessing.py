#guessing a number
import random
computer=random.choice(range(0, 10))
print(computer)
my_guess=int(input("guess a number:"))
guessed_numbers=[]
while True:
    if my_guess<computer:
        print("too low")
        my_guess1=int(input("guess a number:"))
        if my_guess1==my_guess:
            print("you already entered this number,enter another number")
        my_guess=my_guess1
        if my_guess in guessed_numbers:
                print("you already entered this number,enter another number")
        guessed_numbers.append(my_guess)
    elif my_guess>computer:
        print("too high")
        my_guess2=int(input("guess a number:"))
        if my_guess2==my_guess:
            print("you already entered this number,enter another number")
        my_guess=my_guess2
        if my_guess in guessed_numbers:
               print("you already entered this number,enter another number")
        guessed_numbers.append(my_guess)
    else:
        print("you guessed it right")
        break
