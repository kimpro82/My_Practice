import turtle
import time

turtle.setup(width = 300, height = 300)
turtle.title("My turtle practice")

turtle.hideturtle()         # hide turtle : make the moving speed faster


turtle.home()               # set the position (0, 0)
turtle.position()

turtle.penup()              # penup() = pu() = up() : move without drawing
turtle.setpos(0, 125)

turtle.pendown()            # pendown() = pd() = down() : move with drawing
turtle.right(180)
turtle.circle(125)          # 1st circle

turtle.penup()
turtle.setpos(0, 100)

turtle.pendown()
time.sleep(0.3)
turtle.circle(100)          # 2nd circle

turtle.delay(20)

time.sleep(0.5)
turtle.circle(100, steps=3) # 1st triangle

turtle.penup()
turtle.setpos(0, -100)
turtle.right(180)

turtle.pendown()
turtle.circle(100, steps=3) # 2nd triangle

turtle.penup()
turtle.setpos(0, 100)
turtle.right(180)

turtle.delay(30)

turtle.pendown()
turtle.circle(100, steps=6) # hexagon


turtle.mainloop()           # avoid the screen closing