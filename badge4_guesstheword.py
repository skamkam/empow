import random

def guessWord():
    wordlist = ["test", "word", "rhythm", "mystic"]

    randnum = random.randint( 0, len(wordlist) ) # get rand num between 0 and length of wordlist
    secret = wordlist[randnum - 1] # -1 because of 0-based indexing
    so_far = ["_"] * len(secret)
    guesses = [] # start with an empty string of guesses
    turns = 5 # can change this number

    still_playing = True

    
    # GAME LOOP
    while (still_playing) and (turns > 0): # while the total word guessed is not the secret word, ie, game isn't over yet
        print("You have " + str(turns) + " turns left!")
        print("Your guesses so far are: " + str(so_far))
        
        guess = input("Guess a letter: ") # guess 1 letter
        guesses = guesses.append(guess)

        if guess in guesses: # check if the letter is in the already-guessed letters
            print("You already guessed that letter!")

        elif guess not in secret: # if letter isn't in guesses and isn't in secret...
            print("Your guessed letter, " + guess + ", isn't in the secret word")


        elif guess in secret: # if the guess is in secret and hasn't been guessed already
            for i in range(len(secret)): # looping over the length of secret word
                if guess == secret[i]: # compare the guessed letter to the letter whose index we're on
                    so_far[i] = guess # update so_far so that its guessed letter matches the secret


        # check if the game is won yet
        correct = 0
        for i in range(len(secret)):
            if so_far[i] == secret[i]: # check if the secret's letter at that index is the same as so_far's index
                correct = correct + 1
                
        if correct == len(secret): # if the number of correct letters are the same as the length of the secret word, then all of so_far is correct
            still_playing = False
            turns = turns + 1

        turns = turns - 1

    # IS THE GAME OVER?
    # if the game was lost, ie, not all letters were guessed before turns ran out
    if turns == 0:
        print("You ran out of turns! The secret word was: " + secret)
    else: # if the game wasn't ended because you ran out of turns
        print("You won! Your word was: " + secret)



guessWord()
