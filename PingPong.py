from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, spd=10, x=400, y=200, w=65, h=65):
        super().__init__()
        self.image = transform.scale(image.load(img), (win_width, win_height))
        self.rect = self.image.get_rect()
        self.spd = spd
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image ,(self.rect.x, self.rect.y))

class Racket(GameSprite):
        def move(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_UP] and self.rect.y > 0:
                self.rect.x -= self.spd
            if keys_pressed[K_DOWN] and self.rect.y < win_height-125:
                self.rect.x += self.spd
        def move(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_w] and self.rect.y > 0:
                self.rect.x -= self.spd
            if keys_pressed[K_s] and self.rect.y < win_height-125:
                self.rect.x += self.spd

class Ball(GameSprite):
    def move(self):
        pass

win_width = 800
win_height = 400

win = display.set_mode((win_width, win_height))
display.set_caption('PingPong')

bg



mixer.init()
mixer.music.load('SIS.wav')
mixer.music.play()
hit_sound = mixer.Sound('sus.wav')


Ball = Ball("Ping.png", 10, 35, 20, 65, 65)
racket1 = Racket('Pong.png', 10, 25, 140, 25, 125)
racket2 = Racket('Pong.png', 10, 25, 140, 25, 125)


FPS = 60
clock = time.Clock()
game = True
stop = False

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False


    ball.draw()
    racket1.draw()
    racket1.move1()
    racket2.draw()
    racket2.move2()

    display.update()
    clock.tick(FPS)