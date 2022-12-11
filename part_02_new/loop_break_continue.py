# break and continue statement

'''
# continue statement

for i in range(1,10):
    if i == 6:
        break
    print(i)

## continue statement
# print 1 to 10 but not 5

for i in range(1,11):
    if i == 5 :
        continue
    print(i)

'''

# Exercise : Modifying number guessing game 

# winning_number = 43
import random
winning_number = random.randint(1, 100)
guess = 1
number = int(input("Enter a number betweeb 1 & 100 : "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"Congrats,you win!& you guessed this number in {guess} times")
        game_over = True
    else:
        if winning_number>number:
            print('Too low')
            # guess+=1
            # number = int(input("guess Again : "))
        else:
            print("Too High")
        guess+=1
        number = int(input("guess Again: "))    
        #DRY = Don't Repeat Yourself





