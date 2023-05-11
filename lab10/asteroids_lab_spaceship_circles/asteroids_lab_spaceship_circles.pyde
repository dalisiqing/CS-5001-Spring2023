SIZE = (600, 600)
STROKE_WEIGHT = 3
SPACESHIP_POINTS = (-16, 10,  0, -30, 16, 10)
THRUST_INCREMENT =0.5
ROTATION_INCREMENT = 3

thrust_factor = 0
spaceship_x = 300
spaceship_y = 300
x_vel = 0
y_vel = 0
rotation = 0

SIZE_X = 600
SIZE_Y = 600
CIRCLE_RAD = 75
CIRCLE_X_INCREMENT = 1
CIRCLE_Y_INCREMENT = 1
GRAY_COLOR = (0.5, 0.5, 0.5)
WHITE_COLOR = (1.0, 1.0, 1.0)
LIGHT_BLUE_COLOR = (0.8, 0.9, 1.0)
STROKE_WEIGHT = 3

circle_x = 300
circle_2_x = 300
circle_1_y = 100
circle_2_y = 300
circle_3_y = 500


def setup():
    size(SIZE_X, SIZE_Y)
    strokeWeight(STROKE_WEIGHT)
    colorMode(RGB, 1)


def draw():
    global circle_x
    global circle_2_y
    background(0)
    circle_x = circle_x + CIRCLE_X_INCREMENT
    circle_2_y = circle_2_y + CIRCLE_Y_INCREMENT

    if circle_2_y > SIZE_Y + CIRCLE_RAD:
        circle_2_y = circle_2_y - SIZE_Y
    elif circle_2_y > SIZE_Y - CIRCLE_RAD:
        draw_circle_2(circle_2_y - SIZE_Y)

    draw_circle_2(circle_2_y)
    
    global rotation
    draw_spaceship()

    if circle_x > SIZE_X + CIRCLE_RAD:
        circle_x = circle_x - SIZE_X
    elif circle_x > SIZE_X - CIRCLE_RAD:
        draw_circle_1(circle_x - SIZE_X)
        draw_circle_3(circle_x - SIZE_X)

    draw_circle_1(circle_x)
    draw_circle_3(circle_x)


def draw_circle_1(x):

    fill(*GRAY_COLOR)
    stroke(*WHITE_COLOR)
    ellipse(x, circle_1_y, CIRCLE_RAD*2, CIRCLE_RAD*2)


def draw_circle_2(y):
    fill(*LIGHT_BLUE_COLOR)
    stroke(*WHITE_COLOR)
    ellipse(circle_2_x, y, CIRCLE_RAD*2, CIRCLE_RAD*2)


def draw_circle_3(x):
    fill(*GRAY_COLOR)
    stroke(*WHITE_COLOR)
    ellipse(x, circle_3_y, CIRCLE_RAD*2, CIRCLE_RAD*2)


def keyPressed():
    global rotation
    global thrust_factor
    if (key == CODED):
        if keyCode == UP:
            thrust_factor = THRUST_INCREMENT
        if keyCode == RIGHT:
            rotation += ROTATION_INCREMENT
        if keyCode == LEFT:
            rotation -= ROTATION_INCREMENT


def draw_spaceship():
    global spaceship_x
    global spaceship_y
    global x_vel
    global y_vel
    global thrust_factor
    x_vel = (x_vel + sin(radians(rotation))) * thrust_factor
    y_vel = (y_vel - cos(radians(rotation))) * thrust_factor

    spaceship_x = spaceship_x + x_vel
    spaceship_y = spaceship_y + y_vel
    translate(spaceship_x, spaceship_y)
    rotate(radians(rotation))
    fill(0)
    stroke(1)
    strokeWeight(STROKE_WEIGHT)
    triangle(*SPACESHIP_POINTS)

    rotate(radians(-rotation))
    translate(-spaceship_x, -spaceship_y)
