import random
import pygame


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/cloud.png")
        self.rect = self.image.get_rect()

        self.surface = pygame.display.get_surface()
        rand_height = random.randint(0, self.surface.get_height() / 2)
        self.rect.midleft = (self.surface.get_width(), rand_height)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= 5

        if self.rect.right < 0:
            self.kill()