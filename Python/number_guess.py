import random

ran = random.randint(1, 99)
if ran:
    print "Number is setted."
guess = int(raw_input("Enter an interger from 1 to 99: "))

while ran != guess:
    if guess < ran:
        print "Guess is too low"
        guess = int(raw_input("Enter an interger from 1 to 99: "))

    elif guess > ran:
        print "Guess is too high"
        guess = int(raw_input("Enter an interger from 1 to 99: "))

    else:
        print "You got it!"
        break
