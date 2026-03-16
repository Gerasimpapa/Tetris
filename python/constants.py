# Game Constants
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
CELL_SIZE = 30

# Screen dimensions
SCREEN_WIDTH = BOARD_WIDTH * CELL_SIZE
SCREEN_HEIGHT = BOARD_HEIGHT * CELL_SIZE
SIDEBAR_WIDTH = 150

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)

# Tetromino colors
COLORS = {
    'I': (0, 240, 240),      # Cyan
    'O': (240, 240, 0),      # Yellow
    'T': (240, 0, 240),      # Magenta
    'S': (0, 240, 0),        # Green
    'Z': (240, 0, 0),        # Red
    'J': (0, 0, 240),        # Blue
    'L': (240, 160, 0),      # Orange
}

# Game states
PLAYING = 0
PAUSED = 1
GAME_OVER = 2

# Game speed
INITIAL_FALL_SPEED = 0.5  # blocks per second
