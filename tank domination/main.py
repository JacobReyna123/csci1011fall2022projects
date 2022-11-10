import pygame

pygame.init()

#Game settings
monitor_display = (800, 600)

game_display = pygame.display.set_mode(monitor_display)

pygame.display.set_caption("Tank Domination")

system_clock = pygame.time.Clock()

game_running_flag = True

#Game logic
while game_running_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running_flag = False

    if not game_running_flag:
        pygame.quit()



        break
    #Movement
    key_pressed = pygame.key.get_pressed()


    position_delta = 0

    if key_pressed[pygame.K_LEFT]:
        position_delta = -1
    elif key_pressed [pygame.K_RIGHT]:
        position_delta = 1   




    game_display.fill(game_characteristics["sky"]["color"])

    #Create Grass.


    #Create PLayer and computer.
    game_tank_sprite_player = game_tank_sprite_player

    game_display.blit
    #running the game
    pygame.display.update()

    system_clock.tick(30)    


