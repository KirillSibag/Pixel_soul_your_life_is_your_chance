import pygame
import time

screen_h = 540
screen_w = 1140

class player():#класс игрока
    def __init__(self, img_adress = 'imgs/player/player_0.png'):
        self.img_adress = img_adress
        self.img_loading()

        self.image_x = screen_w // 2   #положение по горизонтали
        self.image_y = screen_h // 3   #положение по вертикали

        self.speed = screen_w // 1140 * 3
        self.img_pos = 0
        self.timer = time.time()

    def img_loading(self):
        self.image = pygame.transform.scale(pygame.image.load(self.img_adress), (screen_w // 15, screen_h // 4))  # оригинальное изображение
        image_flip = self.image
        self.image_flip = pygame.transform.flip(image_flip, True, False)  # отражённое изображение
        self.image_show = self.image

    def move(self, horisontal, vertical):
        #изменение положения игрока
        self.image_x += horisontal * self.speed
        self.image_y += vertical * self.speed

        if time.time() - self.timer > 0.15:
            self.timer = time.time()
            self.img_pos += 1

            if self.img_pos > 4:
                self.img_pos = 0

            self.img_adress = f'imgs/player/player_{self.img_pos}.png'
            self.img_loading()





types = {"mushroom": {"adress" : "imgs/objs/mushroom.png","nutrition": 3,"poison": 0,"tyagely": 0}, "bottle" : {"adress" : "imgs/objs/bottle.png","nutrition": 3,"poison": 0,"tyagely": 0}}
class object():#класс объектов, к которым применимы операции выпадения, получения и преобразования
    def __init__(self, type, x, y):
        self.nutrition = types[type]["nutrition"]
        self.poison = types[type]["poison"]
        self.tyagely = types[type]["tyagely"]
        self.x = x
        self.y = y

        self.image = pygame.image.load(types[type]["adress"])  # оригинальное изображение
        self.image_show = self.image


pygame.init()
screen = pygame.display.set_mode((screen_w, screen_h))
done = False

clock = pygame.time.Clock()

player = player()


objs = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #определение нажатых клавиш
    pressed = pygame.key.get_pressed()

    #определение направления движения
    horisontal = pressed[pygame.K_d] - pressed[pygame.K_a]
    vertical =  - pressed[pygame.K_w] + pressed[pygame.K_s]

    if pressed[pygame.K_t]:
        objs.append(object("mushroom", player.image_x, player.image_y))

    if pressed[pygame.K_y]:
        objs.append(object("bottle", player.image_x+10, player.image_y+10))

    player.move(horisontal, vertical)#изменение положения игрока

    #поворот игрока в случае необходимости
    if horisontal < 0:
        player.image_show = player.image_flip
    elif horisontal > 0:
        player.image_show = player.image


    #создание фона
    screen.fill((255, 255, 255))

    #отображение игрока
    screen.blit(player.image_show, (player.image_x, player.image_y))
    for piece in objs:
        screen.blit(piece.image_show, (piece.x, piece.y))


    pygame.display.flip()
    clock.tick(60)