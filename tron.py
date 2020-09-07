import pygame, sys, time, random

# Difficulty settings
# Easy      ->  10
# Medium    ->  15
# Hard      ->  30
if sys.argv[1]:
    if sys.argv[1] == "easy":
        difficulty = 10
    elif sys.argv[1] == "normal":
        difficulty = 15
    elif sys.argv[1] == "hard":
        difficulty = 30
    else:
        difficulty = int(sys.argv[1])
else:
    difficulty = 15

# Window size
frame_size_x = 720
frame_size_y = 480

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Initialise game window
pygame.display.set_caption('Two Snake')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Game variables
snake1_pos = [50, 50]
snake1_body = [[50, 50], [50, 50-10], [50, 50-(2*10)]]

snake2_pos = [670, 50]
snake2_body = [[670, 50], [670, 50-10], [670, 50-(2*10)]]

direction1 = 'DOWN'
change1_to = direction1

direction2 = 'DOWN'
change = direction2

left = snake2_pos[0]
left11 = snake2_pos[0]
left12 = snake2_pos[0]
left13 = snake2_pos[0]

right = frame_size_x - snake2_pos[0]
right11 = frame_size_x - snake2_pos[0]
right12 = frame_size_x - snake2_pos[0]
right13 = frame_size_x - snake2_pos[0]

up = snake2_pos[1]
up11 = snake2_pos[1]
up12 = snake2_pos[1]
up13 = snake2_pos[1]

down = frame_size_y - snake2_pos[1]
down11 = frame_size_y - snake2_pos[1]
down12 = frame_size_y - snake2_pos[1]
down13 = frame_size_y - snake2_pos[1]

score = 0

