from components.button import Button, font_sizes
import pygame
import os

class ButtonCup(Button):

    def __init__(self, game, text, size, position, handler, cup, game_level, owner):
        super().__init__(game, text, size, position, handler)

        self.cup = cup
        self.game_level = game_level
        self.owner = owner

    def draw(self, surface):
        self.font = pygame.font.Font(
            os.path.join(self.game.font_dir, "Inter.ttf"), self.font_size
        )
        color = (255, 255, 255)
        if self.owner != self.game_level.turn:
            color = (100, 100, 100)
        self.text_surface = self.font.render(self.text, True, color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.position

        surface.blit(self.text_surface, self.text_rect)
        if self.cup in self.game_level.level.possibleMoves(self.game_level.turn):
            self.check_click()
    
    def opposite_player(self, Player):
        if Player == 1:
            return 2
        return 1

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.text_rect.collidepoint(mouse_pos):
            if self.font_size < font_sizes[self.size]+6:
                self.font_size += 2
            if pygame.mouse.get_pressed()[0]:
                self.font_size -= 4
                self.pressed = True
            else:
                if self.pressed == True:
                    play_again = self.handler(self.game_level.turn, self.cup)
                    self.game_level.initialize_cups()
                    self.game_level.time_start = pygame.time.get_ticks()
                    if not play_again:
                        self.game_level.turn = self.opposite_player(self.game_level.turn)
                    self.pressed = False
        elif self.font_size > font_sizes[self.size]:
            self.font_size -= 2