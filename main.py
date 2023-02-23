import sys

import pygame
from sprites.road import Road
from sprites.cloud import Cloud
from sprites.dino import Dino
from sprites.obstacles import Cactus
from sprites.game import Score, Game

WIDTH = 700
HEIGHT = 500
FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Dino")
clock = pygame.time.Clock()


def main():
    road = Road()
    clouds = pygame.sprite.Group()
    player = Dino()
    obstacles = pygame.sprite.Group()
    score = Score()
    running = True

    while running:
        # Частота обновления экрана/Screen refresh rate
        clock.tick(FPS)

        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for obstacle in obstacles:
            if pygame.sprite.collide_mask(player, obstacle):
                player.sound_die.play()
                game = Game()
                game.over(main)

        # Рендеринг/Rendering
        screen.fill((255, 255, 255))
        road.draw(screen)
        clouds.draw(screen)
        player.draw(screen)
        obstacles.draw(screen)
        score.draw(screen)

        # Обновление спрайтов/Updating sprites
        road.update()
        clouds.update()
        obstacles.update()
        if len(clouds) < 3:
            cloud = Cloud()
            clouds.add(cloud)
        if len(obstacles) < 1:
            cactus = Cactus()
            obstacles.add(cactus)
        player.update()
        score.update()



        # Обновление экрана/Screen Refresh
        pygame.display.update()


if __name__ == "__main__":
    main()