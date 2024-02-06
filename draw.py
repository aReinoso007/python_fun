from turtle import *
from colorsys import *

bgcolor('black')
speed(0)
h=0
t = Turtle()
for i in range(371):
    t.screen.title('Flower')
    c= hsv_to_rgb(h,1,1)
    h+=0.005
    color(c)
    circle(-i*0.68, 200)
    right(80)
done()