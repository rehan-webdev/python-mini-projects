from random import randint 
r = randint(1,50)
n = int(input("Enter the number of attempts: "))
attempt = 0
while attempt<n:
    attempt +=1
    guess = int(input("Enter the Guess: "))
    if guess > r:
        print(f"Lower number Please!. Attempts Used = {attempt}")
    elif guess < r:
        print(f"Higher number Please!. Attempts used = {attempt} ")
    elif guess == r:
        print(f"You won the Game. The correct answer is {r}.") 
        break
else:
    print(f"You have used all {n} attempts. The correct number was {r}")         
