import pygame


def main():
    pygame.init()
    pygame.display.set_caption("My pong")

    WIDTH = 800
    HEIGHT = 400

    # surface
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # add a solid background as r,g,b:
    screen.fill((0, 0, 0))
    # double buffering: stage updates together; update them at once.
    # avoids flickering.
    pygame.display.update()

    # Walls
    # Rect(surface, color, rect) -> Rect
    wcolor = pygame.Color("white")
    BORDER = 15

    # top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, BORDER)))
    pygame.display.update()

    # left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    pygame.display.update()

    # bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, HEIGHT - BORDER), (WIDTH, BORDER)))
    pygame.display.update()

    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


if __name__ == "__main__":
    # call the main function
    main()
