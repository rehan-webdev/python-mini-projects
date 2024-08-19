# rock = 1
# paper = 0 
# scissor =-1
import random 
dic = {"rock":1,"paper":0,"scissor":-1}
reversedic = {1:"rock",0:"paper",-1:"scissor"}

computer = random.choice([0,-1,1])
you = input("Enter Rock, Paper or scissor : ").lower()
if you not in dic:
    print("Invalid choice!")
else:
    you = dic[you]   

    print(f"You chose {reversedic[you]}\nComputer choose {reversedic[computer]}")

    if you == 1 and computer == 0:
     print("Both Win!")
    elif you == 1 and computer == -1:
      print("You win!")
    elif you == 0 and computer == 1:
      print("Both win!")
    elif you == 0 and computer == -1:
      print("You Lose!")
    elif you == -1 and computer == 0:
      print("You win!")
    elif you == -1 and computer == 1:
      print("You Lose!")
    elif you == computer and computer == you:
      print("Match Draw!")



