# import pygame library
import pygame
import requests
from bs4 import BeautifulSoup

# initialise the pygame font
pygame.font.init()

# Total window
screen = pygame.display.set_mode((500, 600))

# Title and Icon
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")

x = 0
y = 0
dif = 500 / 9
val = 0
# Default Sudoku Board.
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)


def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

    # Function to draw required lines for making Sudoku grid


def draw():
    # Draw the lines

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

                # Fill gird with default numbers specified
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
                # Draw lines horizontally and verticallyto form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

    # Fill value entered in cell


def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))


# Raise error when wrong value entered
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


# Check if the value entered in board is valid
def valid(m, i, j, val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i // 3
    jt = j // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == val:
                return False
    return True


# Solves the sudoku board using Backtracking Algorithm
def solve(grid, i, j):
    while grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if valid(grid, i, j, it) == True:
            grid[i][j] = it
            global x, y
            x = i
            y = j
            # white color background\
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j) == 1:
                return True
            else:
                grid[i][j] = 0
            # white color background\
            screen.fill((255, 255, 255))

            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False


# Display instruction for the game
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))


# Display options when solved
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
# The loop thats keep the window running
while run:

    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False
            # Get the mouse postion to insert number
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
            # Get the number to be inserted if key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
                # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0

                grid = []
                URL = 'http://www.menneske.no/sudoku/eng/random.html?diff=7'

                page = requests.get(URL)

                soup = BeautifulSoup(page.content, 'html.parser')

                grid_txt = soup.find_all('div', {'class': 'grid'})[0].text

                puzzle_no = grid_txt[str.find(grid_txt, 'Showing puzzle') + 23:str.find(grid_txt, 'Puzzletype')]

                rows = soup.find_all('tr', {'class': 'grid'})

                puzzle = []

                for row in rows:
                    cols = row.find_all('td')
                    for col in cols:
                        txt = col.text
                        if txt != '\xa0':
                            par = int(txt)
                            puzzle.append(par)
                        else:
                            puzzle.append(0)

                grid = []

                list1 = []

                list2 = []

                list3 = []

                list4 = []

                list5 = []

                list6 = []

                list7 = []

                list8 = []

                list9 = []

                for i in range(0, 9):
                    list1.append(puzzle[i])
                    del puzzle[i]

                grid.append(list1)

                for i in range(0, 9):
                    list2.append(puzzle[i])
                    del puzzle[i]

                grid.append(list2)

                for i in range(0, 9):
                    list3.append(puzzle[i])
                    del puzzle[i]

                grid.append(list3)

                for i in range(0, 9):
                    list4.append(puzzle[i])
                    del puzzle[i]

                grid.append(list4)

                for i in range(0, 9):
                    list5.append(puzzle[i])
                    del puzzle[i]

                grid.append(list5)

                for i in range(0, 9):
                    list6.append(puzzle[i])
                    del puzzle[i]

                grid.append(list6)

                for i in range(0, 9):
                    list7.append(puzzle[i])
                    del puzzle[i]

                grid.append(list7)

                for i in range(0, 9):
                    list8.append(puzzle[i])
                    del puzzle[i]

                grid.append(list8)

                for i in range(0, 9):
                    list9.append(puzzle[i])

                grid.append(list9)

                # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
    if flag2 == 1:
        if solve(grid, 0, 0) == False:
            error = 1
        else:
            rs = 1
        flag2 = 0
    if val != 0:
        draw_val(val)
        # print(x)
        # print(y)
        if valid(grid, int(x), int(y), val) == True:
            grid[int(x)][int(y)] = val
            flag1 = 0
        else:
            grid[int(x)][int(y)] = 0
            raise_error2()
        val = 0

    if error == 1:
        raise_error1()
    if rs == 1:
        result()
    draw()
    if flag1 == 1:
        draw_box()
    instruction()

    # Update window
    pygame.display.update()

# Quit pygame window
pygame.quit()
