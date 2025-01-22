import pygame
import math
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Serene Galaxy with Mouse Control")
clock = pygame.time.Clock()


BLACK = (0, 0, 0)


NUM_STARS = 1000
stars = [
    {
        "x": random.uniform(0, WIDTH),
        "y": random.uniform(0, HEIGHT),
        "z": random.uniform(0.1, 3),
        "brightness": random.randint(100, 255),
    }
    for _ in range(NUM_STARS)
]


CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
radius_galaxy = 250
num_particles = 300  


mouse_x, mouse_y = WIDTH // 2, HEIGHT // 2  
angle_x, angle_y = 0, 0  


camera_speed = 0.1
zoom_level = 1
star_speed = 0.05


def update_stars():
    for star in stars:
        star["x"] += random.uniform(-star_speed, star_speed) / star["z"]
        star["y"] += random.uniform(-star_speed, star_speed) / star["z"]
        star["brightness"] += random.randint(-1, 2)
        star["brightness"] = max(100, min(255, star["brightness"]))

        if star["x"] < 0 or star["x"] > WIDTH or star["y"] < 0 or star["y"] > HEIGHT:
            star["x"] = random.uniform(0, WIDTH)
            star["y"] = random.uniform(0, HEIGHT)


def draw_stars():
    for star in stars:
        color = (star["brightness"], star["brightness"], star["brightness"])
        pygame.draw.circle(screen, color, (int(star["x"]), int(star["y"])), max(1, int(3 / star["z"])))


def draw_galaxy():
    global angle_x, angle_y
    for i in range(num_particles):
        angle = i * (2 * math.pi / num_particles) + angle_x
        radius = radius_galaxy + 20 * math.sin(angle_y + i * 0.1)
        x = CENTER_X + radius * math.cos(angle)
        y = CENTER_Y + radius * math.sin(angle)

        
        r = int(255 * (0.5 + 0.5 * math.sin(angle)))
        g = int(255 * (0.5 + 0.5 * math.sin(angle + 2 * math.pi / 3)))
        b = int(255 * (0.5 + 0.5 * math.sin(angle + 4 * math.pi / 3)))
        color = (r, g, b)

        pygame.draw.circle(screen, color, (int(x), int(y)), 3)


def draw_galaxy_center():
    global angle_x, angle_y
    num_particles_center = 200
    for i in range(num_particles_center):
        angle = i * (2 * math.pi / num_particles_center) + angle_x
        radius = 30 + 10 * math.sin(angle_y + i)
        x = CENTER_X + radius * math.cos(angle)
        y = CENTER_Y + radius * math.sin(angle)

        
        r = int(255 * (0.5 + 0.5 * math.sin(angle)))
        g = int(255 * (0.5 + 0.5 * math.sin(angle + 2 * math.pi / 3)))
        b = int(255 * (0.5 + 0.5 * math.sin(angle + 4 * math.pi / 3)))
        color = (r, g, b)

        pygame.draw.circle(screen, color, (int(x), int(y)), 5)


def draw_nebula():
    num_nebula_particles = 100  
    for _ in range(num_nebula_particles):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(100, 300)
        x = CENTER_X + radius * math.cos(angle)
        y = CENTER_Y + radius * math.sin(angle)
        radius_variation = random.uniform(12, 30)

        
        color = (
            random.randint(120, 200),
            random.randint(80, 180),
            random.randint(160, 255),
        )
        pygame.draw.circle(screen, color, (int(x), int(y)), int(radius_variation), width=2)


def handle_mouse_control():
    global mouse_x, mouse_y, angle_x, angle_y, zoom_level, star_speed

    
    new_mouse_x, new_mouse_y = pygame.mouse.get_pos()

    
    angle_x += (new_mouse_x - mouse_x) * camera_speed
    angle_y += (new_mouse_y - mouse_y) * camera_speed

    
    if pygame.mouse.get_pressed()[2]:  
        zoom_level += (new_mouse_y - mouse_y) * 0.001
        zoom_level = max(0.5, min(zoom_level, 3))  
        
        star_speed = max(0.01, min(star_speed + (new_mouse_y - mouse_y) * 0.00005, 0.2))

    mouse_x, mouse_y = new_mouse_x, new_mouse_y


running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Выход при нажатии 'q'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    
    handle_mouse_control()

    
    update_stars()

    
    draw_stars()
    draw_galaxy_center()
    draw_galaxy()
    draw_nebula()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
