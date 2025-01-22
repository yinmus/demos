import pygame
import random
import math


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Эффект частиц")


background_color = (0, 0, 0)  
particle_color = (0, 255, 255)  


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(3, 6)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)
        self.alpha = random.randint(100, 255)  
        self.angle = random.uniform(0, 2 * math.pi)
        self.lifetime = random.randint(50, 200)  

    def update(self):
        
        self.x += math.cos(self.angle) * 2
        self.y += math.sin(self.angle) * 2

        self.size -= 0.05  
        self.lifetime -= 1  
        if self.size <= 0:
            self.size = 0  
        if self.lifetime <= 0:
            return False  
        return True

    def draw(self, screen):
        pygame.draw.circle(screen, (self.alpha, self.alpha, self.alpha), (int(self.x), int(self.y)), int(self.size))


particles = []


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Выход при нажатии 'q'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    
    screen.fill(background_color)

    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    
    particles.append(Particle(mouse_x, mouse_y))

    
    particles = [particle for particle in particles if particle.update()]
    for particle in particles:
        particle.draw(screen)

    
    pygame.display.flip()

    
    pygame.time.delay(10)


pygame.quit()
