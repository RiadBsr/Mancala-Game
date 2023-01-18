from states.state import State
from components.button import Button
import pygame


class GameWon(State):
    def __init__(self, game, game_level, winner, level_score):
        State.__init__(self, game)
        self.game_level = game_level
        self.winner = winner
        self.level_score = level_score
        self.game_won_screen = pygame.Surface((game.GAME_W, game.GAME_H))
        self.game_won_rect = self.game_won_screen.get_rect(
            center=(game.GAME_W / 2, game.GAME_H / 2)
        )

        self.background_rect = pygame.Rect(710, 340, 700, 400)

        self.continue_button = Button(
            game, "CONTINUE", "Medium", (self.game.GAME_W / 2, self.game.GAME_H / 5 + 500), self.handle_continue
        )

        self.time = (pygame.time.get_ticks() - game_level.time_start)//1000
    def update(self, actions):
        pass

    def render(self, display):
        self.game_won_screen.fill((0, 0, 0))
        self.draw_title()
        self.continue_button.draw(self.game_won_screen)
        self.draw_winner()
        self.draw_score()
        display.blit(self.game_won_screen, self.game_won_rect)

    def draw_title(self):
        self.game.draw_text(
            self.game_won_screen,
            "GAME OVER",
            "Very big",
            (self.game.GAME_W / 2, self.game.GAME_H / 5),
        )

    def draw_winner(self):
        self.game.draw_text(
            self.game_won_screen,
            f"WINNER:  Player {self.winner}",
            "Big",
            (self.game.GAME_W / 2, self.game.GAME_H / 5 + 100),
        )
    
    def draw_score(self):
        self.game.draw_text(
            self.game_won_screen,
            f"StoreP1: {self.game_level.level.board['1']} | StoreP2: {self.game_level.level.board['2']}",
            "Medium",
            (self.game.GAME_W / 2, self.game.GAME_H / 5 + 250),
        )
        self.game.draw_text(
            self.game_won_screen,
            f"SCORE:  {self.level_score}",
            "Medium",
            (self.game.GAME_W / 2, self.game.GAME_H / 5 + 350),
        )


    def handle_continue(self):
        self.game.state_stack.pop()
        self.game.state_stack.pop()
