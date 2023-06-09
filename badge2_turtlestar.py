import turtle as t
import random

def grabcolor():
    # returns a random tuple of RGB colors
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

if __name__ == "__main__": # ha here's my if statement
    t.speed=(10)
    t.colormode(255)

    counter = 24
    while counter > 0: # draw a 24 pointed star. using a while loop to fulfill badge
        counter -= 1
        t.color(grabcolor())
        for j in range(2): # out of kite shapes!
            t.forward(100)
            t.right(30)
            t.forward(100)
            t.right(150)
        t.right(15)