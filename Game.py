import pygame
from pygame import mixer
import Game_Menu

mixer.init()
import World_2 as level

pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sounds/bgmusic.mpeg"), -1)
mixer.Channel(1).set_volume(0.2)

SCREEN_WIDTH = 1026
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# loading images
PLAYER_1_IMG = pygame.transform.scale(pygame.image.load("Images/Player_1_2.png"), (96, 112))
PLAYER_2_IMG = pygame.transform.scale(pygame.image.load("Images/Player_2_2.png"), (96, 112))
BULLET_img = pygame.transform.scale(pygame.transform.rotate(pygame.image.load("Images/bullet.png"), 270), (10, 10))

# Defining all the varibles
FPS = 60
PLAYER_1_X = 300
PLAYER_1_Y = 10
PLAYER_2_X = 800
PLAYER_2_Y = 10
PLAYER_SPEED = 5
GRAVITY = 10
HOLD_1 = False
HOLD_2 = False
JUMP_1 = False
JUMP_2 = False
JUMP_VELOCITY_1 = 10
JUMP_VELOCITY_2 = 10
BULLET_1_X = PLAYER_1_X
BULLET_1_Y = PLAYER_1_Y
BULLET_2_X = PLAYER_2_X
BULLET_2_Y = PLAYER_2_Y
BULLET_1_rect = pygame.Rect(0, 0, 0, 0)
BULLET_2_rect = pygame.Rect(0, 0, 0, 0)
SHOOT_1 = False
SHOOT_2 = False
RIGHT_1 = True
RIGHT_2 = False
LEFT_1 = False
LEFT_2 = True
KNOCK_1 = 7
KNOCK_2 = 7
HIT_1 = False
HIT_2 = False
STOP_1 = False
STOP_2 = False
var_1 = False
var_2 = False
say = "Start Game"


