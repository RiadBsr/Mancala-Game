import pygame
from states.game_level import GameLevel
from states.game_level_ai import GameLevelAi
from states.settings_menu import SettingsMenu
from states.state import State
from components.button import Button


class MainMenu(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.main_menu_screen = pygame.Surface((game.GAME_W, game.GAME_H))

        self.black_screen = pygame.Surface((game.GAME_W, game.GAME_H))
        self.black_screen.fill((0, 0, 0))
        self.black_screen.set_alpha(255)

        self.play_button = Button(
            game, "PLAY", "Big", (game.GAME_W / 2, game.GAME_H / 2), self.handle_play
        )
        self.settings_button = Button(
            game,
            "SETTINGS", "Big",
            (game.GAME_W / 2, game.GAME_H / 2 + 100),
            self.handle_settings,
        )
        self.exit_button = Button(
            game, "EXIT", "Big", (game.GAME_W / 2, game.GAME_H / 2 + 200), self.handle_exit
        )

    def update(self, actions):
        self.game.reset_keys()

    def render(self, display):
        self.main_menu_screen.fill((0, 0, 0))
        self.draw_menu_title(self.main_menu_screen)
        self.draw_menu_options(self.main_menu_screen)
        self.fade_in()
        display.blit(self.main_menu_screen, (0, 0))

    def draw_menu_title(self, display):
        self.game.draw_text(
            display, "MAIN MENU", "Very big", (self.game.GAME_W / 2, self.game.GAME_H / 3.5)
        )

    def draw_menu_options(self, display):
        self.play_button.draw(display)
        self.settings_button.draw(display)
        self.exit_button.draw(display)
        pass

    def fade_in(self):
        if self.black_screen.get_alpha() != 0:
            self.black_screen.set_alpha(self.black_screen.get_alpha() - 4)
            self.main_menu_screen.blit(self.black_screen, (0, 0))

    def handle_play(self):
        if self.game.game_mode: 
            new_state = GameLevelAi(self.game)
        else :
            new_state = GameLevel(self.game)
        new_state.enter_state()

    def handle_settings(self):
        new_state = SettingsMenu(self.game)
        new_state.enter_state()

    def handle_exit(self):
        self.game.running = False
        self.game.playing = False
