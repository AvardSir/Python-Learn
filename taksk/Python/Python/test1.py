class Items(object):


    def __init__(self, Itemss):
        """Constructor"""
        self.Itemss_=Itemss

    def add(self):
        return "Braking"
####
##
import turtle

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("white")

    circle = turtle.Turtle()
    #circle.shape("turtle circle.color")
    circle.speed(2)

    circle.circle(100)

    turtle.done()

#draw_circle()



def tryandle():
    import turtle
    # создаем экземпляр черепашки
    t = turtle.Turtle()

    # рисуем треугольник
    for i in range(3):
        t.forward(100)
        t.left(120)

    # скрываем черепашку и закрываем окно по клику
    t.hideturtle()
    turtle.done()
#tryandle()

import turtle

def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_star(x, y, color, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_us_flag():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")

    stripe_height = 20
    field_height = 7 * stripe_height
    field_width = 13 * stripe_height * 2
    star_space = stripe_height * 7 / 6
    star_size = field_height / 10

    turtle.penup()
    turtle.goto(-field_width / 2, field_height / 2)
    for _ in range(13):
        if turtle.ycor() % (2 * stripe_height) == 0:
            draw_rectangle("red", field_width, stripe_height)
        else:
            draw_rectangle("white", field_width, stripe_height)
        turtle.right(90)
        turtle.forward(stripe_height)
        turtle.right(90)
        turtle.forward(field_width)
        turtle.left(180)

   # Draw the blue field
    turtle.goto(-field_width / 2, field_height / 2)
    draw_rectangle("blue", field_width / 2, field_height)

    # Draw the stars
    turtle.color("white")
    turtle.pensize(2)
    x_offset = -field_width / 2 + 11/5*star_space
    y_offset = field_height / 2 - star_space
    turtle.goto(x_offset, y_offset)
    star_gap = 2 * 1/6*star_space
    for row in range(9):
        for col in range(11):
            if row % 2 == 0:
                x = x_offset + row * 2 * star_gap
            else:
                x = x_offset + star_gap + row * 2 * star_gap

            y = y_offset - col * star_gap
            if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
                draw_star(x, y, "white", star_size)
    turtle.done()

draw_us_flag()