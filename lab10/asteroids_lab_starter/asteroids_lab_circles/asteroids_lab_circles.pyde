SIZE_X = 600
SIZE_Y = 600
CIRCLE_RAD = 75
CIRCLE_X_INCREMENT = 1
GRAY_COLOR = (0.5, 0.5, 0.5)
WHITE_COLOR = (1.0, 1.0, 1.0)
LIGHT_BLUE_COLOR = (0.8, 0.9, 1.0)
STROKE_WEIGHT = 3

circle_x = 300
circle_1_y = 100
circle_2_y = 300
circle_3_y = 500


def setup():
    size(SIZE_X, SIZE_Y)
    strokeWeight(STROKE_WEIGHT)
    colorMode(RGB, 1)


def draw():
    global circle_x
    background(0)
    circle_x = circle_x + CIRCLE_X_INCREMENT

    if circle_x > SIZE_X + CIRCLE_RAD:
        circle_x = circle_x - SIZE_X
    elif circle_x > SIZE_X - CIRCLE_RAD:
        draw_circle_1(circle_x - SIZE_X)
        draw_circle_2(circle_x - SIZE_X)
        draw_circle_3(circle_x - SIZE_X)
    draw_circle_1(circle_x)
    draw_circle_2(circle_x)
    draw_circle_3(circle_x)


def draw_circle_1(x):
    fill(*GRAY_COLOR)
    stroke(*WHITE_COLOR)
    ellipse(x, circle_1_y, CIRCLE_RAD*2, CIRCLE_RAD*2)


def draw_circle_2(x):
    fill(*LIGHT_BLUE_COLOR)
    stroke(*WHITE_COLOR)
    ellipse(x, circle_2_y, CIRCLE_RAD*2, CIRCLE_RAD*2)


def draw_circle_3(x):
    fill(*GRAY_COLOR)
    stroke(*WHITE_COLOR)
    ellipse(x, circle_3_y, CIRCLE_RAD*2, CIRCLE_RAD*2)
