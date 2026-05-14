import pygame

# размер окна
width = 800
height = 600

clet = 30
fps = 50

# статус игры
s_menu = 0
s_play = 1
s_pause = 2
s_go = 3

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Labirint")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 25)
        self.state = s_menu
        self.maze = None
        self.player = None
        self.enemy = None
        self.small_font = pygame.font.Font(None, 15)
        self.difficulty = 1

    def start(self):
        while True:
            self.on_key()
            if self.state == s_play:
                self.tick()
            self.draw()
            pygame.display.flip()
            self.clock.tick(fps)

    def new(self):
        self.state = s_play
        print("New game", self.difficulty)
        self.maze = Maze(11, 11)
        self.maze.make()

    def on_key(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_1:
                    self.difficulty = 0
                    self.new()
                if event.key == pygame.K_2:
                    self.difficulty = 1
                    self.new()
                if event.key == pygame.K_3:
                    self.difficulty = 2
                    self.new()

    def tick(self):
        pass

    def draw(self):
        self.screen.fill(black)
        if self.state == s_menu:
            text = self.font.render("Menu: play 1 2 3", True, white)
            self.screen.blit(text, (30, 30))
        elif self.state == s_play:
            text = self.font.render("Play go", True, white)
            self.screen.blit(text, (30, 30))

            for y in range(self.maze.height):
                for x in range(self.maze.width):
                    c = self.maze.pole[y][x]
                    if c == stena:
                        pygame.draw.rect(self.screen, black, (x * clet, y * clet, clet, clet))
                    elif c == doroga:
                        pygame.draw.rect(self.screen, green, (x * clet, y * clet, clet, clet))


        elif self.state == s_pause:
            text = self.font.render("Pause", True, white)
            self.screen.blit(text, (30, 30))
        elif self.state == s_go:
            text = self.font.render("GAME OVER", True, red)
            self.screen.blit(text, (30, 30))