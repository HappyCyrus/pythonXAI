import random
minimun, maximun = 1, 100
ans = random.randrange(1, 101)
while True: 
    guess = int(input(f"Guess a number between {minimun} and {maximun}: "))
    if ans == guess:
        print("You got it!")
        break
    elif guess > ans:
        print("Too high!")
        maximun = guess
    else:
        print("Too low!")
        minimun = guess

