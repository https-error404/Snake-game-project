import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()













































# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Set the dimensions of the game window
# window_width = 600
# window_height = 400
# window = pygame.display.set_mode((window_width, window_height))

# # Set the title of the game window
# pygame.display.set_caption("Snake Game")

# # Set the colors
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)

# # Set the font
# font = pygame.font.SysFont(None, 25)

# # Set the block size and speed of the snake
# block_size = 10
# snake_speed = 5

# # Define the function to display the message on the screen
# def message_to_screen(msg, color):
#     screen_text = font.render(msg, True, color)
#     window.blit(screen_text, [window_width/6, window_height/3])

# # Define the game loop
# def gameLoop():
#     game_exit = False
#     game_over = False

#     # Set the starting position of the snake
#     lead_x = window_width/2
#     lead_y = window_height/2

#     # Set the initial movement direction of the snake
#     lead_x_change = 0
#     lead_y_change = 0

#     # Set the initial position of the food
#     food_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
#     food_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0

#     # Set the snake list and length
#     snake_list = []
#     snake_length = 1

#     # Set the initial score
#     score = 0

#     def show_score(score):
#         score_text = font.render("Score: " + str(score), True, black)
#         window.blit(score_text, [0, 0])


#     # Start the game loop
#     while not game_exit:

#         while game_over == True:
#             window.fill(white)
#             message_to_screen(f"Game over, score: {score}, press Q to quit or C to play again", red)
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_exit = True
#                         game_over = False
#                     if event.key == pygame.K_c:
#                         gameLoop()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_exit = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     lead_x_change = -block_size
#                     lead_y_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     lead_x_change = block_size
#                     lead_y_change = 0
#                 elif event.key == pygame.K_UP:
#                     lead_y_change = -block_size
#                     lead_x_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     lead_y_change = block_size
#                     lead_x_change = 0

#         # Check if the snake goes out of bounds
#         if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
#             game_over = True

#         # Update the position of the snake
#         lead_x += lead_x_change
#         lead_y += lead_y_change

#         # Fill the background color
#         window.fill(white)

#         # Draw the snake and the food
#         pygame.draw.rect(window, black, [lead_x, lead_y, block_size, block_size])
#         pygame.draw.rect(window, red, [food_x, food_y, block_size, block_size])

#         # Add the head of the snake to the snake list
#         snake_head = []
#         snake_head.append(lead_x)
#         snake_head.append(lead_y)
#         snake_list.append(snake_head)

#         # Check if the snake has collided with itself
#         if len(snake_list) > snake_length:
#             del snake_list[0]

#         for each_segment in snake_list[:-1]:
#             if each_segment == snake_head:
#                 game_over = True

#         # Update the snake length and the position of the food
#         pygame.display.update()

#         if lead_x == food_x and lead_y == food_y:
#             food_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
#             food_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
#             snake_length += 1

#         # Draw the snake on the game window
#         for segment in snake_list:
#             pygame.draw.rect(window, black, [segment[0], segment[1], block_size, block_size])

#         # Set the snake speed
#         pygame.display.update()
#         clock = pygame.time.Clock()
#         clock.tick(snake_speed)

#     # Deactivate Pygame library and quit
#     pygame.quit()
#     quit()

# # Call the game loop function
# gameLoop()


























































# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Set the dimensions of the game window
# window_width = 600
# window_height = 400
# window = pygame.display.set_mode((window_width, window_height))
# background = pygame.image.load("background.jpg")


# # Set the title of the game window
# pygame.display.set_caption("Snake Game")

# # Set the colors
# white = (255, 255, 255)
# green = (0, 255, 0)
# red = (255, 0, 0)


# # Set the font
# font = pygame.font.SysFont(None, 25)

# # Set the block size and speed of the snake
# block_size = 10
# snake_speed = 15

# # Define the function to display the message on the screen
# def message_to_screen(msg, color):
#     screen_text = font.render(msg, True, color)
#     window.blit(screen_text, [window_width/6, window_height/3])

# # Define the game loop
# def gameLoop():
#     game_exit = False
#     game_over = False

#     # Set the starting position of the snake
#     lead_x = window_width/2
#     lead_y = window_height/2

#     # Set the initial movement direction of the snake
#     lead_x_change = 0
#     lead_y_change = 0

#     # Set the initial position of the food
#     food_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
#     food_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0

#     # Set the snake list and length
#     snake_list = []
#     snake_length = 1

#     # Start the game loop
#     while not game_exit:

#         while game_over == True:
#             window.blit(background, [0, 0])
#             window.fill(white)
#             message_to_screen("Game over, press Q to quit or C to play again", red)
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_exit = True
#                         game_over = False
#                     if event.key == pygame.K_c:
#                         gameLoop()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_exit = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     lead_x_change = -block_size
#                     lead_y_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     lead_x_change = block_size
#                     lead_y_change = 0
#                 elif event.key == pygame.K_UP:
#                     lead_y_change = -block_size
#                     lead_x_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     lead_y_change = block_size
#                     lead_x_change = 0

#         # Check if the snake goes out of bounds
#         if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
#             game_over = True

#         # Update the position of the snake
#         lead_x += lead_x_change
#         lead_y += lead_y_change

#         # Fill the background color
#         window.fill(white)

#         # Draw the snake and the food
#         pygame.draw.rect(window, green, [lead_x, lead_y, block_size, block_size])
#         pygame.draw.rect(window, red, [food_x, food_y, block_size, block_size])

#         # Add the head of the snake to the snake list
#         snake_head = []
#         snake_head.append(lead_x)
#         snake_head.append(lead_y)
#         snake_list.append(snake_head)

#         # Check if the snake has collided with itself
#         if len(snake_list) > snake_length:
#             del snake_list[0]

#         for each_segment in snake_list[:-1]:
#             if each_segment == snake_head:
#                 game_over = True

#         # Update the snake length and the position of the food
#         pygame.display.update()

#         if lead_x == food_x and lead_y == food_y:
#             food_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
#             food_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
#             snake_length += 1

#         # Draw the snake on the game window
#         for segment in snake_list:
#             pygame.draw.rect(window, green, [segment[0], segment[1], block_size, block_size])

#         # Set the snake speed
#         pygame.display.update()
#         clock = pygame.time.Clock()
#         clock.tick(snake_speed)

#     # Deactivate Pygame library and quit
#     pygame.quit()
#     quit()

# # Call the game loop function
# gameLoop() 