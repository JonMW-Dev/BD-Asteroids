import pygame # import pygame module
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    # initialize pygame
    pygame.init()

    # Get/create instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True: 
        log_state()

        # Process the game event queue
        for event in pygame.event.get():
            #if event is QUIT, close program (return from main function)
            if event.type == pygame.QUIT:
                return
            

        screen.fill("black")


        #refresh the window (Keep this at the end of the loop)
        pygame.display.flip()


if __name__ == "__main__":
    main()
