import turtle



object_to_draw = input("Enter the object you want to draw (square, circle or triangle): ")


t = turtle.Turtle()
t.speed(0)

if object_to_draw == "square":
    for i in range(4):
        t.forward(100)
        t.right(90)
elif object_to_draw == "triangle":
    for i in range(3):
        t.forward(100)
        t.left(120)
elif object_to_draw == "circle":
    t.circle(50)
else:
    print("Invalid object...")



t.hideturtle()

turtle.done()
