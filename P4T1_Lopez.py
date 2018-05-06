import turtle


win = turtle.Screen()  
tme = turtle.Turtle()

# add some display options
tme.pensize(5)            # increase pensize (takes integer)
tme.pencolor("blue")     # set pencolor (takes string)
tme.shape("turtle")

#commands from here to the last line can be replaced
# triangle, sides are 360 / 3 = 120 degrees

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
    
    
    
    


# end commands
win.mainloop()             # Wait for user to close window
