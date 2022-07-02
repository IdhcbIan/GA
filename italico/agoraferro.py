from cmath import pi
import pygame
import math

pygame.init()

win = pygame.display.set_mode((1000, 500))
keys = pygame.key.get_pressed()
pygame.display.set_caption("Italico")


x1 = 200
y1 = 25
x2 = 400
y2 = 25
x3 = 200
y3 = 400
x4 = 400
y4 = 400

go = False  
start = False

teta = math.pi/2

run = True
BLUE = (0, 0, 255)

def draw(x1, y1, x2, y2):
    pygame.draw.line(win, BLUE, [x1, y1], [x2,y2], 5)


def square(x1, x2, x3, x4, y1, y2, y3, y4):
    draw(x1, y1, x2, y2)
    draw(x1, y1, x3, y3)
    draw(x3, y3, x4, y4)
    draw(x2, y2, x4, y4)



while run:
    pygame.time.delay(20)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_q]:
        go = True

    if keys[pygame.K_w]:
        teta = math.pi/2
        start = True
        x1 = 200
        x2 = 400
    
    win.fill((0, 0, 0))


    if go == True:
        
        square(x1, x2, x3, x4, y1, y2, y3, y4)

    if teta < math.pi*0.45:
        start = False
        print("chegou")
    
    if start == True:
        teta -= 0.001
        x1 += y1/math.tan(teta)
        x2 += y2/math.tan(teta)
    print(teta/math.pi)


    pygame.display.update()


pygame.quit() 






























