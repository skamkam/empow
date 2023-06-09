from turtle import *
import time
import random

screen = Screen() #Runs the screen's constructor to create it!
screen.setup(width=500,height=500) #Sets the size of your window in pixels
screen.tracer(0) #Turns off the screen's automatic updates

#Player class
class Player(Turtle):
    def __init__(self): #The constructor, a required function in every class
        Turtle.__init__(self) #Runs the Turtle class constructor
        self.penup()
        self.goto(-200,0)
        self.color('blue')
    
    def turn(self,x,y):
        newHeading = self.towards(x,y)
        self.setheading(newHeading)

#Projectile class
class Projectile(Turtle):
    alive = []
    
    def __init__(self, x, y, heading):
        Turtle.__init__(self)
        self.penup()
        self.shape('arrow')
        self.goto(x,y)
        self.setheading(heading)
        self.alive.append(self)

# Mine class
# destroys projectiles if they run into the mines
class Mine(Turtle):
    alive = []
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.goto(x,y)
        self.alive.append(self)

def play():
    player = Player()
    counter = 0
    while True:
        #Redraw and wait for next frame!
        counter += 1
        screen.update()
        time.sleep(1/60)

        if counter % 11 == 0:
            Projectile(random.randrange(-230,230),random.randrange(-230,230),random.randrange(-230,230))
        if counter % 29 == 0:
            Mine(random.randrange(-230,230),random.randrange(-230,230)) # spawns in a mine at the same time as projectile

        player.forward(4)
        if abs(player.xcor()) > 250 or abs(player.ycor()) > 250:
            player.backward(4)

        screen.onclick(player.turn)

        for p in Projectile.alive:
            p.forward(2)

            if abs(p.xcor()) > 250 or abs(p.ycor()) > 250:
                p.hideturtle()
                Projectile.alive.remove(p)
            else:
                for m in Mine.alive: # danger to projectile so nest in else stmt
                    if p.distance(m) < 15:
                        p.hideturtle()
                        Projectile.alive.remove(p)
                        m.hideturtle()
                        Mine.alive.remove(m) # removes both the projectile and the mine
                        break

            if p.distance(player) < 15:
                screen.clear() #Erase the screen
                hideturtle() #Hide the turtle we're writing with
                write("GAME OVER", align='center',font=('Impact',20,'normal'))
                screen.update() #Refresh so we see the clear screen and text
                time.sleep(3) #Wait for 3 seconds with the text up
                screen.bye() #Close the window
                return #End the game() function! This avoids any errors caused by closing our window early
            


play()