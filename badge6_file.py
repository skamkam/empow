import time

starttime = time.time()

filename = input("Which madlib would you like? ")
try:
    with open(filename, "r") as f:
        madlib = f.read() 
except FileNotFoundError:
    print("Sorry, I couldn't open {}".format(filename))
    exit()

my_story = ""

len = len(madlib)
i = 0
while i < len: # seek by character
    if madlib[i] == "<":
        start = i + 1 # character after "<"
        end = madlib.find(">", start) # find index of the next ">", starting from current "<"
        print("Can you give me a {}? ".format(madlib[start:end]), end="") # slice, non-inclusive of the ">"
        my_story += input()
        i = end # set index to the last ">", used a while loop to be able to skip ahead
    else: # can just add the characters
        my_story += madlib[i]
    i += 1

print("\n" + my_story)