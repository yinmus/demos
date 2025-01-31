import pygame
import math
import sys
import numpy as np

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plasma Effect")

clock = pygame.time.Clock()

def generate_palette():
    palette = []
    for i in range(64):
        r = int((math.sin(i * 0.1) + 1) * 127)
        g = int((math.sin(i * 0.15) + 1) * 127)
        b = int((math.sin(i * 0.2) + 1) * 127)
        palette.append((r, g, b))
    return palette

palette = generate_palette()

def plasma(x, y, time):
    return int((math.sin(x * 0.1 + time * 0.05) + 
                math.sin(y * 0.1 + time * 0.05) + 
                math.sin((x + y) * 0.1 + time * 0.05)) * 64) % 64

time = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    for y in range(HEIGHT):
        for x in range(WIDTH):
            palette_index = plasma(x, y, time)
            screen.set_at((x, y), palette[palette_index])

    pygame.display.flip()

    time += 1

    if time % 100 == 0:
        palette = generate_palette()

    clock.tick(60)

