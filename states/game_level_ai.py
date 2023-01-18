import pygame
from components.game_grid import GameGrid
from components.button import Button
from states.game_won import GameWon
from solver.do_search import do_search
from states.state import State
from level.level_state import LevelState
from components.button_cup import ButtonCup

class GameLevelAi(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.level = LevelState()
        self.game_level_screen = pygame.Surface((game.GAME_W, game.GAME_H))
        
        self.board_w, self.board_h = 1600, 400
        self.cup_size = self.board_h / 2
        self.y_offset, self.x_offset = (game.GAME_W-self.board_w)/2,(game.GAME_H-self.board_h)/2
        self.center = (game.GAME_W / 2, game.GAME_H / 2)
        
        self.game_grid = GameGrid(self.game, (self.board_w, self.board_h), self.level)
        
        self.reset_button = Button(
            game,
            "RESET","Medium",
            (self.center[0] - 550, self.center[1] + 370),
            self.handle_reset,
        )
        self.quit_button = Button(
            game, "QUIT", "Medium", (self.center[0] + 520, self.center[1] + 370), self.handle_quit
        )

        self.time_start = pygame.time.get_ticks()
        self.ai_time = pygame.time.get_ticks()

        self.turn = game.starting_player
        self.value = None

        self.initialize_cups()


    def update(self, actions):
        if self.gameOver():
            winner = self.findWinner()
            level_score = self.evaluate()
            print("WINNER")
            self.print_board()
            self.handle_win(winner, level_score)
        pass

    def render(self, display):
        self.game_level_screen.fill((0, 0, 0))
        if self.turn == 2:
            self.AI_turn()
        self.game_grid.draw(self.game_level_screen)
        self.draw_buttons()
        self.draw_stores()
        self.draw_time()
        self.draw_trun()
        self.reset_button.draw(self.game_level_screen)
        self.quit_button.draw(self.game_level_screen)
        display.blit(self.game_level_screen, (0, 0))
        pass

    def AI_turn(self):
        if pygame.time.get_ticks() - self.ai_time > 2000:
            self.ai_time = pygame.time.get_ticks()
            bestValue, bestCup = do_search(self)
            print(bestValue, bestCup)
            replay = self.level.doMove(self.turn,bestCup)
            self.initialize_cups()
            self.print_board()
            print("score:",self.evaluate())
            if not replay:
                self.turn = self.level.opposite_player(self.turn)
        

    def draw_time(self):
        time = (pygame.time.get_ticks() - self.time_start)//1000

        self.game.draw_text(
            self.game_level_screen,
            f"TIME {time}/{self.game.time_limit}s",
            "Small",
            (self.center[0] - 280, self.center[1] - 450),
        )
        if time > self.game.time_limit:
            self.turn = self.level.opposite_player(self.turn)
            self.time_start = pygame.time.get_ticks()

    def draw_trun(self):
        self.game.draw_text(
            self.game_level_screen,
            f"TURN: Player {self.turn}",
            "Small",
            (self.center[0] + 280, self.center[1] - 450),
        )

    def draw_buttons(self):
        for button in self.cups_buttons:
            button.draw(self.game_level_screen)
    
    def draw_stores(self):
        self.game.draw_text(
            self.game_level_screen,
            str(self.level.board['2']),
            "Very big",
            (self.y_offset + self.cup_size/2, self.x_offset + self.cup_size)
        )
        self.game.draw_text(
            self.game_level_screen,
            str(self.level.board['1']),
            "Very big",
            (self.y_offset + self.board_w - self.cup_size /2, self.x_offset + self.cup_size)
        )

    def handle_reset(self):
        level = LevelState()
        self.game_grid = GameGrid(self.game, (1600, 400), level)

    def handle_quit(self):
        self.exit_state()

    def handle_win(self, winner, level_score):
        new_state = GameWon(self.game, self, winner, level_score)
        new_state.enter_state()

    def initialize_cups(self):
        buttons = []
        for i in range(6):
            buttons.append(
                ButtonCup(
                    self.game, 
                    str(self.level.board[self.level.PlayerCups[1][i]]), 
                    "Very big", 
                    (self.y_offset + (i + 1.5) * self.cup_size, self.x_offset + self.board_h - self.cup_size / 2), 
                    self.level.doMove,
                    self.level.PlayerCups[1][i],
                    self, 1
                )
            )
        for i in range(6):
            buttons.append(
                ButtonCup(
                    self.game, 
                    str(self.level.board[self.level.PlayerCups[2][i]]), 
                    "Very big", 
                    (self.y_offset + (i + 1.5) * self.cup_size, self.x_offset + self.cup_size / 2), 
                    self.level.doMove,
                    self.level.PlayerCups[2][i],
                    self, 2
                )
            )
        self.cups_buttons = buttons
    
    def gameOver(self):
        emptyCups_P1, emptyCups_P2 = 0, 0
        for key in self.level.board:
            if key in self.level.PlayerCups[1] and self.level.board[key] == 0:
                emptyCups_P1 += 1
            if key in self.level.PlayerCups[2] and self.level.board[key] == 0:
                emptyCups_P2 += 1
        if emptyCups_P1 == 6:
            Nb_stones = 0
            for key in self.level.PlayerCups[2]:
                    Nb_stones += self.level.board[key]
            self.level.board['1'] += Nb_stones
            return True
        elif emptyCups_P2 == 6:
            Nb_stones = 0
            for key in self.level.PlayerCups[1]:
                    Nb_stones += self.level.board[key]
            self.level.board['2'] += Nb_stones
            return True
        return False
    
    def findWinner(self):
        if self.level.board['1'] > self.level.board['2']:
            return 1
        return 2
    
    def evaluate(self):
        self.value = self.level.board['1'] - self.level.board['2']
        return abs(self.value)


    def print_board(self):
        print(self.level.board['2'],"|",
        self.level.board['G'],
        self.level.board['H'],
        self.level.board['I'],
        self.level.board['J'],
        self.level.board['K'],
        self.level.board['L'],
        )
        print(
        self.level.board['A'],
        self.level.board['B'],
        self.level.board['C'],
        self.level.board['D'],
        self.level.board['E'],
        self.level.board['F'],"|",self.level.board['1']
        )
        
