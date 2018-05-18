import random

guess_taken = 0

print ('hello! what is your name?')
my_name = input()

number = random.randint(1,100)
print ('well,'+ my_name +'i am thinking of a number between 1 and 100.')

user_guess=0

while user_guess != number:
    user_guess = int(input("Take guess: "))

    if user_guess<number:
      print( my_name  +  'your guess is too low.')

    elif user_guess>number:
      print( my_name  +  'your guess is too high.')

    elif user_guess==number:
        print( my_name +  "you figured it out!" + 'congrats!!')
        break


