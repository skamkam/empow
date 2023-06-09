import random

def computer_choice():
    # Get the computer's choice
    rand = random.randint(0, 2)
    if rand == 0:
        return "rock"
    elif rand == 1:
        return "scissors"
    elif rand == 2: # could use else but using elif is clearer code-wise
        return "paper"

def user_choice():
    try:
        user = input("Rock, Paper, or Scissors? Type one of these: ")
        user = user.lower()
        while user not in ["rock", "paper", "scissors"]:
            user = input("Not one of the options, try again: ")
            user = user.lower()
    except:
        print("error, start program again")
    return user

def user_wins(user, comp):
    # is there a good way of determining winner without using nested if's
    if user == "rock":
        if comp == "scissors":
            return True # user won game = True
        else:
            return False
    elif user == "paper":
        if comp == "rock":
            return True
        else:
            return False
    elif user == "scissors":
        if comp == "paper":
            return True
        else:
            return False

def main():
    comp = computer_choice()
    user = user_choice()
    if user == comp:
        print("You and the computer both chose " + user + ". Tie!")
    elif (user_wins(user, comp)): # returns True if user won and False if comp won
        print("You won! You picked "+user+" and the computer picked "+comp+".")
    else:
        print("You lost. You picked "+user+" and the computer picked "+comp+".")
    
if __name__ == "__main__":
    main()