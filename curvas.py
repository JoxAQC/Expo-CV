import pygame

# Inicializar pygame
pygame.init()

# Definir el tamaño de la pantalla
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Definir los puntos de control de la curva
puntos_control = [(100, 100), (400, 300), (500, 100)]

# Ciclo principal de la aplicación
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Dibujar la curva de Bezier
    pygame.draw.lines(screen, (255, 255, 255), False, puntos_control, 2)
    for t in range(101):
        # Calcular la posición de la curva en el punto t/100
        p0, p1, p2 = puntos_control
        t_norm = t / 100
        x = int((1-t_norm)**2 * p0[0] + 2 * t_norm * (1-t_norm) * p1[0] + t_norm**2 * p2[0])
        y = int((1-t_norm)**2 * p0[1] + 2 * t_norm * (1-t_norm) * p1[1] + t_norm**2 * p2[1])
        # Dibujar un punto en la posición de la curva
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 2)

    # Actualizar la pantalla
    pygame.display.flip()
