     def __init__(self) -> None:
         self._load_config_files()
         pygame.init()
        pygame.display.set_caption(self.window_config["window"]["title"])
        sizes = tuple(self.window_config["window"]["size"].values())
        background_color = tuple(self.window_config["window"]["bg_color"].values())
         self.screen = pygame.display.set_mode(sizes, pygame.SCALED)
         self.clock = pygame.time.Clock()
         self.is_running = False
        self.framerate = self.window_config["window"]["framerate"]
         self.delta_time = 0
         self.bg_color = pygame.Color(background_color)
         self.laser_sound = generate_laser_beep()