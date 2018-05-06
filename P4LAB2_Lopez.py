# CTI-110 
# P4LAB2 - Turtle draws my initials 
# Miguel Lopez 
# 3/25/2018
#

import turtle


win = turtle.Screen()  
tme = turtle.Turtle()

# add some display options
tme.pensize(5)            
tme.pencolor("red")     
tme.shape("turtle")

#commands to draw initials

tme.left(90)
tme.forward(100)
tme.right(150)
tme.forward(50)
tme.left(120)
tme.forward(50)
tme.right(150)
tme.forward(100)

tme.penup()
tme.left(90)
tme.forward(50)
tme.pendown()
tme.left(90)
tme.forward(100)
tme.backward(100)
tme.right(90)
tme.forward(55)
tme.penup()
tme.forward(50)


    
    
    
    



win.mainloop()             
