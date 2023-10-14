import random
print("""Game Rules
Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.
if you want to choose Rock press 1
if you want to choose paper press 2
if you want to choose scissors press 3""""")


while True:
    player1 = int(input("enter your choice: "))
    if player1>3 or player1<1:
        print("enter valid number")
    elif player1==1:
        print("you choose Rock")
    elif player1==2:
        print("you choose Paper")
    elif player1==3:
        print("you choose scissors")

    print("computer is choosing....")
    player2 = random.randint(1,3)
    if player2==1:
        print("computer choose Rock")
    elif player2==2:
        print("computer choose Paper")
    elif player2==3:
        print("computer choose scissors")

    if player1==player2:
        print("match is draw")
    elif player1==1 and player2==2:
        print("computer won")
    elif player1==1 and player2==3:
        print("you won")
    elif player1==2 and player2==1:
        print("you wins")
    elif player1==2 and player2==3:
        print("computer won")
    elif player1==3 and player2==1:
        print("computer won")
    elif player1==3 and player2==2:
        print("you won")

    rematch = input("rematch?(yes/no): ")
    if rematch=="yes":
        continue
    elif rematch=="no":
        break

