import pygame
import random
#Initial Settings
pygame.init()
screen=pygame.display.set_mode((750,600))
game_on=True

#Adding the hero
monster=pygame.image.load("ghost_30x30.jpg")
monster_coordinate=monster.get_rect()
monster_coordinate.topleft=(375,300)

#Adding Money
money=pygame.image.load("money.jpg")
money_coordinate=money.get_rect()
inital_x=random.randint(30,750)
inital_y=random.randint(120,600)
money_coordinate.bottomright=(inital_x,inital_y)

#Score Board Font
font=pygame.font.SysFont("calibri",64,True)

#Adding Songs
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1,0.0)
eating_sound=pygame.mixer.Sound("eating-sound-effect-36186.mp3")#Pay attention to Sound method
game_over_sound=pygame.mixer.Sound("game_over.mp3")

#FPS and Speed Settings
speed=5
FPS=30
inital_time=pygame.time.Clock()

#Game
score = 0
def game_over():
    global score
    game_over_sound.play()
    score = 0
    monster_coordinate.topleft = (375, 300)
    pygame.time.wait(150)
while game_on:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game_on = False
    pressing = pygame.key.get_pressed()
    if pressing[pygame.K_UP] and monster_coordinate.y > 90:
        monster_coordinate.y -= speed
    elif pressing[pygame.K_UP] and monster_coordinate.y <= 90:
        game_over()
    elif pressing[pygame.K_DOWN] and monster_coordinate.y < 570:
        monster_coordinate.y += speed
    elif pressing[pygame.K_DOWN] and monster_coordinate.y>=570:
        game_over()
    elif pressing[pygame.K_LEFT] and monster_coordinate.x > 0:
        monster_coordinate.x -= speed
    elif pressing[pygame.K_LEFT] and monster_coordinate.x<=0:
        game_over()
    elif pressing[pygame.K_RIGHT] and monster_coordinate.x < 720:
        monster_coordinate.x += speed
    elif pressing[pygame.K_RIGHT] and monster_coordinate.x>=720:
        game_over()
    if monster_coordinate.colliderect(money_coordinate):
        eating_sound.play()  # It must not be infinite loop
        new_x = random.randint(30, 750)
        new_y = random.randint(120, 600)
        money_coordinate.bottomright = (new_x, new_y)
        score += 1

    screen.fill((0, 0, 0))
    screen.blit(money, money_coordinate)
    screen.blit(monster, monster_coordinate)
    score_board = font.render("Score: " + str(score), True, (255, 0, 0))
    score_board_coordinate = score_board.get_rect()
    score_board_coordinate.topleft = (20, 20)
    screen.blit(score_board, score_board_coordinate)
    # Line that separates game and score board
    pygame.draw.line(screen, (255, 0, 0), (0, 90), (750, 90))
    pygame.display.update()
    inital_time.tick(FPS)
pygame.quit()
