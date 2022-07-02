import pygame
#       //  pygame tutorial 1  //


pygame.init()

win = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
 
pygame.display.set_caption("Bolas")

class bola():
    def __init__(self, x, h, r, vel1, cor, hb):
        self.x = int(x)
        self.h = int(h)
        self.r = int(r)
        self.vel1 = int(vel1)
        self.cor = cor
        self.hb = int(hb)
        



    def draw(self, x, h, r, cor):
        pygame.draw.circle(win, cor, (x, h), r)


x1 = 50
x2 = 200
h = 100
widht = 40
height = 60             # 3 = 1m/s
inp  =  int(input("qual a velocidade? "))  
vel1 = inp
vel2 = 1

ine = False
ela = False

r = 20
cor = (0, 0, 0)
hb1 = x1 + r
hb2 = x2 - r

col = False


#  classes 




#-------------------------------------------------------------------------------------
run = True

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
   

    keys = pygame.key.get_pressed()



    if keys[pygame.K_q]:
        ine = True

    if keys[pygame.K_e]:
        ela = True
        print("aqui")
        

    win.fill((0, 0, 0))

    hb1 = x1 + r
    hb2 = x2 - r


    #Elastico -----------------------
    if ela == True:
        if hb1 > hb2:
            col = True
        else:
            pass
        
        if col == True:
            vel1 == 0
            vel2 = inp
            print(vel2)
            x2 += vel2
        else:
            x1 += vel1
        
        
    #---------------------------------
   
    #inelastico -----------------------
    if ine == True:
        if hb1 > hb2:
            
            vel1 == vel1
            x1 += vel1/2
            x2 = x1 + (2*r - 1) 
            print(vel1)

        else:
            
            x1 += vel1 
    #---------------------------------


    luke = bola(x1 ,h ,20 , vel1, (255, 0, 0), hb1)
    boulos = bola(x2, h ,20 ,vel2, (0, 0, 255), hb2)     
    #print(hb1) 
    #print(hb2)

  
    luke.draw(x1, h, 20, (255, 0, 0))
    boulos.draw(x2, h, 20, (0, 0, 255))
     
    pygame.display.update()
    #---------------------------------------------------------------------------------------------
else:
    
        pygame.display.update()


#pygame.quit() 