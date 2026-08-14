from turtle import *
import math


def heart_x(k):
    return 15 * math.sin(k) ** 3


def heart_y(k):
    return (
        12 * math.cos(k)
        - 5 * math.cos(2 * k)
        - 2 * math.cos(3 * k)
        - math.cos(4 * k)
    )


speed(0)
bgcolor("black")
color("red")

for i in range(6000):
    goto(heart_x(i) * 20, heart_y(i) * 20)

goto(0, 0)
done()
