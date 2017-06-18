# tk is a graphics package on which turtle is based.
# Using tk gives you more direct control over the graphics than turtle does.
from tkinter import *
import random
import time

# These two lines set the size of the graphics window.
WIDTH = 400
HEIGHT = 600

tk=Tk()
canvas=Canvas(tk,width=WIDTH,height=HEIGHT)

tk.title("Drawing")
canvas.pack()

# This next command creates an oval. The size and position of the oval are
# determined by an invisible "bounding box" which you  define with the first
# 4 arguments.
# The first two arguments specify the x and y coordinates of one
# corner of the box.
# The third and fourth arguments specify the x and y coordinates of the corner
# diametrically opposite to the first corner you specified. 

ball=canvas.create_oval(10,110,60,160,fill="orange")

xspeed=1  #horizontal speed
yspeed=1  #vertical speed

while True:
    canvas.move(ball,xspeed,yspeed)

    pos = canvas.coords(ball)
    if pos[2]>WIDTH or pos[0]<0:
        xspeed = -xspeed
    if pos[3]>HEIGHT or pos[1]<0:
        yspeed = -yspeed


    tk.update()
    time.sleep(.01)

tk.mainloop()


#CHALLENGES
# 1.  Run the program to see what it does.
# 2.  Change the size and title of the canvas without changing  
#     the call to Canvas. Hint: This requires modifying 3 lines of the code.
# 4.  Change the color of the ball to blue.
# 5.  Change the speeds of the ball so it moves ONLY horizontally.
# 6.  Change the speeds of the ball so it moves ONLY vertically.

#HARDER CHALLENGES
# 1.  Identify the lines that cause the ball to bounce when it hits an edge.
#     Comment out these lines and run the program to see what happens.
#     Uncomment these lines so the program operates normally.
# 2.  Change the size of the circle's bounding box to be a square 200 units
#     on each side instead of 50.
# 3.  Change the shape of the circle's bounding box so it's a rectangle 100 units 
#     wide and 50 units high.
# 4.  Make the bounding box a 50x50 square but start it near the center of the canvas. 
#     Hint: Use the WIDTH and HEIGHT constants at the top of the code to find the 
#     center of the canvas and use this information when you define the ball's bounding
#     box.

#EXPERT CHALLENGE
# Create a second ball of a different size and color that bounces. 
# Hint: Create 3 new variables before the "while" loop then copy most (but not all)
# the lines within the loop and modify them to bounce the second ball you created.
