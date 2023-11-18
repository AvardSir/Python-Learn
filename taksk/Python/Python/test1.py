class Items(object):


    def __init__(self, Itemss):
        """Constructor"""
        self.Itemss_=Itemss

    def add(self):
        return "Braking"
print('go')
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
tryandle()