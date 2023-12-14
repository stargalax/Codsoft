import random
options = ["rock", "paper", "scissors"]
def check(user):
    if user in options:
        game(user)
    elif user =="end":
        print("Thanks for playing!")
    else:
        print("Enter a valid input")
def game(user):
    global userscore,comscore
    com = random.choice(options)
    print("You chose: ", user)
    print("Computer chose: ", com)
    if user  == com:
        print("It's a tie!")
    elif user  == "rock" and com == "scissors":
        print("You win!")
        userscore +=1
    elif user  == "paper" and com == "rock":
        print("You win!")
        userscore +=1
    elif user  == "scissors" and com == "paper":
        print("You win!")
        userscore +=1
    else:
        print("Computer wins!")
        comscore +=1
def display():
    print("\nFinal Scores:","\nUser:",userscore,"\nComputer:",comscore)
#main
userscore,comscore=0,0

print("**Rock Paper Scissors Game**")
print("Enter 'end' to end game and see your scores!!")
while True:
    user = input("Choose Rock, Paper, or Scissors: ").lower()
    check(user)
    if user=="end":
        display()
        break
    
    
