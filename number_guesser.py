import random
num = random.choice(range(1,10001))
while True:
    guess = int(input("guess a number between 1 and 10000"))
    if guess > 10000:
        print("out of range")
    elif guess > num:
        print("too high")
    if guess == num:
        print("correct")
        break
    if guess < num:
        print("too low")
        