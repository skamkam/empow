import requests

def user_search(db):
    """
    Searches through the dictionary database
    of Star Wars characters and tries to find
    the one with the name matching user's input
    """
    char = input("\nWhich Star Wars character do you want info about? ").strip()
    for guy in db: # iterate across characters in db
        if guy["name"] == char: # if the char's name is the same as user input
            return(guy)
    return -1

def main():
    # Read in the API and turn the data into a dictionary
    req = requests.get("https://swapi.dev/api/people")
    results = req.json()
    db = results["results"]

    # Ask the user for SW characters and print out info about them
    # Ask the user if they want to keep querying
    query = True
    while query:
        guy = user_search(db) # character result of choice
        if guy == -1: # failed search
            print("That isn't a character in our Star Wars database, sorry!")
        else:
            print(guy["name"] + " is " + guy["height"] + "cm tall and has " + guy["hair_color"] + " hair.")
        
        keep_playing = input("Ask about another character? Y/N: ")
        if keep_playing == "Y":
            query = True
        elif keep_playing == "N":
            print("Okay, bye!")
            query = False
        else:
            print("That wasn't an option. Program ending now.")
            query = False

if __name__ == "__main__":
    main()