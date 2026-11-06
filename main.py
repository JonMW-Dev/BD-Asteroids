import pygame # import pygame module
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import player


def main():
    # initialize pygame
    pygame.init()

    # Get/create instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create clock object to track time and a dt variable to enforce 60fps
    clock = pygame.time.Clock()
    dt = 0.0

    # game loop.
    while True: 
        log_state()

        # Process the game event queue
        for event in pygame.event.get():
            #if event is QUIT, close program (return from main function)
            if event.type == pygame.QUIT:
                return
            

        screen.fill("black")

        player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
        player1.draw(screen)


        #refresh the window (Keep this at the end of the loop)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print(f"DeltaTime: {dt}")


if __name__ == "__main__":
    main()
