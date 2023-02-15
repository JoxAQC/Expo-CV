import pygame

# Definir los vértices de la malla
vertices = [(100, 100), (200, 100), (200, 200), (100, 200)]

# Definir los índices de los triángulos que forman la malla
indices = [(0, 1, 2), (0, 2, 3)]

# Inicializar pygame
pygame.init()

# Definir el tamaño de la pantalla
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Ciclo principal de la aplicación
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Dibujar la malla
    pygame.draw.polygon(screen, (255, 255, 255), vertices, 2)
    for triangle in indices:
        pygame.draw.polygon(screen, (0, 255, 0), [vertices[i] for i in triangle], 0)
        pygame.draw.polygon(screen, (255, 255, 255), [vertices[i] for i in triangle], 2)
    
    # Actualizar la pantalla
    pygame.display.flip()
