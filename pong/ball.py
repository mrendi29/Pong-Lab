import pygame


class Ball:
    radius = 10

    def __init__(self, x, y, vx, vy, screen, color, bgcolor,constants):
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.color = color
        self.bgcolor = bgcolor
        self.constants = constants

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.radius)

    def update(self):
        # delete the old ball
        self.show(self.bgcolor)

        px = self.x + self.vx
        py = self.y + self.vy
        # TODO: Check if colliding.
        ## Flip velocity/direction
        if px < (self.constants.BORDER + self.radius):
            self.vx = -self.vx
        if py <(self.constants.BORDER + self.radius):
            self.vy = -self.vy
        if py > (self.constants.HEIGHT - self.radius - self.constants.BORDER):
            self.vy = -self.vy
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.color)