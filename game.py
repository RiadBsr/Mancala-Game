import os, pygame

from states.splash import Splash

class Game:
    def __init__(self):
        pygame.init()

        # Settings
        self.starting_player = 1
        self.game_mode = False # True: Against AI, False: Two Players
        self.automatic_depth = False # set automaticaly the depth based on the time limit
        self.time_limit = 30 # seconds
        self.search_depth = (self.time_limit - 10) // 10 + 2 # AI
        self.search_algorithm = 1 # 1: Minimax, 2: Negamax

        self.GAME_W, self.GAME_H = 1920, 1080
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))

        self.screen = pygame.display.set_mode(
            (0, 0), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN, 8
        )
        self.SCREEN_W, self.SCREEN_H = pygame.display.get_surface().get_size()

        self.actions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False,
            "enter": False,
            "escape": False,
            "event_1" : False
        }

        self.state_stack = []

        self.load_assets()
        self.load_states()

        self.running, self.playing = True, True

    def game_loop(self):
        while self.playing:
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.state_stack[-1].update(self.actions)

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(
            pygame.transform.scale(self.game_canvas, (self.SCREEN_W, self.SCREEN_H)),
            (0, 0),
        )
        pygame.display.flip()

    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.very_big_font = pygame.font.Font(os.path.join(self.font_dir, "Inter.ttf"), 100)
        self.big_font = pygame.font.Font(os.path.join(self.font_dir, "Inter.ttf"), 64)
        self.medium_font = pygame.font.Font(os.path.join(self.font_dir, "Inter.ttf"), 48)
        self.small_font = pygame.font.Font(os.path.join(self.font_dir, "Inter.ttf"), 32)
        self.very_small_font = pygame.font.Font(os.path.join(self.font_dir, "Inter.ttf"), 24)

    def load_states(self):
        self.splash_screen = Splash(self)
        self.state_stack.append(self.splash_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def draw_text(self, surface, text, size, position, color=(255, 255, 255)):
        match size:
            case "Very big":
                text_surface = self.very_big_font.render(text, True, color)
            case "Big":
                text_surface = self.big_font.render(text, True, color)
            case "Medium":
                text_surface = self.medium_font.render(text, True, color)
            case "Small":
                text_surface = self.small_font.render(text, True, color)
            case "Very small":
                text_surface = self.very_small_font.render(text, True, color)

        text_rect = text_surface.get_rect()
        text_rect.center = position
        surface.blit(text_surface, text_rect)


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()
