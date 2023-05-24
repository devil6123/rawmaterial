import random

def get_choices():
    player_choice=input(":Rock,:paper,:scissors  ")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice, "computer":computer_choice}

    return choices

# def check_win(player,computer):
#     print("you choose "+ player + " computer choose "+computer)
#     if player == computer:
#         return "it is atie!"
#     elif player =="rock" and computer == "scissors":
#         return "You win"
#     elif player=="scissors" and computer =="rock":
#         return "computer wins"
#     elif computer == "rock" and player == "paper":
#         return "You won"
#     elif computer=="paper" and player=="rock":
#         return "computer wins"
#     elif computer=="scissors" and player == "paper":
#         return "computer wins"
#     elif computer=="paper" and player=="scissors":
#         return "You won"
#     else:
#         return "invalid entry!!"

# choices=get_choices()
# result=check_win(choices["player"],choices["computer"])
# print(result)


def check_win(player,computer):
    print("you choose "+ player + " computer choose "+computer)
    if player == computer:
        return "it is a tie!"
    elif player =="rock":
        if computer=="scissors":
            return "You won!"
        else:
            return "you Lose!"
    
    elif player =="paper":
        if computer=="rock":
            return "You won!"
        else:
            return "you Lose!"
        
    elif player =="scissors":
        if computer=="paper":
            return "You won!"
        else:
            return "you Lose!"
choices=get_choices()
result=check_win(choices["player"],choices["computer"])
print(result)
