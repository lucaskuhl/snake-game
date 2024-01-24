import pygame
import random

pygame.init()

game_over = False
clock = pygame.time.Clock()

#colors
snake_white = (255,255,255)
fruit_red = (255,0,0)
display_black = (0,0,0)

#Display
width = 860
height = 1080
display = pygame.display.set_mode((height,width))
pygame.display.set_caption('Snake Game - Lucas')

#snake
snake_block = 10
snake_length = []
snake_list = 1

def snake (snake_block, snake_length):
    for x in snake_length:
        pygame.draw.rect(display, snake_white, [x[0], x[1], snake_block, snake_block])

#coords
x1 = height/2
y1 = width/2
x_change = 0
y_change = 0
x_food = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
y_food = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        
#game_loop
def game_loop ():
    game_over = False
    game_loop = False
    
    x1 = height/2
    y1 = width/2
    x_change = 0
    y_change = 0
    x_food = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    y_food = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    
#Message
# def message (message):
#     msg = font_style.render(message, True, snake_white)
#     display.blit(msg, [width/3,height/3])
blocked_key = 0    
while not game_over:
    ''
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            game_over=True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and blocked_key != pygame.K_LEFT:
                blocked_key = pygame.K_RIGHT
                x_change = -snake_block
                y_change = 0
            if event.key == pygame.K_RIGHT and blocked_key != pygame.K_RIGHT:
                blocked_key = pygame.K_LEFT
                x_change = snake_block
                y_change = 0    
            if event.key == pygame.K_DOWN and blocked_key != pygame.K_DOWN:
                blocked_key = pygame.K_UP
                x_change = 0
                y_change = snake_block
            if event.key == pygame.K_UP and blocked_key != pygame.K_UP:
                blocked_key = pygame.K_DOWN
                x_change = 0
                y_change = -snake_block
                
    if x1 >= height or x1 < 0:
        game_over = True        
    elif y1 >= width or y1 < 0:
        game_over = True   
                
    x1 += x_change
    y1 += y_change
    
    display.fill(display_black)
    
    pygame.draw.rect(display, fruit_red, [x_food, y_food, snake_block, snake_block])
    
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_length.append(snake_head)
    
    if len(snake_length) > snake_list:
            del snake_length[0]
 
    for x in snake_length[:-1]:
        if x == snake_head:
            game_over = True
    
    snake(snake_block, snake_length)
    
    pygame.display.update()
    
    if x1 == x_food and y1 == y_food:
        
        x_food = round(random.randrange(0, round(width/2 - snake_block)) / 10.0) * 10.0
        y_food = round(random.randrange(0, round(height/2 - snake_block)) / 10.0) * 10.0 
        snake_list += 1
        pygame.display.update()
    
    clock.tick(20)

pygame.quit()
quit()
