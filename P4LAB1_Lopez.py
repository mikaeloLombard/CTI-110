# CTI-110 
# P4LAB1 - Turtle draws a square and a triangle 
# Miguel Lopez 
# 3/25/2018
#

import turtle


win = turtle.Screen()  
tme = turtle.Turtle()

# add some display options
tme.pensize(5)            
tme.pencolor("blue")     
tme.shape("turtle")

#commands to draw a square first then a triangle


for x in range(4):
    tme.forward(120)
    tme.left(90)

tme.penup()
tme.forward(300)
tme.pendown()
          
for x in range(3):
    tme.forward(100)          
    tme.left(120)            
    tme.forward(100)
    
    
    
    



win.mainloop()             
