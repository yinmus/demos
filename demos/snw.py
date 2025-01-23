import pygame
import random
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Title")

background_color = (0, 0, 0)
particle_color = (255, 255, 255)

class Particle:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(-20, height)
        self.size = random.randint(3, 6)
        self.speed = random.randint(1, 3)
        self.angle = random.uniform(-math.pi / 4, math.pi / 4)
        self.alpha = random.randint(100, 255)

    def update(self):
        self.x += self.speed * math.sin(self.angle)
        self.y += self.speed * math.cos(self.angle)
        if self.y > height:
            self.y = random.randint(-20, -1)
            self.x = random.randint(0, width)

    def draw(self):
        pygame.draw.circle(screen, (self.alpha, self.alpha, self.alpha), (self.x, self.y), self.size)

particles = [Particle() for _ in range(200)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    screen.fill(background_color)

    for particle in particles:
        particle.update()
        particle.draw()

    pygame.display.flip()

    pygame.time.delay(10)

pygame.quit()
