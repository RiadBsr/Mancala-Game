import pygame
from states.state import State
from states.main_menu import MainMenu

class Splash(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.splash_screen = pygame.Surface((game.GAME_W, game.GAME_H))

        self.black_screen = pygame.Surface((game.GAME_W, game.GAME_H))
        self.black_screen.set_alpha(0)

        self.timer = pygame.time.get_ticks()
        self.clock = pygame.time.Clock()

    def update(self, actions):
        if pygame.time.get_ticks() - self.timer > 2000:
            new_state = MainMenu(self.game)
            new_state.enter_state()

        self.clock.tick(60)

        self.game.reset_keys()

    def render(self, display):
        self.splash_screen.fill((0, 0, 0))
        self.draw_splash(self.splash_screen)
        self.fade_out()
        display.blit(self.splash_screen, (0, 0))

    def draw_splash(self, display):
        self.game.draw_text(
            display, "MANCALA", "Very big", (self.game.GAME_W / 2, self.game.GAME_H / 2)
        )

    def fade_out(self):
        self.splash_screen.blit(self.black_screen, (0, 0))
        if pygame.time.get_ticks() - self.timer > 1000:
            self.black_screen.set_alpha(self.black_screen.get_alpha() + 5)
