import pygame
import sys

# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (23, 145, 135)
GREEN = (0, 255, 0)

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe game:")

display_surface.fill(WHITE)


def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(
            display_surface,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            15,
        )
        pygame.draw.line(
            display_surface,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, WIDTH),
            15,
        )


def check_winner(board, player):
    # Check rows and columns
    for i in range(BOARD_ROWS):
        if all(board[i][j] == player for j in range(BOARD_COLS)) or all(
            board[j][i] == player for j in range(BOARD_ROWS)
        ):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or all(
        board[i][BOARD_COLS - 1 - i] == player for i in range(BOARD_ROWS)
    ):
        return True
    return False


def draw_move(row, col, player):
    centerX = col * SQUARE_SIZE + SQUARE_SIZE // 2
    centerY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    radius = SQUARE_SIZE // 3

    if player == "X":
        pygame.draw.line(
            display_surface,
            BLACK,
            (centerX - radius, centerY - radius),
            (centerX + radius, centerY + radius),
            5,
        )
        pygame.draw.line(
            display_surface,
            BLACK,
            (centerX + radius, centerY - radius),
            (centerX - radius, centerY + radius),
            5,
        )
    else:
        pygame.draw.circle(display_surface, BLACK, (centerX, centerY), radius, 5)


def main():
    running = True
    currentPlayer = "X"
    board = [[" " for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == " ":
                board[clicked_row][clicked_col] = currentPlayer
                draw_move(clicked_row, clicked_col, currentPlayer)
                if check_winner(board, currentPlayer):
                    print(f"Player {currentPlayer} wins!")
                    running = False
            currentPlayer = (
                "O" if currentPlayer == "X" else "X" 
                  )      # Switch player
        draw_grid()
        pygame.display.update()

    pygame.quit()
    sys.exit()

    #


if __name__ == "__main__":
    main()
