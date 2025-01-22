import pygame
import random
import math


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graph Animation")
clock = pygame.time.Clock()


NUM_NODES = 30
MAX_DISTANCE = 150


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)


nodes = [
    {
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),
        "vx": random.uniform(-1, 1),
        "vy": random.uniform(-1, 1),
    }
    for _ in range(NUM_NODES)
]


def update_nodes():
    for node in nodes:
        node["x"] += node["vx"]
        node["y"] += node["vy"]

        
        if node["x"] <= 0 or node["x"] >= WIDTH:
            node["vx"] *= -1
        if node["y"] <= 0 or node["y"] >= HEIGHT:
            node["vy"] *= -1


def draw_graph():
    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes):
            if i != j:
                
                distance = math.sqrt(
                    (node1["x"] - node2["x"]) ** 2 + (node1["y"] - node2["y"]) ** 2
                )
                if distance < MAX_DISTANCE:
                    
                    intensity = max(0, 255 - int(distance / MAX_DISTANCE * 255))
                    color = (intensity, intensity, intensity)
                    pygame.draw.line(
                        screen, color, (node1["x"], node1["y"]), (node2["x"], node2["y"]), 1
                    )

    for node in nodes:
        pygame.draw.circle(screen, WHITE, (int(node["x"]), int(node["y"])), 3)


def add_node_at_position(x, y):
    nodes.append({
        "x": x,
        "y": y,
        "vx": random.uniform(-1, 1),
        "vy": random.uniform(-1, 1),
    })


running = True
while running:
    screen.fill(BLACK)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            x, y = event.pos
            add_node_at_position(x, y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    update_nodes()
    draw_graph()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
