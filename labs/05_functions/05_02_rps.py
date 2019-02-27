'''
Code a game of rock paper scissors.

'''


# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(hand):
    if hand == 0:
        a = "scissor"
    elif hand == 1:
        a = "rock"
    elif hand == 2:
        a = "paper"
    else:
        a = "error"
    return a


    # 0 = scissor, 1 = rock, 2 = paper
#
#     # for example if the variable hand is 0, it should return the string "scissor"
#     pass
#
# # function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
    if computer == player:
         return "tie"
    if computer == "rock" and player == "scissor":
         return("computer")
    if computer == "rock" and player == "paper":
         return("player")
    if computer == "paper" and player == "rock":
         return("computer")
    if computer == "paper" and player == "scissor":
         return("player")
    if computer == "scissor" and player == "rock":
         return("player")
    if computer == "scissor" and player == "paper":
         return("computer")



'''
Start here
'''

# take in a number 0-2 from the user that represents their hand

# generate a random number 0-2 to use for the computer's hand

# call the function get_hand to get the string representation of the user's hand

# call the function get_hand to get the string representation of the computer's hand

# call the function determine_winner to figure out the winner

# print out the player hand and computer hand

# print out the winner


import random

my_number = int(input("input 0 or 1 or 2"))
computer_number = random.randint(0,2)



my_hand = (get_hand(my_number))
computer_hand = get_hand(computer_number)

print(my_hand)
print(computer_hand)

print(f"the winner is {determine_winner(computer_hand, my_hand)}")