class Player:
    def __init__(self, xcord, ycord, img):
        self.x = xcord
        self.y = ycord
        self.img = img

    def draw(self):

        if self == PLAYER_1:
            if LEFT_1:
                img_1 = pygame.transform.flip(self.img, True, False)
                SCREEN.blit(img_1, (self.x, self.y))

            elif RIGHT_1:
                SCREEN.blit(self.img, (self.x, self.y))

        elif self == PLAYER_2:
            if LEFT_2:
                img_1 = pygame.transform.flip(self.img, True, False)
                SCREEN.blit(img_1, (self.x, self.y))

            elif RIGHT_2:
                SCREEN.blit(self.img, (self.x, self.y))

    def move(self):
        global GRAVITY, HOLD_1, HOLD_2, JUMP_1, JUMP_2, RIGHT_1, RIGHT_2, LEFT_1, LEFT_2, TURN_1, TURN_2

        key_press = pygame.key.get_pressed()
        if self == PLAYER_1:
            # key press for movement control
            if key_press[pygame.K_d]:
                self.x += PLAYER_SPEED
                if not SHOOT_1:
                    RIGHT_1 = True
                    LEFT_1 = False
            elif key_press[pygame.K_a]:
                if not SHOOT_1:
                    LEFT_1 = True
                    RIGHT_1 = False
                self.x -= PLAYER_SPEED
        elif self == PLAYER_2:
            if key_press[pygame.K_RIGHT]:
                if not SHOOT_2:
                    LEFT_2 = False
                    RIGHT_2 = True
                self.x += PLAYER_SPEED
            elif key_press[pygame.K_LEFT]:
                if not SHOOT_2:
                    RIGHT_2 = False
                    LEFT_2 = True
                self.x -= PLAYER_SPEED

        # Standing on the platforms
        PLAYER_FEET_rect = pygame.Rect(self.x + 40, self.y + 115, self.img.get_width() - 85,
                                       self.img.get_height() - 130)
        PLAYER_FEET_1_rect = pygame.Rect(PLAYER_1.x + 25, PLAYER_1.y + 115, PLAYER_1_IMG.get_width() - 70,
                                         PLAYER_1_IMG.get_height() - 130)
        PLAYER_FEET_2_rect = pygame.Rect(PLAYER_2.x + 25, PLAYER_2.y + 115, PLAYER_2_IMG.get_width() - 70,
                                         PLAYER_2_IMG.get_height() - 130)
        pygame.draw.rect(SCREEN, "red", PLAYER_FEET_1_rect, 5)
        pygame.draw.rect(SCREEN, "red", PLAYER_FEET_2_rect, 5)

        HOLD_1 = False
        HOLD_2 = False

        for rect in level.WORLD.rect_list:

            if pygame.Rect.colliderect(PLAYER_FEET_1_rect, rect):
                HOLD_1 = True
                GRAVITY = 10
            if pygame.Rect.colliderect(PLAYER_FEET_2_rect, rect):
                HOLD_2 = True
                GRAVITY = 10

        if not (pygame.Rect.colliderect(PLAYER_FEET_rect, level.WORLD.rect_list[len(level.WORLD.rect_list)-1]) or pygame.Rect.colliderect(
                PLAYER_FEET_rect, level.WORLD.rect_list[len(level.WORLD.rect_list)-2])):
            if key_press[pygame.K_s]:
                HOLD_1 = False
            if key_press[pygame.K_DOWN]:
                HOLD_2 = False

        if not HOLD_1 and not JUMP_1:
            if self == PLAYER_1:
                self.y += GRAVITY
                GRAVITY += 0.5
        if not HOLD_2 and not JUMP_2:
            if self == PLAYER_2:
                self.y += GRAVITY
                GRAVITY += 0.5

    def jump(self):
        global JUMP_1, JUMP_2, JUMP_VELOCITY_1, JUMP_VELOCITY_2, HOLD_1, HOLD_2
        key_press = pygame.key.get_pressed()
        if self == PLAYER_1:
            if key_press[pygame.K_w]:
                if HOLD_1:
                    HOLD_1 = False
                    JUMP_1 = True
        else:
            if key_press[pygame.K_UP]:
                if HOLD_2:
                    HOLD_2 = False
                    JUMP_2 = True

        if self == PLAYER_1 and JUMP_1:
            self.y -= JUMP_VELOCITY_1
            JUMP_VELOCITY_1 -= 0.5
            if JUMP_VELOCITY_1 <= -10 or HOLD_1 and JUMP_VELOCITY_1 < 0:
                JUMP_1 = False
                JUMP_VELOCITY_1 = 10
        if self == PLAYER_2 and JUMP_2:
            self.y -= JUMP_VELOCITY_2
            JUMP_VELOCITY_2 -= 0.5
            if JUMP_VELOCITY_2 <= -10 or HOLD_2 and JUMP_VELOCITY_2 < 0:
                JUMP_2 = False
                JUMP_VELOCITY_2 = 10

    def bullet(self, velocity):
        global SHOOT_1, SHOOT_2, BULLET_1_Y, BULLET_1_X, BULLET_2_Y, BULLET_2_X, BULLET_1_rect, BULLET_2_rect, RIGHT_2, LEFT_1, STOP_1, STOP_2

        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_z]:
            if self == PLAYER_1:
                if not SHOOT_1:
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound("Sounds/Gun_Shot.mp3"))
                    mixer.Channel(0).set_volume(0.4)
                    BULLET_1_Y = self.y
                    BULLET_1_X = self.x
                    SHOOT_1 = True
        if key_press[pygame.K_m]:
            if self == PLAYER_2:
                if not SHOOT_2:
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound("Sounds/Gun_Shot.mp3"))
                    mixer.Channel(0).set_volume(0.4)
                    BULLET_2_X = self.x
                    BULLET_2_Y = self.y
                    SHOOT_2 = True

        if SHOOT_1:

            if LEFT_1:
                BULLET_1_X -= velocity
            elif RIGHT_1:
                BULLET_1_X += velocity

            BULLET_1_rect = pygame.Rect(BULLET_1_X + 36, BULLET_1_Y + 52, BULLET_img.get_width(),
                                        BULLET_img.get_height() - 7)
            SCREEN.blit(BULLET_img, (BULLET_1_X + 40, BULLET_1_Y + 50))
            if BULLET_1_X > 1040 or BULLET_1_X < -10 or STOP_2:
                STOP_2 = False
                SHOOT_1 = False
                BULLET_1_rect = pygame.Rect(BULLET_1_X + 36, BULLET_1_Y + 52, 0, 0)

        if SHOOT_2:

            if RIGHT_2:
                BULLET_2_X += velocity
            else:
                BULLET_2_X -= velocity

            BULLET_2_rect = pygame.Rect(BULLET_2_X + 36, BULLET_2_Y + 52, BULLET_img.get_width(),
                                        BULLET_img.get_height() - 7)
            SCREEN.blit(BULLET_img, (BULLET_2_X + 40, BULLET_2_Y + 50))
            if BULLET_2_X + 40 <= -10 or BULLET_2_X >= 1040 or STOP_1:
                STOP_1 = False
                SHOOT_2 = False
                BULLET_2_rect = pygame.Rect(BULLET_2_X + 36, BULLET_2_Y + 52, 0, 0)

    def knockback(self):
        global KNOCK_1, KNOCK_2, HIT_1, HIT_2

        if self == PLAYER_1:
            if STOP_1:
                KNOCK_1 = 7
            if var_1:
                self.x -= KNOCK_1
                KNOCK_1 -= 0.1
                if KNOCK_1 <= 0:
                    KNOCK_1 = 7
                    HIT_1 = False
            elif not var_1:
                self.x += KNOCK_1
                KNOCK_1 -= 0.1
                if KNOCK_1 <= 0:
                    KNOCK_1 = 7
                    HIT_1 = False

        if self == PLAYER_2:
            if STOP_2:
                KNOCK_2 = 7
            if var_2:
                self.x -= KNOCK_2
                KNOCK_2 -= 0.1
                if KNOCK_2 <= 0:
                    KNOCK_2 = 7
                    HIT_2 = False
            elif not var_2:
                self.x += KNOCK_2
                KNOCK_2 -= 0.1
                if KNOCK_2 <= 0:
                    KNOCK_2 = 7
                    HIT_2 = False

    def hit(self):
        global HIT_1, HIT_2, STOP_1, STOP_2, var_1, var_2

        player_rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

        # pygame.draw.rect(SCREEN, "red", BULLET_1_rect, 5)
        # pygame.draw.rect(SCREEN, "red", BULLET_2_rect, 5)
        # pygame.draw.rect(SCREEN, "red", player_rect, 5)

        if self == PLAYER_1:
            if pygame.Rect.colliderect(player_rect, BULLET_2_rect):
                HIT_1 = True
                STOP_1 = True
                var_1 = LEFT_2
        elif self == PLAYER_2:
            if pygame.Rect.colliderect(player_rect, BULLET_1_rect):
                HIT_2 = True
                STOP_2 = True
                var_2 = LEFT_1


