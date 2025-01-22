import pygame
import math
import random


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Rotating Icosahedron")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PHI = (1 + math.sqrt(5)) / 2  
vertices = [
    (-1, PHI, 0), (1, PHI, 0), (-1, -PHI, 0), (1, -PHI, 0),
    (0, -1, PHI), (0, 1, PHI), (0, -1, -PHI), (0, 1, -PHI),
    (PHI, 0, -1), (PHI, 0, 1), (-PHI, 0, -1), (-PHI, 0, 1)
]

edges = [
    (0, 11), (0, 5), (0, 1), (0, 7), (0, 10),
    (1, 5), (1, 9), (1, 8), (1, 7), (2, 11),
    (2, 10), (2, 3), (2, 6), (2, 4), (3, 6),
    (3, 9), (3, 8), (3, 4), (4, 9), (4, 5),
    (5, 11), (6, 10), (6, 8), (7, 10), (7, 8),
    (9, 11)
]

SCALE = 150
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

edge_colors = [
    (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    for _ in edges
]

def rotate_point(x, y, z, angle_x, angle_y):
    cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
    y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x

    cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
    x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y

    return x, y, z



running = True
angle_x, angle_y = 0, 0
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    angle_x += 0.01
    angle_y += 0.01


    projected_points = []
    for x, y, z in vertices:
        x, y, z = rotate_point(x, y, z, angle_x, angle_y)
        
        factor = SCALE / (z + 3) if z + 3 != 0 else SCALE
        x_proj = int(x * factor + CENTER_X)
        y_proj = int(y * factor + CENTER_Y)
        projected_points.append((x_proj, y_proj))

    for edge, color in zip(edges, edge_colors):
        start, end = edge
        pygame.draw.line(screen, color, projected_points[start], projected_points[end], 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
