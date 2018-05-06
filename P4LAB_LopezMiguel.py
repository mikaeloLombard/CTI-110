# CTI-110 
# P4LAB- Snow Flake
# Miguel Lopez 
# 3/25/2018
#

import turtle
def main():
    
    me= turtle.Turtle()

    

    me.penup()
    me.forward(80)
    me.left(50)
    me.pendown()

    for i in range(8):
        me.forward(80)
        me.right(55)
        for i in range(2):
            for i in range(2):
                me.forward(30)
                me.backward(30)
                me.right(45)
            me.left(90)
            me.backward(30)
            me.left(45)
        me.right(90)
        me.forward(90)






main()