PLAYER_1 = Player(PLAYER_1_X, PLAYER_1_Y, PLAYER_1_IMG)
PLAYER_2 = Player(PLAYER_2_X, PLAYER_2_Y, PLAYER_2_IMG)


def game_over():
    global say
    if PLAYER_1.y >= SCREEN_WIDTH + 112:
        print("Game Over \nPlayer 2(RED) won the Game")
        say = "Play Again"
        Game_Menu.menu()
    elif PLAYER_2.y >= SCREEN_WIDTH + 112:
        print("Game Over \nPlayer 1(AQUA) won the Game")
        say = "Play Again"
        Game_Menu.menu()


def main():
    clock = pygame.time.Clock()
    PLAYER_1.x = 300
    PLAYER_1.y = 10
    PLAYER_2.x = 300
    PLAYER_2.y = 10
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Drawing stuff on the screen
        SCREEN.blit(level.WORLD.img, (0, 0))
        PLAYER_1.draw()
        PLAYER_2.draw()

        # Player movement and its standing on platforms
        PLAYER_1.move()
        PLAYER_2.move()

        # JUmping of player
        PLAYER_1.jump()
        PLAYER_2.jump()

        # bullet shooting
        PLAYER_1.bullet(20)
        PLAYER_2.bullet(20)

        # Check hit with the bullet
        PLAYER_1.hit()
        PLAYER_2.hit()

        # Knockback after getting hit
        if HIT_1:
            PLAYER_1.knockback()
        if HIT_2:
            PLAYER_2.knockback()

        # Check for winner and game over
        game_over()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
