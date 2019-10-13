import random

guess = random.randint(1, 10)

print(guess)
inputnum = int(input('input a numner'))

flag = 2
while inputnum != guess:

    if flag == 0:
        print('You lose')
        break
    elif inputnum > guess:
        print('Try it less')
        inputnum = int(input('again:'))
        flag -= 1
    elif inputnum < guess:
        print('Try it Grater')
        inputnum = int(input('again:'))
        flag -= 1

else:
    print('Your are right the number is ', guess)
