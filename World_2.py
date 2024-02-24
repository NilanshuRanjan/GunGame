import pygame

SCREEN_WIDTH = 1026
SCREEN_HEIGHT = 600
#
# SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class World:

    def __init__(self):
        # creating the rectangles
        self.img = pygame.transform.scale(pygame.image.load("Images/Midnight_Wood_Map.webp"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect_top_plank = pygame.Rect(220, 120, 620, 4)
        self.rect_mid_block_1 = pygame.Rect(172, 217, 205, 4)
        self.rect_mid_block_2 = pygame.Rect(685, 213, 205, 4)
        self.rect_mid_block_3 = pygame.Rect(122, 305, 205, 4)
        self.rect_mid_block_4 = pygame.Rect(685, 213, 205, 4)
        self.rect_mid_block_5 = pygame.Rect(433, 303, 205, 4)
        self.rect_mid_block_6 = pygame.Rect(738, 306, 205, 4)
        self.rect_mid_block_7 = pygame.Rect(67, 397, 210, 4)
        self.rect_mid_block_8 = pygame.Rect(786, 396, 210, 4)
        self.rect_low_block_1 = pygame.Rect(223, 488, 346, 4)
        self.rect_low_block_2 = pygame.Rect(560, 488, 280, 4)

        self.rect_list = [
            self.rect_mid_block_3, self.rect_mid_block_4,
            self.rect_mid_block_5, self.rect_mid_block_6,
            self.rect_top_plank, self.rect_mid_block_1,
            self.rect_mid_block_2, self.rect_mid_block_7,
            self.rect_mid_block_8, self.rect_low_block_1,
            self.rect_low_block_2
        ]
    #
    # def draw(self):
    #
    #     for rect in self.rect_list:
    #         pygame.draw.rect(SCREEN, "red", rect, 5)


WORLD = World()

# run = True
# while run:
#
#     SCREEN.blit(WORLD.img, (0, 0))
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     WORLD.draw()
#     pygame.display.update()
#
# pygame.quit()
