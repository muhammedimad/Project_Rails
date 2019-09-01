import random

num = random.randint(1, 9)

guess = 0
counter = 0

while (guess != num and guess != 'exit'):
    guess = input("Enter a number")
    if guess == "exit":
        break

    guess = int(guess)
    counter += 1

    if guess < num:
        print("too low")
    elif guess > num:
        print("too high")
    else:
        print('right answer after ',counter,'trials')



