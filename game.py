import pygame
pygame.init()

win = pygame.display.set_mode((720,600))
pygame.display.set_caption("Game of Squares")

bluex = 200
bluey = 200
redx = 400
redy = 400
bluevel = 8
redvel = 7
bluesize = 20
redsize = 40
run = True

def drawGame():
    win.fill((0,0,0))
    pygame.draw.rect(win,(0,0,255),(bluex,bluey,bluesize,bluesize))
    pygame.draw.rect(win,(255,0,0),(redx,redy,redsize,redsize))
    pygame.display.update()

while run:
    pygame.time.delay(100)
    
    if redx < bluex - 10:
        redx = redx + redvel
        drawGame()
    
    elif redx > bluex + 10:
        drawGame()
        redx = redx - redvel
        
    elif redy < bluey - 10:
        redy = redy + redvel
    
    elif redy > bluey + 10:
        redy = redy - redvel
    
    else:
        run = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        bluex -= bluevel
    
    if keys[pygame.K_RIGHT]:
        bluex += bluevel
        
    if keys[pygame.K_DOWN]:
        bluey += bluevel
        
    if keys[pygame.K_UP]:
        bluey -= bluevel
        
    if bluex > 720:
        run = False 
        
    elif bluex < 0:
        run = False
        
    elif bluey > 600:
        run = False
        
    elif bluey < 0:
        run = False
    
    drawGame()
    
    redsize = redsize + 0.25
    
pygame.quit()
