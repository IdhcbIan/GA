import pygame
#       //  pygame tutorial 1  //


pygame.init()

win = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

pygame.display.set_caption("Bolas")

x1 = 50
x2 = 200
y = 100
widht = 40
height = 60
vel = 5
move = False

run = True

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()


    if keys[pygame.K_SPACE]:
        move = True

    if move == True:    
        x1 += vel

        if x1 + 35 == x2 and x2 + 20 != 500:
            if x1 + 35 == x2:
                x2 += vel
            else: 
                vel = -10

        win.fill((0, 0, 0))
        pygame.draw.circle(win, (255, 0, 0), (x1, y), 20)
        pygame.draw.circle(win, (0, 0, 255), (x2, y), 20)
        pygame.display.update()
    
    else:
    
        pygame.display.update()


pygame.quit() 