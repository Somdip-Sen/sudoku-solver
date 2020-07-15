import Sudoku
from Sudoku import board  # imported board from another module (Because I am Lazy:) )
import pygame
import time
from threading import *  # multi threading for better performance

mouseX, mouseY = 0, 0
Time, back, signal, hold = True, False, False, False


# Time -> control the Time


def check(board1, board2):  # check if the given solution and the original solution is same
    for i in range(9):
        for j in range(9):
            if board1[i][j] != board2[i][j]:
                return False
    return True


def button(text_):
    global signal
    while not hold:
        if 50 < mouseX < 150 and 460 < mouseY < 490:
            pygame.draw.rect(button_canvas, (170, 170, 170), (50, 10, 100, 30))
            signal = True
        else:
            pygame.draw.rect(button_canvas, (100, 100, 100), (50, 10, 100, 30))
        button_canvas.blit(text_, (58, 17))
        pygame.display.update((0, 450, 200, 50))


def display_number(board_curr):
    for i in range(9):
        for j in range(9):
            if board_curr[i][j] != 0:
                number = font.render(str(board_curr[i][j]), True, (255, 255, 255))
                screen.blit(number, (j * 50 + 20, i * 50 + 15))


def show_time():  # display time in another thread
    secs = 0
    while Time:
        sec = secs % 60
        minute = secs // 60
        hr = minute // 60
        format_ = u'{:02d}:{:02d}:{:02d}'.format(hr, minute, sec)
        text3 = font.render("Time: " + format_, True, (255, 255, 255))
        time_canvas.fill((0, 0, 0))
        time_canvas.blit(text3, (100, 10))
        time.sleep(1)
        secs += 1  # second calculation
        pygame.display.update((0, 450, 450, 50))


def playGUI():
    win, flag, show, over = False, False, False, False
    x, y = None, None
    global Time, mouseX, mouseY, signal, hold, back
    t3 = Thread(target=show_time)  # thread for show_time()
    t3.start()
    while True:
        canvas.fill((49, 150, 100))
        button_canvas.fill((0, 0, 0))
        event = pygame.event.wait()  # gets a single event from the event queue
        if event.type == pygame.QUIT:  # if the 'close' button of the window is pressed
            pygame.quit()
            exit()  # stop the execution

        # if any mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            x_, y_ = x, y
            x, y = (event.pos[0] // 50 * 50), (event.pos[1] // 50 * 50)
            flag = True if x_ == x and y_ == y else False  # check if the same block is clicked again
            pygame.draw.rect(canvas, (255, 0, 0), (x, y, 50, 50))

        # if any mouse button is released
        elif event.type == pygame.MOUSEBUTTONUP:
            if flag:
                x, y = None, None  # de-select
            mouseX, mouseY = 0, 0

        if x is not None:
            pygame.draw.rect(canvas, (255, 0, 0), (x, y, 50, 50))  # highlight the selected block
            pygame.draw.rect(canvas, (49, 150, 100), (x + 4, y + 4, 42, 42))

        for i in range(1, 10):
            pygame.draw.line(canvas, (0, 0, 0), (50 * i, 0), (50 * i, 450),
                             1 if i % 3 != 0 else 3)  # checker board making
            pygame.draw.line(canvas, (0, 0, 0), (0, 50 * i), (450, 50 * i), 1 if i % 3 != 0 else 3)

        # display numbers in their corresponding blocks
        if show:
            display_number(board_cpy)
        else:
            display_number(board)

        # number input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                board[y // 50][x // 50] = 1
            elif event.key == pygame.K_2:
                board[y // 50][x // 50] = 2
            elif event.key == pygame.K_3:
                board[y // 50][x // 50] = 3
            elif event.key == pygame.K_4:
                board[y // 50][x // 50] = 4
            elif event.key == pygame.K_5:
                board[y // 50][x // 50] = 5
            elif event.key == pygame.K_6:
                board[y // 50][x // 50] = 6
            elif event.key == pygame.K_7:
                board[y // 50][x // 50] = 7
            elif event.key == pygame.K_8:
                board[y // 50][x // 50] = 8
            elif event.key == pygame.K_9:
                board[y // 50][x // 50] = 9
            elif event.key == pygame.K_KP_ENTER:  # go for result
                if not show:
                    win = check(board, board_cpy)
                    over = True
                    hold = True
            elif event.key == pygame.K_MINUS:  # removing the selected numbers
                board[y // 50][x // 50] = 0

            if x is not None:  # key navigation
                if event.key == pygame.K_UP:
                    y -= 50
                elif event.key == pygame.K_DOWN:
                    y += 50
                elif event.key == pygame.K_LEFT:
                    x -= 50
                elif event.key == pygame.K_RIGHT:
                    x += 50

        if signal:
            show = True
            Time = False  # Stop the Clock

        # game over - result display
        while over:
            font1 = pygame.font.SysFont('game_over.ttf', 70)
            canvas.fill((49, 150, 100))
            if win:
                canvas.blit(font1.render("You Win", True, (255, 255, 255)), (125, 210))

            else:
                canvas.blit(font1.render("You Lose", True, (255, 255, 255)), (125, 210))
            Time = False
            canvas.blit(font.render("Click to see the board ...", True, (255, 255, 255)), (155, 270))
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN:  # back to game again ( time to correct your mistakes :) )
                over = False
                hold = False
                back = True

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            time_canvas.fill((49, 150, 100))
            button_canvas.fill((49, 150, 100))

            pygame.display.flip()  # update the whole screen

        pygame.display.update((0, 0, 450, 450))


if __name__ == '__main__':
    pygame.init()  # initialize
    font = pygame.font.SysFont('arial', 20)
    button_font = pygame.font.SysFont('Corbel', 14, bold=True)
    text = button_font.render('Show Answer', True, (0, 0, 0))
    pygame.display.set_caption("Tinku r Challenge")  # sets the window title
    screen = pygame.display.set_mode((450, 500))  # sets the window size
    canvas = screen.subsurface((0, 0), (450, 450))
    time_canvas = screen.subsurface((200, 450), (250, 50))
    button_canvas = screen.subsurface((0, 450), (200, 50))
    start = time.time()
    board_cpy = [row[:] for row in board]
    t1 = Thread(target=Sudoku.solve, args=(0, 0, board_cpy))
    t2 = Thread(target=button, args=(text,))
    t2.start()
    t1.start()
    playGUI()
    t1.join()
    t2.join()
