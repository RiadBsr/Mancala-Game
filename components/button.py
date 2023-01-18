import os
import pygame

font_sizes = {
    "Very big": 100,
    "Big": 64,
    "Medium": 48,
    "Small": 32,
    "Very small": 24
}

class Button:
    def __init__(self, game, text, size, position, handler):
        self.pressed = False

        self.game = game
        self.handler = handler
        self.text = text
        self.position = position

        self.size = size
        self.font_size = font_sizes[size]

    def draw(self, surface):
        self.font = pygame.font.Font(
            os.path.join(self.game.font_dir, "Inter.ttf"), self.font_size
        )
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.position

        surface.blit(self.text_surface, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.text_rect.collidepoint(mouse_pos):
            if self.font_size < font_sizes[self.size]+6:
                self.font_size += 1
            if pygame.mouse.get_pressed()[0]:
                self.font_size -= 2
                self.pressed = True
            else:
                if self.pressed == True:
                    self.handler()
                    self.pressed = False
        elif self.font_size > font_sizes[self.size]:
            self.font_size -= 1
