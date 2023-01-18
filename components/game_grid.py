import pygame

LINE_WIDTH = 4

class GameGrid:
    def __init__(self, game, size, level_state):
        self.game = game      
        self.level_state = level_state
    
        self.board_w, self.board_h = size

        self.board_surface = pygame.Surface((self.board_w, self.board_h))

        # Frame stuff
        self.board_rect = self.board_surface.get_rect()
        self.board_rect.center = (game.GAME_W / 2, game.GAME_H / 2)


    def draw(self, surface):
        self.board_surface.fill((0,0,0))
        self.draw_map()

        surface.blit(self.board_surface, self.board_rect)

    def draw_map(self):
        pygame.draw.line(
            self.board_surface, (255, 255, 255), (0, 0), (self.board_w, 0), LINE_WIDTH
        )
        pygame.draw.line(
            self.board_surface,
            (255, 255, 255),
            (self.board_w - 2, 0),
            (self.board_w - 2, self.board_h),
            LINE_WIDTH,
        )
        pygame.draw.line(
            self.board_surface,
            (255, 255, 255),
            (self.board_w, self.board_h - 2),
            (0, self.board_h - 2),
            LINE_WIDTH,
        )
        pygame.draw.line(
            self.board_surface, (255, 255, 255), (0, self.board_h), (0, 0), LINE_WIDTH
        )
        cup_size = self.board_h / 2
        pygame.draw.line(
            self.board_surface, 
            (255, 255, 255), 
            (cup_size, self.board_h/2), 
            (self.board_w-cup_size,self.board_h/2), 
            LINE_WIDTH
        )
        for i in range(1,8):
            pygame.draw.line(
                self.board_surface, (255,255,255), (cup_size*i, 0),(cup_size*i, self.board_h), LINE_WIDTH
            )

        
