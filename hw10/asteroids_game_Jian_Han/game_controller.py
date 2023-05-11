from laserbeam import LaserBeam
from asteroid import Asteroid
from spaceship import Spaceship
from math import sqrt


class GameController:
    """
    Maintains the state of the game
    and manages interactions of game elements.
    """

    def __init__(self, SPACE, fadeout):
        """Initialize the game controller"""
        self.SPACE = SPACE
        self.fadeout = fadeout

        self.spaceship_hit = False
        self.asteroid_destroyed = False
        self.asteroids = [Asteroid(self.SPACE)]
        self.laser_beams = []
        self.spaceship = Spaceship(self.SPACE)
        self.blow_up_move = 5

    def update(self):
        """Updates game state on every frame"""
        self.do_intersections()

        for asteroid in self.asteroids:
            asteroid.display()

        # ======================================================
        # TODO: Problem 3, Part 2: Laser beam handler
        # Your code will replace (or augment) the next several
        # lines. Laser beam objects should remain in the scene
        # as many frames as their lifespan allows.
        # Begin problem 3 code changes
        l = 0
        while l < len(self.laser_beams):
            if self.laser_beams[l].lifespan <= 0:
                del self.laser_beams[l]
                l -= 1
            else:
                self.laser_beams[l].display()
            l += 1

        # End problem 3, part 2 code changes
        # =======================================================

        self.spaceship.display()

        # Carries out necessary actions if game over
        if self.asteroids == []:
            self.asteroid_destroyed = True

        if self.spaceship_hit:
            if self.fadeout <= 0:
                fill(1)
                textSize(30)
                text("YOU HIT AN ASTEROID",
                     self.SPACE['w']/2 - 165, self.SPACE['h']/2)
            else:
                self.fadeout -= 1

        if self.asteroid_destroyed:
            fill(1)
            textSize(30)
            text("YOU DESTROYED THE ASTEROIDS!!!",
                 self.SPACE['w']/2 - 250, self.SPACE['h']/2)

    def fire_laser(self, x, y, rot):
        """Add a laser beam to the game"""
        x_vel = sin(radians(rot))
        y_vel = -cos(radians(rot))
        self.laser_beams.append(
            LaserBeam(self.SPACE, x, y, x_vel, y_vel)
        )

    def handle_keypress(self, key, keycode=None):
        if (key == ' '):
            if self.spaceship.intact:
                self.spaceship.control(' ', self)
        if (keycode):
            if self.spaceship.intact:
                self.spaceship.control(keycode)

    def handle_keyup(self):
        if self.spaceship.intact:
            self.spaceship.control('keyup')

    def do_intersections(self):
        # ======================================================
        # TODO: Problem 4, Part 1: Intersections
        # Here's where you'll probably want to check for intersections
        # between asteroids and laser beams. Laser beams should be removed
        # from the scene if they hit an asteroid, and the asteroid should
        # blow up (the blow_up_asteroid method also must be written. It's
        # been started for you below).
        #
        # The intersection logic below between the spaceship
        # and asteroids should give a hint as to how this will work.
        # Begin code changes for Problem 4, Part 1: Intersections

        l = 0
        while l < len(self.laser_beams):
            a = 0
            while a < len(self.asteroids):
                if (
                    abs(self.laser_beams[l].x - self.asteroids[a].x)
                    < max(self.asteroids[a].radius, self.laser_beams[l].radius)
                    and
                    abs(self.laser_beams[l].y - self.asteroids[a].y)
                    < max(self.asteroids[a].radius,
                          self.laser_beams[l].radius)
                          ):
                    self.blow_up_asteroid(a, l)
                    l -= 1
                    break
                a += 1
            l += 1


        # End of code changes for Problem 4, Part 1: Intersections
        # ======================================================

        # If the space ship still hasn't been blown up
        if self.spaceship.intact:
            # Check each asteroid for intersection
            for i in range(len(self.asteroids)):
                if (
                    abs(self.spaceship.x - self.asteroids[i].x)
                    < max(self.asteroids[i].radius, self.spaceship.radius)
                    and
                    abs(self.spaceship.y - self.asteroids[i].y)
                        < max(self.asteroids[i].radius, self.spaceship.radius)):
                    # We've intersected an asteroid
                    self.spaceship.blow_up(self.fadeout)
                    self.spaceship_hit = True

    def blow_up_asteroid(self, i, j):
        # ======================================================
        # TODO: Problem 4, Part 2: Asteroid blow-up

        # Here you'll write the code to blow up an asteroid.
        # The parameters represent the indexes for the list of
        # asteroids and the list of laser beams, indicating
        # which asteroid is hit by which laser beam.

        # You'll need to:
        # A) Remove the hit asteroid from the scene
        # B) Add appropriate smaller asteroids to the scene
        # C) Make sure that the smaller asteroids are positioned
        #    correctly and flying off in the correct directions

        # Specifically. If the large asteroid is hit, it should
        # break into two medium asteroids, which should fly off
        # perpendicularly to the direction of the laser beam.

        # If a medium asteroid is hit, it should break into three
        # small asteroids, two of which should fly off perpendicularly
        # to the direction of the laser beam, and the third
        # should fly off in the same direction that the laser
        # beam had been traveling.

        # If a small asteroid is hit, it disappears.

        # Begin code changes for Problem 4, Part 2: Asteroid blow-up

        new_x = self.asteroids[i].x
        new_y = self.asteroids[i].y
        slow_factor = 5

        if self.asteroids[i].asize == 'Large':
            chunks = 2
            new_size = 'Med'
        elif self.asteroids[i].asize == 'Med':
            chunks = 3
            new_size = 'Small'
        else:
            chunks = 0

        # del self.asteroids[i]

        # In order to find the perpendicularly velocity,
        # take the cross product of vector

        cross = [
            (self.laser_beams[j].y_vel, -self.laser_beams[j].x_vel),
            (-self.laser_beams[j].y_vel, self.laser_beams[j].x_vel),
            (self.laser_beams[j].y_vel, self.laser_beams[j].x_vel)
            ]

        for k in range(chunks):
            new_asteroid = [
                Asteroid(self.SPACE, new_size,
                         x=new_x + cross[k][0]*self.blow_up_move,
                         y=new_y + cross[k][1]*self.blow_up_move,
                         x_vel=cross[k][0]/slow_factor,
                         y_vel=cross[k][1]/slow_factor)
                         ]
            self.asteroids += new_asteroid

        del self.asteroids[i]
        del self.laser_beams[j]
