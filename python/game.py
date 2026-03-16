"""
Core Tetris game logic
"""
from constants import BOARD_WIDTH, BOARD_HEIGHT, PLAYING, GAME_OVER
from pieces import get_random_piece


class TetrisGame:
    """Main game logic class"""
    
    def __init__(self):
        self.board = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_piece = get_random_piece()
        self.next_piece = get_random_piece()
        self.score = 0
        self.lines_cleared = 0
        self.state = PLAYING
        self.fall_counter = 0
        self.fall_speed = 0.5  # blocks per second
        
    def update(self, dt):
        """Update game state (dt is delta time in seconds)"""
        if self.state != PLAYING:
            return
        
        # Update fall counter
        self.fall_counter += dt * self.fall_speed
        
        if self.fall_counter >= 1.0:
            self.fall_counter = 0
            if not self.move_piece_down():
                # Piece can't move down, lock it
                self.lock_piece()
                self.check_lines()
                self.spawn_new_piece()
    
    def move_piece_down(self):
        """Move current piece down. Returns True if successful, False if blocked"""
        self.current_piece.move_down()
        if self.is_valid_position():
            return True
        else:
            self.current_piece.undo_move_down()
            return False
    
    def move_piece_left(self):
        """Move current piece left"""
        self.current_piece.move_left()
        if not self.is_valid_position():
            self.current_piece.undo_move_left()
    
    def move_piece_right(self):
        """Move current piece right"""
        self.current_piece.move_right()
        if not self.is_valid_position():
            self.current_piece.undo_move_right()
    
    def rotate_piece(self):
        """Rotate current piece"""
        self.current_piece.rotate()
        if not self.is_valid_position():
            self.current_piece.undo_rotate()
    
    def hard_drop(self):
        """Drop piece all the way to the bottom"""
        while self.move_piece_down():
            self.score += 2
    
    def is_valid_position(self):
        """Check if current piece is in valid position"""
        cells = self.current_piece.get_cells()
        
        for x, y in cells:
            # Check bounds
            if x < 0 or x >= BOARD_WIDTH or y < 0 or y >= BOARD_HEIGHT:
                return False
            # Check collision with locked pieces
            if y >= 0 and self.board[y][x] is not None:
                return False
        
        return True
    
    def lock_piece(self):
        """Lock the current piece onto the board"""
        cells = self.current_piece.get_cells()
        
        for x, y in cells:
            if 0 <= y < BOARD_HEIGHT and 0 <= x < BOARD_WIDTH:
                self.board[y][x] = self.current_piece.color
    
    def check_lines(self):
        """Check for and clear completed lines"""
        lines_to_clear = []
        
        for y in range(BOARD_HEIGHT):
            if all(self.board[y][x] is not None for x in range(BOARD_WIDTH)):
                lines_to_clear.append(y)
        
        # Clear lines
        for y in reversed(lines_to_clear):
            del self.board[y]
            self.board.insert(0, [None for _ in range(BOARD_WIDTH)])
        
        # Update score and statistics
        num_lines = len(lines_to_clear)
        if num_lines > 0:
            self.lines_cleared += num_lines
            # Scoring: 100 for 1 line, 300 for 2, 500 for 3, 800 for 4
            scores = {1: 100, 2: 300, 3: 500, 4: 800}
            self.score += scores.get(num_lines, 0)
            
            # Increase fall speed slightly
            self.fall_speed += 0.02
    
    def spawn_new_piece(self):
        """Spawn a new piece"""
        self.current_piece = self.next_piece
        self.next_piece = get_random_piece()
        
        # Check if game is over (piece can't be placed)
        if not self.is_valid_position():
            self.state = GAME_OVER
    
    def get_board(self):
        """Get the current board state"""
        return self.board
    
    def get_current_piece(self):
        """Get the current piece"""
        return self.current_piece
    
    def get_next_piece(self):
        """Get the next piece"""
        return self.next_piece
    
    def reset(self):
        """Reset the game"""
        self.__init__()
