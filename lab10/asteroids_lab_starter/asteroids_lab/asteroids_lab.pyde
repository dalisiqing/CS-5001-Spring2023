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


def setup():
    size(*SIZE)
    colorMode(RGB, 1)


def draw():
    global rotation
    background(0)
    draw_spaceship()


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
