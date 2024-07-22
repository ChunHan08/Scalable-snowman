import turtle
radius1 = float(input("How big is the first circle?: "))
radius2 = float(input("How big is the second circle?: "))
radius3 = float(input("How big is the third circle?: "))
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("grey")

def Snowman(x, y, radius1, radius2, radius3):
  turtle.goto(x, y)
  turtle.color("light blue")
  turtle.begin_fill()
  turtle.circle(radius1)
  turtle.end_fill()
  turtle.up()
  turtle.right(90)
  turtle.forward(radius2 * 2)
  turtle.left(90)
  turtle.begin_fill()
  turtle.circle(radius2)
  turtle.end_fill()
  turtle.up()
  turtle.right(90)
  turtle.forward(radius3 * 2)
  turtle.left(90)  
  turtle.begin_fill()
  turtle.circle(radius3)
  turtle.end_fill()
  turtle.color("blue")
  turtle.left(90)
  turtle.forward(radius3*2+radius2*2+radius1)
  turtle.left(-90)
  turtle.forward(radius1/2)
  turtle.begin_fill()
  turtle.circle(radius1/6)
  turtle.end_fill()
  turtle.left(180)
  turtle.forward(radius1)
  turtle.right(180)
  turtle.begin_fill()
  turtle.circle(radius1/6)
  turtle.end_fill()
  turtle.forward(radius1/2)
  turtle.right(90)
  turtle.color("red")
  turtle.begin_fill()
  turtle.forward(radius1/2)
  turtle.left(120)
  turtle.forward(radius1/2)
  turtle.left(120)
  turtle.forward(radius1/2)
  turtle.end_fill()
  turtle.setheading(270)
  turtle.forward(radius1)
  for x in range(3):
      turtle.forward(radius2/2)
      turtle.begin_fill()
      turtle.circle(radius1/6)
      turtle.end_fill()
  turtle.left(90)
  
def draw():
  turtle.tracer(0, 0)
  Snowman(x, y, radius1, radius2, radius3)
  Snowman(x+120, y, radius1, radius2, radius3)
  Snowman(x+-120, y, radius1, radius2, radius3)
  turtle.update()
  
def left():
  global x
  turtle.clear()
  x -= 10
  draw()
  
def right():
  global x
  turtle.clear()
  x += 10
  draw()
  
x = 0
y = 0 
draw()

turtle.onkeypress(left, "a")
turtle.onkeypress(right, "d")

turtle.listen()
turtle.mainloop()