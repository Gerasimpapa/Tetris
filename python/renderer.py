"""
Game rendering using Pygame
"""
import pygame
from constants import (
    BOARD_WIDTH, BOARD_HEIGHT, CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT,
    SIDEBAR_WIDTH, BLACK, WHITE, GRAY, LIGHT_GRAY, COLORS, GAME_OVER
)


class Renderer:
    """Handles all game rendering"""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH + SIDEBAR_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.font_large = pygame.font.Font(None, 36)
        self.font_medium = pygame.font.Font(None, 24)
        self.font_small = pygame.font.Font(None, 18)
        self.clock = pygame.time.Clock()
    
    def draw_game(self, game):
        """Draw the entire game"""
        # Clear screen
        self.screen.fill(BLACK)
        
        # Draw board background
        pygame.draw.rect(self.screen, GRAY, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Draw grid
        self.draw_grid()
        
        # Draw locked pieces
        self.draw_board(game.get_board())
        
        # Draw current piece
        self.draw_piece(game.get_current_piece())
        
        # Draw sidebar
        self.draw_sidebar(game)
        
        # Draw game over if needed
        if game.state == GAME_OVER:
            self.draw_game_over(game)
        
        pygame.display.flip()
    
    def draw_grid(self):
        """Draw the game grid"""
        for x in range(BOARD_WIDTH + 1):
            pygame.draw.line(
                self.screen,
                LIGHT_GRAY,
                (x * CELL_SIZE, 0),
                (x * CELL_SIZE, SCREEN_HEIGHT)
            )
        
        for y in range(BOARD_HEIGHT + 1):
            pygame.draw.line(
                self.screen,
                LIGHT_GRAY,
                (0, y * CELL_SIZE),
                (SCREEN_WIDTH, y * CELL_SIZE)
            )
    
    def draw_board(self, board):
        """Draw all locked pieces on the board"""
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if board[y][x] is not None:
                    self.draw_cell(x, y, board[y][x])
    
    def draw_piece(self, piece):
        """Draw the current falling piece"""
        cells = piece.get_cells()
        for x, y in cells:
            if 0 <= y < BOARD_HEIGHT:  # Only draw visible cells
                self.draw_cell(x, y, piece.color)
    
    def draw_cell(self, x, y, color):
        """Draw a single cell"""
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, BLACK, rect, 1)
    
    def draw_sidebar(self, game):
        """Draw the sidebar with score and next piece"""
        sidebar_x = SCREEN_WIDTH
        
        # Draw background
        pygame.draw.rect(self.screen, LIGHT_GRAY, (sidebar_x, 0, SIDEBAR_WIDTH, SCREEN_HEIGHT))
        
        # Draw score
        score_text = self.font_medium.render("Score", True, BLACK)
        self.screen.blit(score_text, (sidebar_x + 10, 20))
        
        score_value = self.font_large.render(str(game.score), True, BLACK)
        self.screen.blit(score_value, (sidebar_x + 10, 50))
        
        # Draw lines cleared
        lines_text = self.font_medium.render("Lines", True, BLACK)
        self.screen.blit(lines_text, (sidebar_x + 10, 100))
        
        lines_value = self.font_large.render(str(game.lines_cleared), True, BLACK)
        self.screen.blit(lines_value, (sidebar_x + 10, 130))
        
        # Draw next piece
        next_text = self.font_medium.render("Next", True, BLACK)
        self.screen.blit(next_text, (sidebar_x + 10, 200))
        
        self.draw_next_piece(game.get_next_piece(), sidebar_x + 10, 240)
        
        # Draw controls
        controls_y = 400
        controls = [
            "Controls:",
            "Arrow Keys: Move",
            "Space: Rotate",
            "D: Hard Drop",
            "P: Pause",
            "R: Restart"
        ]
        
        for i, text in enumerate(controls):
            control_text = self.font_small.render(text, True, BLACK)
            self.screen.blit(control_text, (sidebar_x + 5, controls_y + i * 25))
    
    def draw_next_piece(self, piece, offset_x, offset_y):
        """Draw the next piece preview in the sidebar"""
        cells = piece.get_cells()
        
        # Find bounding box
        if cells:
            min_x = min(x for x, y in cells)
            min_y = min(y for x, y in cells)
            
            for x, y in cells:
                draw_x = offset_x + (x - min_x) * CELL_SIZE
                draw_y = offset_y + (y - min_y) * CELL_SIZE
                rect = pygame.Rect(draw_x, draw_y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, piece.color, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)
    
    def draw_game_over(self, game):
        """Draw game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.font_large.render("GAME OVER", True, WHITE)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
        self.screen.blit(game_over_text, text_rect)
        
        # Final score
        final_score = self.font_medium.render(f"Final Score: {game.score}", True, WHITE)
        score_rect = final_score.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(final_score, score_rect)
        
        # Restart message
        restart_text = self.font_small.render("Press R to restart or Q to quit", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        self.screen.blit(restart_text, restart_rect)
    
    def set_title(self, title):
        """Set window title"""
        pygame.display.set_caption(title)
    
    def get_clock(self):
        """Get the pygame clock"""
        return self.clock
