# In the last EXPERT CHALLENGE you created a second bouncing ball by
# copying code and creating extra variables. 
#
# When you're coding it's usually inefficient to copy code since computers
# can rerun code over and over. Why not let the machine do all the work?
#
# In this file we introduce a "class" called Ball which gives you a simple way 
# to reuse code that creates a ball and controls its movement. It does this
# with "methods" which are functions associated with the created ball.
# You can now simply and easily create a ball of the color and size you want. 
# In the following code the speed of the ball will be 
# randomly chosen within a range. The move method of the class moves the ball
# and takes care of the bouncing mechanics.
from tkinter import *
import random
import time

WIDTH = 400
HEIGHT = 600

tk=Tk()

canvas=Canvas(tk,width=WIDTH,height=HEIGHT)

tk.title("Drawing")
canvas.pack()

class Ball:
    def __init__(self,color,size):
      self.shape = canvas.create_oval(10,10,size,size,fill=color)
      self.xspeed = random.randrange(1,8)
      self.yspeed = random.randrange(1,8)

    def move(self):
        canvas.move(self.shape,self.xspeed,self.yspeed)    
        pos = canvas.coords(self.shape)
        if pos[2]>WIDTH or pos[0]<0:
            self.xspeed = -self.xspeed
        if pos[3]>HEIGHT or pos[1]<0:
            self.yspeed = -self.yspeed

newball = Ball("blue",40)
newball2 = Ball("yellow",70)

while True:
    newball.move()
    newball2.move()
    tk.update()
    time.sleep(.01)

tk.mainloop()

# Challenges
#  1. Run the code to see how it behaves.
#  2. Add 3 more balls of different colors and sizes to the program. Name them
#     whatever you want and make sure to have  them move!
# Harder Challenges
#  1. Instead of having xspeed and yspeed take on random values make xspeed and yspeed
#     two arguments for Ball's init method. Make sure to modify your calls to Ball
#     by specifying two values for these new arguments such as newball=Ball("pink",30,4,6).
#  2. Without changing any of the lines in "move" make the balls "crawl". 
#     Hint: Stay Awake!