def game_over(player):
    if player == 1:
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('Player 1 DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
        game_window.fill(black)
        game_window.blit(game_over_surface, game_over_rect)
        show_score(0, red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
    else:
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('Player 2 DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
        game_window.fill(black)
        game_window.blit(game_over_surface, game_over_rect)
        show_score(0, red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


while True:
    if sys.argv[2] == "demo":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == ord('w'):
                    change1_to = 'UP'
                if event.key == ord('s'):
                    change1_to = 'DOWN'
                if event.key == ord('a'):
                    change1_to = 'LEFT'
                if event.key == ord('d'):
                    change1_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change1_to == 'UP' and direction1 != 'DOWN':
            direction1 = 'UP'
        if change1_to == 'DOWN' and direction1 != 'UP':
            direction1 = 'DOWN'
        if change1_to == 'LEFT' and direction1 != 'RIGHT':
            direction1 = 'LEFT'
        if change1_to == 'RIGHT' and direction1 != 'LEFT':
            direction1 = 'RIGHT'

        check1 = random.randrange(50, 80, 10)

        if direction2 == 'LEFT' or direction2 == 'RIGHT':
            if direction2 == 'LEFT':
                print("debug1.1")
                if (snake2_pos[0] - check1) <= 0:
                    print("debug11")
                    up1 = snake2_pos[1]
                    down1 = frame_size_y - snake2_pos[1]
                    if up1 > up:
                        up = up1
                    if down1 > down1:
                        down = down1
                for block2 in snake2_body[1:]:
                    if snake2_pos[0] > block2[0] and snake2_pos[1] == block2[1]:
                        if (snake2_pos[0] - check1) <= block2[0]:
                            print("debug12")
                            left12 = snake2_pos[0] - block2[0]
                            up2 = snake2_pos[1] - block2[1]
                            down2 = block2[1] - snake2_pos[1]
                            if up2 > up:
                                up = up2
                            if down2 > down:
                                down = down2
                for block1 in snake1_body[1:]:
                    if snake2_pos[0] > block1[0] and snake2_pos[1] == block1[1]:
                        if (snake2_pos[0] - check1) <= block1[0]:
                            print("debug13")
                            left13 = snake2_pos[0] - block1[0]
                            up3 = snake2_pos[1] - block1[1]
                            down3 = block1[1] - snake2_pos[1]
                            if up3 > up:
                                up = up3
                            if down3 > down:
                                down = down3

                left11 = snake2_pos[0]
                left14 = min(left11, left12, left13)
                if left14 != 0:
                    if left14 < left:
                        left = left14
                print("left: ", left)

            elif direction2 == 'RIGHT':
                print("debug1.2")

                if (snake2_pos[0] + check1) >= frame_size_x:
                    print("debug14")
                    up4 = snake2_pos[1]
                    down4 = frame_size_y - snake2_pos[1]
                    if up4 > up:
                        up = up4
                    if down4 > down:
                        down = down4
                for block2 in snake2_body[1:]:
                    if snake2_pos[0] < block2[0] and snake2_pos[1] == block2[1]:
                        if (snake2_pos[0] + check1) >= block2[0]:
                            print("debug15")
                            right12 = block2[0] - snake2_pos[0]
                            up5 = snake2_pos[1] - block2[1]
                            down5 = block2[1] - snake2_pos[1]
                            if up5 > up:
                                up = up5
                            if down5 > down:
                                down = down5
                for block1 in snake1_body[1:]:
                    if snake2_pos[0] < block1[0] and snake2_pos[1] == block1[1]:
                        if (snake2_pos[0] + check1) >= block1[0]:
                            print("debug16")
                            right13 = block1[0] - snake2_pos[0]
                            up6 = snake2_pos[1] - block1[1]
                            down6 = block1[1] - snake2_pos[1]
                            if up6 > up:
                                up = up6
                            if down6 > down:
                                down = down6

                right11 = frame_size_x - snake2_pos[0]
                right14 = min(right11, right12, right13)
                if right14 != 0:
                    if right14 < right:
                        right = right14
                print("right: ", right)

        elif direction2 == 'UP' or direction2 == 'DOWN':
            if direction2 == 'UP':
                print("debug2.1")
                if (snake2_pos[1] - check1) <= 0:
                    print("debug21")
                    left1 = snake2_pos[0]
                    right1 = frame_size_x - snake2_pos[0]
                    if left1 > left:
                        left = left1
                    if right1 >= right:
                        right = right1
                for block2 in snake2_body[1:]:
                    if snake2_pos[1] > block2[1] and snake2_pos[0] == block2[0]:
                        if (snake2_pos[1] - check1) <= block2[1]:
                            print("debug22")
                            up12 = snake2_pos[1] - block2[1]
                            left2 = snake2_pos[0] - block2[0]
                            right2 = block2[0] - snake2_pos[0]
                            if left2 > left:
                                left = left2
                            if right2 > right:
                                right = right2
                for block1 in snake1_body[1:]:
                    if snake2_pos[1] > block1[1] and snake2_pos[0] == block1[0]:
                        if (snake2_pos[1] - check1) <= block1[1]:
                            print("debug23")
                            up13 = snake2_pos[1] - block1[1]
                            left3 = snake2_pos[0] - block1[0]
                            right3 = block1[0] - snake2_pos[0]
                            if left >= left3:
                                left = left3
                            if right >= right3:
                                right = right3

                up11 = snake2_pos[1]
                up14 = min(up11, up12, up13)
                if up14 != 0:
                    if up14 < up:
                        up = up14
                print("up: ", up)

            elif direction2 == 'DOWN':
                print("debug2.2")
                if (snake2_pos[1] + check1) >= frame_size_y:
                    print("debug24")
                    left4 = snake2_pos[0]
                    right4 = frame_size_x - snake2_pos[0]
                    if left4 > left:
                        left = left4
                    if right4 > right:
                        right = right4
                for block2 in snake2_body[1:]:
                    if snake2_pos[1] < block2[1] and snake2_pos[0] == block2[0]:
                        if (snake2_pos[1] + check1) >= block2[1]:
                            print("debug25")
                            down12 = block2[1] - snake2_pos[1]
                            left5 = snake2_pos[0] - block2[0]
                            right5 = block2[0] - snake2_pos[0]
                            if left5 > left:
                                left = left5
                            if right5 > right:
                                right = right5
                for block1 in snake1_body[1:]:
                    if snake2_pos[1] < block1[1] and snake2_pos[0] == block1[0]:
                        if (snake2_pos[1] + check1) >= block1[1]:
                            print("debug26")
                            down13 = block1[1] - snake2_pos[1]
                            left6 = snake2_pos[0] - block1[0]
                            right6 = block1[0] - snake2_pos[0]
                            if left6 > left:
                                left = left6
                            if right6 > right:
                                right = right6

                down11 = frame_size_y - snake2_pos[1]
                down15 = min(down11, down12, down13)
                if down != 0:
                    if down15 < down:
                        down = down15
                print("down: ", down)

        print("L, R, U, D", left, right, up, down)

        change = direction2

        change21 = {"UP": up, "DOWN": down, "LEFT": left}
        change22 = {"UP": up, "DOWN": down, "RIGHT": right}
        change23 = {"LEFT": left, "RIGHT": right, "UP": up}
        change24 = {"LEFT": left, "RIGHT": right, "DOWN": down}

        if change == "LEFT":
            direction2 = max(change21, key=change21.get)
        elif change == "RIGHT":
            direction2 = max(change22, key=change22.get)
        elif change == "UP":
            direction2 = max(change23, key=change23.get)
        elif change == "DOWN":
            direction2 = max(change24, key=change24.get)

        print("direction2: ", direction2)

    elif sys.argv[2] == "random":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == ord('w'):
                    change1_to = 'UP'
                if event.key == ord('s'):
                    change1_to = 'DOWN'
                if event.key == ord('a'):
                    change1_to = 'LEFT'
                if event.key == ord('d'):
                    change1_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change1_to == 'UP' and direction1 != 'DOWN':
            direction1 = 'UP'
        if change1_to == 'DOWN' and direction1 != 'UP':
            direction1 = 'DOWN'
        if change1_to == 'LEFT' and direction1 != 'RIGHT':
            direction1 = 'LEFT'
        if change1_to == 'RIGHT' and direction1 != 'LEFT':
            direction1 = 'RIGHT'

        check2 = random.randint(1, 5)

        if check2 == 1:
            direction2 = "UP"
        elif check2 == 2:
            direction2 = "DOWN"
        elif check2 == 3:
            direction2 = "LEFT"
        else:
            direction2 = "RIGHT"

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Whenever a key is pressed down
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == ord('w'):
                    change1_to = 'UP'
                if event.key == pygame.K_UP:
                    change2_to = 'UP'
                if event.key == ord('s'):
                    change1_to = 'DOWN'
                if event.key == pygame.K_DOWN:
                    change2_to = 'DOWN'
                if event.key == ord('a'):
                    change1_to = 'LEFT'
                if event.key == pygame.K_LEFT:
                    change2_to = 'LEFT'
                if event.key == ord('d'):
                    change1_to = 'RIGHT'
                if event.key == pygame.K_RIGHT:
                    change2_to = 'RIGHT'
                # Esc -> Create event to quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))


        # Making sure the snake cannot move in the opposite direction instantaneously
        if change1_to == 'UP' and direction1 != 'DOWN':
            direction1 = 'UP'
        if change1_to == 'DOWN' and direction1 != 'UP':
            direction1 = 'DOWN'
        if change1_to == 'LEFT' and direction1 != 'RIGHT':
            direction1 = 'LEFT'
        if change1_to == 'RIGHT' and direction1 != 'LEFT':
            direction1 = 'RIGHT'

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change2_to == 'UP' and direction2 != 'DOWN':
            direction2 = 'UP'
        if change2_to == 'DOWN' and direction2 != 'UP':
            direction2 = 'DOWN'
        if change2_to == 'LEFT' and direction2 != 'RIGHT':
            direction2 = 'LEFT'
        if change2_to == 'RIGHT' and direction2 != 'LEFT':
            direction2 = 'RIGHT'


    # Moving the snake 1
    if direction1 == 'UP':
        snake1_pos[1] -= 10
    if direction1 == 'DOWN':
        snake1_pos[1] += 10
    if direction1 == 'LEFT':
        snake1_pos[0] -= 10
    if direction1 == 'RIGHT':
        snake1_pos[0] += 10

    # Moving the snake 1
    if direction2 == 'UP':
        snake2_pos[1] -= 10
    if direction2 == 'DOWN':
        snake2_pos[1] += 10
    if direction2 == 'LEFT':
        snake2_pos[0] -= 10
    if direction2 == 'RIGHT':
        snake2_pos[0] += 10

    # Snake body growing mechanism
    snake1_body.insert(0, list(snake1_pos))
    snake2_body.insert(0, list(snake2_pos))
    score += 1

    # GFX
    game_window.fill(black)
    for pos in snake1_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    for pos in snake2_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Game Over conditions
    # Getting out of bounds
    if snake1_pos[0] < 0 or snake1_pos[0] > frame_size_x:
        game_over(1)
    if snake1_pos[1] < 0 or snake1_pos[1] > frame_size_y:
        game_over(1)
    # Touching the snake body
    for block1 in snake1_body[1:]:
        if snake1_pos[0] == block1[0] and snake1_pos[1] == block1[1]:
            game_over(1)
    for block2 in snake2_body[1:]:
        if snake1_pos[0] == block2[0] and snake1_pos[1] == block2[1]:
            game_over(1)

    #Player 2
    if snake2_pos[0] < 0 or snake2_pos[0] > frame_size_x:
        print("debug15")
        game_over(2)
    if snake2_pos[1] < 0 or snake2_pos[1] > frame_size_y:
        print("debug16")
        game_over(2)
    # Touching the snake body
    for block2 in snake2_body[1:]:
        if snake2_pos[0] == block2[0] and snake2_pos[1] == block2[1]:
            print("debug17")
            game_over(2)
    for block1 in snake1_body[1:]:
        if snake2_pos[0] == block1[0] and snake2_pos[1] == block1[1]:
            print("debug18")
            game_over(2)


    show_score(1, white, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(difficulty)
