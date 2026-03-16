"""
Tetris Game - Main entry point
"""
import pygame
import sys
from game import TetrisGame
from renderer import Renderer
from constants import PLAYING, PAUSED, GAME_OVER


class TetrisApplication:
    """Main application class"""
    
    def __init__(self):
        pygame.init()
        self.game = TetrisGame()
        self.renderer = Renderer()
        self.running = True
        self.paused = False
        
    def handle_events(self):
        """Handle user input and events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    self.running = False
                
                elif event.key == pygame.K_p:
                    # Pause/unpause
                    if self.game.state == PLAYING:
                        self.game.state = PAUSED
                    elif self.game.state == PAUSED:
                        self.game.state = PLAYING
                
                elif event.key == pygame.K_r:
                    # Restart game
                    self.game.reset()
                    self.paused = False
                
                elif self.game.state == PLAYING:
                    # Game controls
                    if event.key == pygame.K_LEFT:
                        self.game.move_piece_left()
                    elif event.key == pygame.K_RIGHT:
                        self.game.move_piece_right()
                    elif event.key == pygame.K_DOWN:
                        self.game.hard_drop()
                    elif event.key == pygame.K_UP:
                        self.game.rotate_piece()
    
    def update(self, dt):
        """Update game state"""
        if self.game.state == PLAYING:
            self.game.update(dt)
    
    def render(self):
        """Render the game"""
        self.renderer.draw_game(self.game)
    
    def run(self):
        """Main game loop"""
        clock = self.renderer.get_clock()
        target_fps = 60
        
        while self.running:
            dt = clock.tick(target_fps) / 1000.0  # Convert to seconds
            
            self.handle_events()
            self.update(dt)
            self.render()
        
        pygame.quit()
        sys.exit()


def main():
    """Entry point"""
    app = TetrisApplication()
    app.run()


if __name__ == "__main__":
    main()
