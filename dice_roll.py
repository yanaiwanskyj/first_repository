import random
num = list(range(1,7))
while True:
    random_number = random.choice(num)
    print(random_number)
    answer = input("Would you like to roll again? yes/no")
    if answer != "yes":
        break