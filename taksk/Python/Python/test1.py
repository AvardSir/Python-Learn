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

draw_circle()
