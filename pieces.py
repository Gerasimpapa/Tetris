"""
Tetromino pieces definitions and handling
"""
import random
from constants import COLORS

# Tetromino shapes (as relative coordinates from top-left)
PIECE_SHAPES = {
    'I': [(0, 1), (1, 1), (2, 1), (3, 1)],      # Straight line
    'O': [(0, 0), (0, 1), (1, 0), (1, 1)],      # Square
    'T': [(0, 1), (1, 0), (1, 1), (2, 1)],      # T-shape
    'S': [(0, 1), (1, 0), (1, 1), (2, 0)],      # S-shape
    'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],      # Z-shape
    'J': [(0, 0), (0, 1), (1, 1), (2, 1)],      # J-shape
    'L': [(0, 1), (1, 1), (2, 0), (2, 1)],      # L-shape
}

# Rotation states for each piece (not all pieces need all rotations)
ROTATIONS = {
    'I': [
        [(0, 1), (1, 1), (2, 1), (3, 1)],       # Horizontal
        [(1, 0), (1, 1), (1, 2), (1, 3)],       # Vertical
    ],
    'O': [
        [(0, 0), (0, 1), (1, 0), (1, 1)],       # No rotation needed
    ],
    'T': [
        [(0, 1), (1, 0), (1, 1), (2, 1)],       # Up (normal)
        [(0, 0), (1, 0), (1, 1), (1, 2)],       # Right
        [(0, 1), (1, 0), (1, 1), (2, 1)],       # Down (same as up for symmetry)
        [(0, 0), (0, 1), (0, 2), (1, 1)],       # Left
    ],
    'S': [
        [(0, 1), (1, 0), (1, 1), (2, 0)],       # Horizontal
        [(0, 0), (1, 0), (1, 1), (2, 1)],       # Vertical
    ],
    'Z': [
        [(0, 0), (1, 0), (1, 1), (2, 1)],       # Horizontal
        [(0, 1), (1, 0), (1, 1), (2, 0)],       # Vertical
    ],
    'J': [
        [(0, 0), (0, 1), (1, 1), (2, 1)],       # Up
        [(0, 0), (1, 0), (1, 1), (1, 2)],       # Right
        [(0, 1), (1, 1), (2, 0), (2, 1)],       # Down
        [(0, 0), (0, 1), (0, 2), (1, 2)],       # Left
    ],
    'L': [
        [(0, 1), (1, 1), (2, 0), (2, 1)],       # Up
        [(1, 0), (0, 1), (0, 2), (1, 2)],       # Right
        [(0, 0), (1, 0), (2, 0), (2, 1)],       # Down
        [(0, 0), (1, 0), (1, 1), (1, 2)],       # Left
    ],
}


class Piece:
    """Represents a Tetromino piece"""
    
    def __init__(self, piece_type=None):
        if piece_type is None:
            piece_type = random.choice(list(PIECE_SHAPES.keys()))
        
        self.piece_type = piece_type
        self.color = COLORS[piece_type]
        self.rotation_state = 0
        self.x = 3  # Starting X position (center-ish)
        self.y = 0  # Starting Y position (top)
        
    def get_cells(self):
        """Returns the current cells occupied by this piece"""
        if self.piece_type in ROTATIONS:
            shape = ROTATIONS[self.piece_type][self.rotation_state]
        else:
            shape = PIECE_SHAPES[self.piece_type]
        
        cells = []
        for dx, dy in shape:
            cells.append((self.x + dx, self.y + dy))
        return cells
    
    def rotate(self):
        """Rotate the piece clockwise"""
        if self.piece_type in ROTATIONS:
            self.rotation_state = (self.rotation_state + 1) % len(ROTATIONS[self.piece_type])
    
    def move_left(self):
        """Move piece left"""
        self.x -= 1
    
    def move_right(self):
        """Move piece right"""
        self.x += 1
    
    def move_down(self):
        """Move piece down"""
        self.y += 1
    
    def undo_move_left(self):
        """Undo left move"""
        self.x += 1
    
    def undo_move_right(self):
        """Undo right move"""
        self.x -= 1
    
    def undo_move_down(self):
        """Undo down move"""
        self.y -= 1
    
    def undo_rotate(self):
        """Undo rotation"""
        self.rotation_state = (self.rotation_state - 1) % len(ROTATIONS.get(self.piece_type, [0]))


def get_random_piece():
    """Get a random Tetromino piece"""
    return Piece()
