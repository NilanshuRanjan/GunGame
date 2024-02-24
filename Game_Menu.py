import pygame
import Game
pygame.font.init()

def menu():
    from Game import say

    screen = pygame.display.set_mode((1026, 600))
    print(say)

    font = pygame.font.Font("Font.ttf", 49)
    bg = pygame.transform.scale(pygame.image.load("Images/Menu_BG_1.jpg"), (1026, 600))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(bg, (0, 0))
        start = font.render(say, True, "Chartreuse2")
        quit = font.render("Quit", True, "Chartreuse2")
        screen.blit(start, (280, 100))
        screen.blit(quit, (280, 200))

        rect1 = pygame.Rect(280, 100, start.get_width(), start.get_height())
        rect2 = pygame.Rect(280, 200, quit.get_width(), quit.get_height())

        # pygame.draw.rect(screen, "blue", rect1, 5)
        # pygame.draw.rect(screen, "blue", rect2, 5)

        if pygame.Rect.collidepoint(rect1, pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                Game.main()
        if pygame.Rect.collidepoint(rect2, pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                pygame.quit()

        pygame.display.update()

if __name__ == '__main__':
    menu()

