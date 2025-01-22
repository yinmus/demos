import pygame
import random
import math


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Гравитационные частицы")


background_color = (0, 0, 0)  
particle_color = (0, 255, 255)  


gravity_strength = 0.1


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(3, 6)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)
        self.alpha = random.randint(100, 255)  
        self.lifetime = random.randint(100, 200)  

    def update(self, target_x, target_y):
        
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        
        if distance > 0:
            dx /= distance
            dy /= distance

        
        self.speed_x += dx * gravity_strength
        self.speed_y += dy * gravity_strength

        
        self.x += self.speed_x
        self.y += self.speed_y

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
    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    
    if random.random() < 0.1:  
        particles.append(Particle(random.randint(0, width), random.randint(0, height)))

    
    screen.fill(background_color)

    
    particles = [particle for particle in particles if particle.update(mouse_x, mouse_y)]
    for particle in particles:
        particle.draw(screen)

    
    pygame.display.flip()

    
    pygame.time.delay(10)


pygame.quit()
