import pygame
import random
import math
import time
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DEC_V = 6
myTime = 0.0
fr = 0
fullscreen = False
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Rendering Example")
running = True
clock = pygame.time.Clock()
while running:
    start_ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    myTime += 0.0003
    window.fill((0, 0, 0))
    fr += 1
    random.seed(myTime)
    for i in range(100):
        x = random.random()
        y = random.random()
        new_color = random.randint(0, 0xFFFFFF)
        for j in range(2000):
            x = (myTime + x + math.cos(y * 2.2 + x * 0.1)) % 1.0
            y = (myTime * 0.3 + y + math.sin(x * 1.5)) % 1.0
            r = (new_color >> 16) & 0xFF
            g = (new_color >> 8) & 0xFF
            b = new_color & 0xFF
            pygame.draw.circle(window, (r, g, b), (int(x * WINDOW_WIDTH), int(y * WINDOW_HEIGHT)), 1)
    pygame.display.flip()
    frame_ticks = pygame.time.get_ticks() - start_ticks
    if frame_ticks > 0:
        fps = 1000.0 / frame_ticks
        pygame.display.set_caption(f"FPS: {fps:.2f}")
    clock.tick(60)
pygame.quit()
