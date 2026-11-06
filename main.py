import pygame # import pygame module
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
import player
import asteroid
import asteroidfield
import sys
from shot import Shot

def main():
    # initialize pygame
    pygame.init()

    #------------------------------INITIALIZATION---------------------------
    # Get/create instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create clock object to track time and a dt variable to enforce 60fps
    clock = pygame.time.Clock()
    dt = 0.0

    #------------------------------GROUPS-------------------------------
    #The purpose of using groups is that we can call a single method on an
    #entire group; using the method on the item within the group.

    # create two group objects: updatable group, and a drawable group
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots     = pygame.sprite.Group()


    #Add the Player *class* to both groups
    player.Player.containers = (updatable, drawable)

    #Add the Asteroid *class* to the asteroids, updatable, and drawable groups
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)

    #Automatically add Shot instances to the shots group
    Shot.containers = (shots, drawable, updatable)


    #------------------------------PLAYER-----------------------------------
    # Create instance of Player at center of screen
    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    #------------------------------ASTEROID---------------------------------
    # Create instance(s) of Asteroidfield
    field = asteroidfield.AsteroidField()

    #confirm instance of player correctly in groups
    for item in updatable:
        if isinstance(item, player.Player):
            print("Player instance correctly created in updatable")
        else: 
            print("No player instance found")

    for item in drawable:
        if isinstance(item, player.Player):
            print("Player instance correctly drawable")
        else: 
            print("No player instance found")
    

    # game loop.
    while True: 
        log_state()
        screen.fill("black")


        # Process the game event queue
        for event in pygame.event.get():
            #if event is QUIT, close program (return from main function)
            if event.type == pygame.QUIT:
                return

        # refresh game components
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)

        #iterate over asteroids and check for collisions
        for item in asteroids:
            if item.collides_with(player1):
                log_event("player_hit")
                print(f"Game over!")
                sys.exit()
            for shot in shots:
                if item.collides_with(shot):
                    log_event("asteroid_shot")
                    item.split()
                    shot.kill()
            


        #refresh the window (Keep this at the end of the loop)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print(f"DeltaTime: {dt}")


if __name__ == "__main__":
    main()
