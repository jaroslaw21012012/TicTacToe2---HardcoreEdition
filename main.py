import sys, pygame, time
from pygame.locals import *
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TicTacToe2 - hardcore edition")

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BG = (39, 151, 128)
BG_BOARD = (140, 177, 107)
X = (249, 115, 42)
O = (242, 244, 213)




def game():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(None)
        board.append(row)
    print(board)
    player = "X"
    history_x = []
    history_O = []
    win = False
    line = 0
    d = 500 / 3 / 2

    while True:
        #BG
        display.fill(BG)
        #BOARD
        pygame.draw.rect(display, BG_BOARD, (50, 50, 500, 500), border_radius=10)
        #BORDER_LINES
        pygame.draw.line(display, BG, (50 + (500 / 3), 50), (50 + (500 / 3), 550), width=5)
        pygame.draw.line(display, BG, (50 + (500 / 3 * 2), 50), (50 + (500 / 3 * 2), 550), width=5)
        pygame.draw.line(display, BG, (50, 50 + (500 / 3)), (550, 50 + (500 / 3)), width=5)
        pygame.draw.line(display, BG, (50, 50 + (500 / 3 * 2)), (550, 50 + (500 / 3 * 2)), width=5)
        #.
        if line == 1:
            pygame.draw.line(display, BLACK, (50, 50 + 500 / 3 / 2), (550, 50 + 500 / 3 / 2), width=5)
        elif line == 2:
            pygame.draw.line(display, BLACK, (50, 50 + 500 / 3 + d), (550, 50 + 500 / 3 + d), width=5)
        elif line == 3:
            pygame.draw.line(display, BLACK, (50, 50 + 500 / 3 * 2 + d), (550, 50 + 500 / 3 * 2 + d), width=5)
        elif line == 4:
            pygame.draw.line(display, BLACK, (50 + 500 / 3 / 2, 50), (50 + 500 / 3 / 2, 550), width=5)
        elif line == 5:
            pygame.draw.line(display, BLACK, (50 + 500 / 3 + d, 50), (50 + 500 / 3 + d, 550), width=5)
        elif line == 6:
            pygame.draw.line(display, BLACK, (50 + 500 / 3 * 2 + d, 50), (50 + 500 / 3 * 2 + d, 550), width=5)
        elif line == 7:
            pygame.draw.line(display, BLACK, (50, 50), (550, 550), width=5)
        elif line == 8:
            pygame.draw.line(display, BLACK, (50, 550), (550, 50), width=5)
        for y in range(len(board)):
            for x in range(len(board[y])):
                symbol = board[y][x]
                center_x = 50 + (500 / 3 / 2) + (500 / 3 / 2) * x + (500 / 3 / 2) * x
                center_y = 50 + (500 / 3 / 2) + (500 / 3 / 2) * y + (500 / 3 / 2) * y
                if symbol == "X":
                    pygame.draw.line(display, X, (center_x - 50, center_y - 50), (center_x + 50, center_y + 50),
                                    width=10)
                    pygame.draw.line(display, X, (center_x - 50, center_y + 50), (center_x + 50, center_y - 50),
                                     width=10)
                elif symbol == "O":
                    pygame.draw.circle(display, O, (center_x, center_y), radius=50, width=10)
        #X WINS
        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
            win = True
            line = 1
        elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
            win = True
            line = 2
        elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
            win = True
            line = 3
        elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
            win = True
            line = 4
        elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
            win = True
            line = 5
        elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
            win = True
            line = 6
        elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            win = True
            line = 7
        elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
            win = True
            line = 8
        # O WINS
        if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
            win = True
            line = 1
        elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
            win = True
            line = 2
        elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
            win = True
            line = 3
        elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
            win = True
            line = 4
        elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
            win = True
            line = 5
        elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
            win = True
            line = 6
        elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
            win = True
            line = 7
        elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
            win = True
            line = 8
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == MOUSEBUTTONDOWN:
                if not win:
                    for y in range(len(board)):
                        for x in range(len(board[y])):
                            symbol = board[y][x]
                            center_x = 50 + (500 / 3 / 2) + (500 / 3 / 2) * x + (500 / 3 / 2) * x
                            center_y = 50 + (500 / 3 / 2) + (500 / 3 / 2) * y + (500 / 3 / 2) * y
                            rect = pygame.Rect(center_x - (500 / 3 / 2), center_y - (500 / 3 / 2), 500 / 3, 500 / 3)
                            if rect.collidepoint(event.pos[0], event.pos[1]):
                                if board[y][x]:
                                    break
                                board[y][x] = player
                                if player == "X":
                                    history_x.append([y, x])
                                    if len(history_x) > 3:
                                        y, x = history_x[0]
                                        board[y][x] = None
                                        history_x.pop(0)
                                    player = "O"
                                else:
                                    history_O.append([y, x])
                                    if len(history_O) > 3:
                                        y, x = history_O[0]
                                        board[y][x] = None
                                        history_O.pop(0)
                                    player = "X"
                                break
        pygame.display.update()
        clock.tick(FPS)










if __name__ == '__main__':
    game()