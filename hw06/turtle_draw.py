# Draws in the window a spiral surrounded with an octagon

import turtle
import math

# Set the actual parameter for the each draw function call
starSegments = 500

R = starSegments / (2 * math.cos(math.radians(18)))

# Set the each start coordinate point as tuples for the
# turtle pen before draw function call
starBegin = -R * math.cos(math.radians(18)), R * math.sin(math.radians(18))

circleBegin = 0, -R

pentagonBegin = (-R * math.cos(math.radians(18))
                 * math.tan(math.radians(36)) * math.tan(math.radians(18)),
                 R - R*math.cos(math.radians(18)) * math.tan(math.radians(36)))

pentagon_length = 2 * R * math.cos(math.radians(18))\
    * math.tan(math.radians(36)) * math.tan(math.radians(18))


def draw_star(a, x, y):
    global r
    turtle.color(x, y)
    turtle.begin_fill()
    i = 0
    while i < 5:
        turtle.forward(a)
        turtle.right(180-36)
        i += 1
    turtle.end_fill()


def draw_circle(r, x, y):
    turtle.color(x, y)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def draw_pentagon(p, x, y):
    turtle.begin_fill()
    turtle.color(x, y)
    for _ in range(5):
        turtle.forward(p)
        turtle.right(72)
    turtle.end_fill()


def main():
    turtle.penup()
    turtle.goto(*circleBegin)
    turtle.pendown()
    draw_circle(R, "blue", "cyan")
    turtle.penup()
    turtle.goto(*starBegin)
    turtle.pendown()
    draw_star(starSegments, "red", "yellow")
    turtle.penup()
    turtle.goto(*pentagonBegin)
    turtle.pendown()
    draw_pentagon(pentagon_length, "red", "cyan")
    turtle.penup()
    turtle.hideturtle()
    turtle.done()


main()
