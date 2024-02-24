import pygame

SCREEN_WIDTH = 1026
SCREEN_HEIGHT = 600

class World:

    def __init__(self):
        # creating the rectangles
        self.img = pygame.transform.scale(pygame.image.load("Images/BG.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect_top_plank = pygame.Rect(260, 198, 520, 10)
        self.rect_mid_block_1 = pygame.Rect(260, 270, 120, 10)
        self.rect_mid_block_2 = pygame.Rect(640, 270, 120, 10)
        self.rect_mid_plank = pygame.Rect(97, 350, 850, 10)
        self.rect_low_plank = pygame.Rect(361, 440, 300, 10)
        self.rect_low_block_1 = pygame.Rect(65, 520, 346, 10)
        self.rect_low_block_2 = pygame.Rect(610, 520, 370, 10)

        self.rect_list = [
            self.rect_top_plank, self.rect_mid_block_1,
            self.rect_mid_block_2, self.rect_mid_plank,
            self.rect_low_plank, self.rect_low_block_1,
            self.rect_low_block_2
        ]


WORLD = World()
