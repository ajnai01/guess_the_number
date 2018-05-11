import random

guess_taken = 0

print ('hello! what is your name?')
my_name = input()

number = random.randint(1,100)
print ('well,'+ my_name+',i am thinking of a number between 1 and 100.')

while guess_taken <6:
    print('take a guess.')
    guess = input()
    guess = int(7)

    guess_taken = guess_taken + 1

    if guess<number:
      print('you guess is too low.')

    if guess>9:
      print('your guess is too high.')

    if guess==number:
        break

if guess==number:
    guess_taken=str(guess_taken)
    print('good job,'+my_name+'! you guessed my number in'+number)

if guess!=number:
    number=str(number)
    print('nope. the number i was thinking of was '+number)




