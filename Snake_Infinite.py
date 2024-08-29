import pygame
import random

pygame.init()

SCREENHEIGHT = 720
SCREENWIDTH = 720
BLOCKSIZE = 24

font = pygame.font.Font('font.ttf', 32)


SCREEN = pygame.display.set_mode((SCREENHEIGHT+1,SCREENWIDTH+1))
pygame.display.set_caption("Im a Snaaak...")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x , self.y = int(SCREENHEIGHT//2) , int(SCREENWIDTH//2) 
        self.xdir , self.ydir = 0,0
        self.head = pygame.Rect(self.x,self.y,BLOCKSIZE,BLOCKSIZE)
        self.body = [pygame.Rect(self.x-BLOCKSIZE,self.y,BLOCKSIZE,BLOCKSIZE)]
        self.dead = False

    def move(self):
        for sq in self.body:
            if self.head.x == sq.x and self.head.y == sq.y:
                self.dead = True

        if self.dead:
            self.x , self.y = int(SCREENHEIGHT/2) , int(SCREENWIDTH/2) 
            self.xdir , self.ydir = 1,0
            self.head = pygame.Rect(self.x,self.y,BLOCKSIZE,BLOCKSIZE)
            self.body = [pygame.Rect(self.x-BLOCKSIZE,self.y,BLOCKSIZE,BLOCKSIZE)]
            self.dead = False

        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCKSIZE
        self.head.y += self.ydir * BLOCKSIZE
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.x=int(random.randint(0,SCREENHEIGHT-20)/BLOCKSIZE)*BLOCKSIZE
        self.y=int(random.randint(0,SCREENWIDTH-20)/BLOCKSIZE)*BLOCKSIZE
        self.rect= pygame.Rect(self.x,self.y,BLOCKSIZE,BLOCKSIZE)

    def appleUpdate(self):
        pygame.draw.rect(SCREEN,"red",self.rect)

    
class Speed:
    def __init__(self):
        Speed = 10


snake = Snake()
apple = Apple()


running = True
while running:
    for event in pygame.event.get():
        # quite button
        if event.type == pygame.QUIT:
            running = False
        # controls
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                snake.xdir = 0
                snake.ydir = -1
            elif event.key == pygame.K_DOWN :
                snake.xdir = 0
                snake.ydir = 1
            elif event.key == pygame.K_LEFT :
                snake.xdir = -1
                snake.ydir = 0
            elif event.key == pygame.K_RIGHT :
                snake.xdir = 1
                snake.ydir = 0

    

    SCREEN.fill("black")



    # sanke & apple updater
    snake.move()
    apple.appleUpdate()
  
    pygame.draw.rect(SCREEN,"blue",snake.head)

    for square in snake.body:
        pygame.draw.rect(SCREEN,"green",square)

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y,BLOCKSIZE,BLOCKSIZE))
        apple=Apple()

    # wall portal
    if snake.head.x == SCREENHEIGHT :
        snake.head.x = 0
    if snake.head.x < 0 :
        snake.head.x = SCREENHEIGHT
    if snake.head.y == SCREENWIDTH :
        snake.head.y = 0
    if snake.head.y < 0 :
        snake.head.y = SCREENWIDTH

    # score board
    text = font.render(f'{len(snake.body)-1}', True, 'white')
    textRect = text.get_rect()
    textRect.center = (SCREENHEIGHT // 2, 50)
    SCREEN.blit(text,textRect)
  
    pygame.display.flip()
    clock.tick(10)

pygame.quit()