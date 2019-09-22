import pygame
import random
pygame.init()

height = 500
width = 1000
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0
black = 0,0,0
blue = 0,0,255





def homeScreen():
    bg_img=pygame.image.load("brickimg3.jpg")
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.blit(bg_img,(0,0))
        pygame.display.flip()

def score(c):
    font = pygame.font.SysFont(None,30)
    text = font.render("Score : {}".format(c), True, red)
    screen.blit(text, (5,5))

def life(lifeRemaining):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Life Remaining : {}".format(lifeRemaining), True, red)
    screen.blit(text, (800, 10))
    
def gameOver():
    font_1 = pygame.font.SysFont(None,80)
    text_1 = font_1.render("Game Over",True,red)
    font_2 = pygame.font.SysFont(None,60)
    text_2 = font_2.render("Press Any Key to Start Again",True,white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                homeScreen()

        screen.blit(text_1,(200,100))
        screen.blit(text_2,(100,250))

        pygame.display.update()

def level():
     font_1 = pygame.font.SysFont(None,80)
     text_1=font_1.render("Level Completed",True,red)
     while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                homeScreen()

        screen.blit(text_1,(300,200))

        pygame.display.update()



def game():
    barHeight = 20
    barWidth = 160
    barx = width//2 - barWidth//2
    bary = height - barHeight - 10
    moveX = 0

    ballRadius = 8
    ballY = bary - 10

    brickWidth = 100
    brickheight = 20

   
    moveBall = False
    ballOnBar = True
    ballMoveX = 0
    ballMoveY = 0
    brickList = []
    brickColors = []
    for row in range(1,6):
        for col in range(9):
            brickX = col * (brickWidth+5)
            brickY = row * (brickheight+5)
            color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            brickColors.append(color)
            brickList.append(pygame.Rect(brickX,brickY,brickWidth,brickheight))
  

    count = 0
    FPS = 300
    clock = pygame.time.Clock()
    lifeRemaining=3
    while True:
        if ballOnBar:
            ballX = barx + barWidth // 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 5
                elif event.key == pygame.K_LEFT:
                    moveX = -5
                elif event.key == pygame.K_SPACE:
                    if ballOnBar:
                        moveBall = True
                        ballOnBar = False
            elif event.type == pygame.KEYUP:
                moveX = 0

        # screen.fill(white)
        screen.fill(black)

        barRect = pygame.draw.rect(screen,red,[barx,bary,barWidth,barHeight])
        pygame.draw.circle(screen,white,(ballX,ballY),ballRadius)
        ballRect = pygame.Rect(ballX,ballY,ballRadius,ballRadius)

        for i in range(len(brickList)):
            pygame.draw.rect(screen,brickColors[i],brickList[i])

        barx += moveX
        ballX += ballMoveX
        ballY += ballMoveY

        for i in range(len(brickList)):
            if brickList[i].colliderect(ballRect):
                del brickList[i]
                ballMoveY = 3
                count += 1
                FPS += 5
                break

        

        if moveBall:
            ballMoveX = -3
            ballMoveY = -3
            moveBall = False

        if barx > width - 50:
            moveX = -3
        elif barx < 0:
            moveX = 3

        if ballX > width - ballRadius:
            ballMoveX = -3
        elif ballX < ballRadius:
            ballMoveX = 3
        elif ballY < ballRadius:
            ballMoveY = 3
        elif barRect.colliderect(ballRect):
            ballMoveY = -3
        elif ballY > height*2:
            # print("Game Over")
            # play()
            ballOnBar = True
            ballMoveY = 0
            ballMoveX = 0
            ballY = bary - 10
            lifeRemaining -= 1
            count+=0

        if lifeRemaining == 0:
            gameOver()
        if count==10:
            level()

        life(lifeRemaining)
        score(count)


        pygame.display.flip()
        clock.tick(FPS)
#game()
homeScreen()
