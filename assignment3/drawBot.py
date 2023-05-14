import turtle
import random


def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)


def draw_triangle(size):
    for i in range(3):
        t.forward(size)
        t.right(120)


def draw_circle(size):
    t.circle(size)



screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.pencolor('blue')
t.pensize(3)




while True:
    shape = input("Enter the shape you want to draw (square, triangle, circle): ")
    size = int(input("Enter the size of the shape: "))


    if shape == 'square':
        draw_square(size)
    elif shape == 'triangle':
        draw_triangle(size)
    elif shape == 'circle':
        draw_circle(size)
    else:
        print("Invalid shape")
        break

    t.penup()
    t.goto(random.randint(-150, 150), random.randint(-150, 150))
    t.pendown()


t.hideturtle()
turtle.done()

