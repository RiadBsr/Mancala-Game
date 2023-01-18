import pygame
from components.button import Button
from states.state import State


class SettingsMenu(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.settings_menu_surface = pygame.Surface((game.GAME_W, game.GAME_H))

        self.title_position = (game.GAME_W / 2, game.GAME_H / 4 - 50)
        self.options_position = (game.GAME_W / 2, game.GAME_H / 2 - 150)
        
        self.game_mode = {True: "Against AI", False: "Two Players"}
        self.game_mode_button = Button(game, f"GAME MODE: {self.game_mode[game.game_mode]}", "Medium", (self.options_position[0], self.options_position[1] ), self.game_mode_handler)
        self.starting_player_button = Button(game, f"STARTING PLAYER: Player {game.starting_player}", "Medium", (self.options_position[0], self.options_position[1] + 100), self.starting_player_handler)
        self.back_button = Button(game, "BACK", "Medium", (self.options_position[0], self.options_position[1] + 500), self.back_handler)
        
        self.increase_time_button = Button(game, "+","Medium",(self.options_position[0]+200, self.options_position[1]+ 200), self.increase_time_handler)
        self.decrease_time_button = Button(game, "-","Medium",(self.options_position[0]-200, self.options_position[1]+ 200), self.decrease_time_handler)

        self.increase_depth_button = Button(game, "+","Medium",(self.options_position[0]+200, self.options_position[1]+ 400), self.increase_depth_handler)
        self.decrease_depth_button = Button(game, "-","Medium",(self.options_position[0]-200, self.options_position[1]+ 400), self.decrease_depth_handler)

        type = "Custom"
        if self.game.automatic_depth:
            type = "Auto"
        self.depthType_button = Button(game, f"Search Depth : {type}","Medium",(self.options_position[0], self.options_position[1] + 300), self.auto_depth_handler)

    def update(self, actions):
        pass

    def render(self, display):
        self.settings_menu_surface.fill((0,0,0))
        self.draw_title()
        self.draw_options()
        display.blit(self.settings_menu_surface, (0, 0))

    def draw_title(self):
        self.game.draw_text(self.settings_menu_surface, "SETTINGS", "Big", self.title_position)

    def draw_options(self):
        self.game_mode_button.draw(self.settings_menu_surface)
        self.starting_player_button.draw(self.settings_menu_surface)
        self.back_button.draw(self.settings_menu_surface)
        self.depthType_button.draw(self.settings_menu_surface)

        self.game.draw_text(self.settings_menu_surface, "TIME: "+str(self.game.time_limit)+'s', "Medium", (self.options_position[0], self.options_position[1]+200))
        self.increase_time_button.draw(self.settings_menu_surface)
        self.decrease_time_button.draw(self.settings_menu_surface)
        
        self.game.draw_text(self.settings_menu_surface, "DEPTH: "+str(self.game.search_depth), "Medium", (self.options_position[0], self.options_position[1]+400))
        
        if not self.game.automatic_depth:
            self.increase_depth_button.draw(self.settings_menu_surface)
            self.decrease_depth_button.draw(self.settings_menu_surface)

    def game_mode_handler(self):
        self.game.game_mode = not self.game.game_mode
        
        self.game_mode_button = Button(
            self.game, 
            f"GAME MODE: {self.game_mode[self.game.game_mode]}", 
            "Medium", 
            (self.options_position[0], self.options_position[1]), 
            self.game_mode_handler
        )

    def starting_player_handler(self):
        if self.game.starting_player == 1:
            self.game.starting_player = 2
        else:
            self.game.starting_player = 1
        
        self.starting_player_button = Button(
            self.game, 
            f"STARTING PLAYER: Player {self.game.starting_player}",
            "Medium", 
            (self.options_position[0], self.options_position[1] + 100), 
            self.starting_player_handler
        )

    def increase_depth_handler(self):
        if self.game.search_depth < 15:
            self.game.search_depth += 1
    
    def decrease_depth_handler(self):
        if self.game.search_depth > 2:
            self.game.search_depth -= 1

    def increase_time_handler(self):
        if self.game.time_limit < 120:
            self.game.time_limit += 5
        if self.game.automatic_depth:
            self.game.search_depth = (self.game.time_limit - 10) // 10 + 2
    
    def decrease_time_handler(self):
        if self.game.time_limit > 10:
            self.game.time_limit -= 5
        if self.game.automatic_depth:
            self.game.search_depth = (self.game.time_limit - 10) // 10 + 2
    
    def auto_depth_handler(self):
        self.game.automatic_depth = not self.game.automatic_depth
        if self.game.automatic_depth:
            self.game.search_depth = (self.game.time_limit - 10) // 10 + 2
        type = "Custom"
        if self.game.automatic_depth:
            type = "Auto"
        self.depthType_button = Button(self.game, f"Search Depth : {type}","Medium",(self.options_position[0], self.options_position[1] + 300), self.auto_depth_handler)

    def back_handler(self):
        self.exit_state()
