import os
import pygame


class ArrowButton:
    def __init__(self, game, direction, position, handler):
        self.pressed = False

        self.game = game
        self.handler = handler
        self.position = position
        self.direction = direction

        self.arrow = pygame.image.load(
            os.path.join(game.sprite_dir, "arrow", direction + ".png")
        ).convert_alpha()
        self.arrow_rect = self.arrow.get_rect(center=position)

    def draw(self, surface):
        surface.blit(self.arrow, self.arrow_rect)
        self.check_click()
        pass

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.arrow_rect.collidepoint(mouse_pos):
            self.in_hover_effect()
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    self.handler()
                    self.pressed = False
        else:
            self.out_hover_effect()

    def in_hover_effect(self):
        if self.direction == "right":
            if self.arrow_rect.center[0] < self.position[0] + 10:
                self.arrow_rect.center = (
                    self.arrow_rect.center[0] + 1,
                    self.arrow_rect.center[1],
                )
        else:
            if self.arrow_rect.center[0] > self.position[0] - 10:
                self.arrow_rect.center = (
                    self.arrow_rect.center[0] - 1,
                    self.arrow_rect.center[1],
                )

    def out_hover_effect(self):
        if self.arrow_rect.center[0] != self.position[0]:
            if self.direction == "right":
                self.arrow_rect.center = (
                    self.arrow_rect.center[0] - 1,
                    self.arrow_rect.center[1],
                )
            else:
                self.arrow_rect.center = (
                    self.arrow_rect.center[0] + 1,
                    self.arrow_rect.center[1],
                )
