import turtle

def poly(sides):
    angle = 360 / sides
    for j in range(sides):
        # Draw a side of the polygon
        t.forward(length)
        t.right(angle)

def spiral():
    t.speed(0)

    for i in range(100):
        t.forward(i * 2)
        t.right(30)

pattern_to_draw = input("Enter the number of sides of the pattern or random (3, 4, 5, 6....) or random: ")


t = turtle.Turtle()
t.pencolor("blue")
t.pensize(2)
length = 100

if pattern_to_draw == "random":
    spiral()
else:
    poly(int(pattern_to_draw))


t.hideturtle()
turtle.done()



