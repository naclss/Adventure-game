import pygame as pg

pg.init()
pg.display.set_caption("Бродилка")

class Game:
    def __init__(self):
        self.WIDTH = 1089
        self.HEIGHT = 738
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))

        self.back_image_1 = pg.image.load('фон1.png')
        self.back_rect_1 = self.back_image_1.get_rect()
        self.back_image_2 = pg.image.load('фон2.png')
        self.back_rect_2 = self.back_image_2.get_rect()

        self.char_image = pg.image.load('персонаж.png')
        self.char_image = pg.transform.scale(self.char_image, (100, 100))
        self.char_rect = self.char_image.get_rect()
        self.left_image = pg.transform.flip(self.char_image.copy(), 1, 0)
        self.right_image = self.char_image.copy()
        self.speed = 1

        self.health_image = pg.image.load('хп.png')
        self.health_image = pg.transform.scale(self.health_image, (50, 50))
        self.health_rect = self.health_image.get_rect()
        self.health = 3
        self.health = 3

        self.lose_image = pg.image.load('проигрыш.jpg')
        self.lose_image = pg.transform.scale(self.lose_image, (1089, 738))
        self.lose_rect = self.lose_image.get_rect()

    def check_move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.char_rect.top > 0:
            self.char_rect.y -= self.speed
        if keys[pg.K_s] and self.char_rect.bottom < self.HEIGHT:
            self.char_rect.y += self.speed
        if keys[pg.K_a] and self.char_rect.left > 0:
            self.char_image = self.left_image
            self.char_rect.x -= self.speed
        if keys[pg.K_d] and self.char_rect.right < self.WIDTH:
            self.char_image = self.right_image
            self.char_rect.x += self.speed

        if self.health == 0:
            self.screen.blit(self.lose_image, self.lose_rect)
            return False

        return True


    def draw(self):
        self.screen.blit(self.back_image_1, self.back_rect_1)
        self.screen.blit(self.char_image, self.char_rect)
        for i in range(self.health):
            self.health_rect.x = 10 + i * (self.health_image.get_width() + 5)
            self.health_rect.y = self.HEIGHT - self.health_image.get_height() - 10
            self.screen.blit(self.health_image, self.health_rect)

    def update(self):
        self.check_move()
        pg.display.flip()
        pg.time.Clock().tick(165)

    def running(self):
        running = True
        while running:
            running = self.check_move()
            self.draw()
            self.update()

pg.quit()

if __name__ == '__main__':
    k = Game()
    k.running()