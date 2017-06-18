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
    def __init__(self,color,size,myname):
       xctr=WIDTH/2
       yctr=HEIGHT/2
       self.shape = canvas.create_oval(xctr,yctr,xctr+size,yctr+size,fill=color)
       self.name = canvas.create_text(xctr+size/2,yctr+size/2,text=myname)
       self.xspeed = random.randrange(-5,5)
       self.yspeed = random.randrange(-1,1)

    def move(self):
        canvas.move(self.shape,self.xspeed,self.yspeed)    
        canvas.move(self.name,self.xspeed,self.yspeed)    
        pos = canvas.coords(self.shape)
        if pos[2]>WIDTH or pos[0]<0:
            self.xspeed = -self.xspeed
        if pos[3]>HEIGHT or pos[1]<0:
            self.yspeed = -self.yspeed

colors=["red","green","blue","yellow","cyan","turquoise","dodgerblue","magenta","gold","pink","gray","purple","black"]

balls=[]

for i in range(10):
   balls.append(Ball(random.choice(colors),random.randrange(40,100),i))

while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(.01)

tk.mainloop()
