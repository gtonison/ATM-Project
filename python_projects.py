# adj = input("what is programming: ")
# verb1 = input("you to love to what about programming: ")
# why = input("tell us why: ")
# famous = input("you want to  be famous like who ")
# madlib = f"computer programming is so {adj} it makes me so excited all the time because i love to {verb1} stay hydrated and stay self because {why} and why like you are famous like {famous}"
# print(madlib)
user = input("guess the number: ")
import random

def guess(x):
    random_number = random.randint( x,1)
    while True:
     if user and input == True:
         print("youve successfully guessed the number")
         break
    else:
        print("wrong guess")p