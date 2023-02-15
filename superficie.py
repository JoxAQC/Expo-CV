import pygame

# Inicializar pygame
pygame.init()

# Definir el tamaño de la pantalla
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Definir los puntos de control de la superficie
puntos_control = [
    [(100, 100), (150, 200), (200, 100), (250, 150)],
    [(100, 250), (150, 300), (200, 250), (250, 300)],
    [(100, 400), (150, 400), (200, 450), (250, 400)],
    [(300, 100), (350, 150), (400, 100), (450, 150)],
    [(300, 250), (350, 300), (400, 250), (450, 300)],
    [(300, 400), (350, 400), (400, 450), (450, 400)],
    [(500, 100), (550, 200), (600, 100), (650, 150)],
    [(500, 250), (550, 300), (600, 250), (650, 300)],
    [(500, 400), (550, 400), (600, 450), (650, 400)]
]

# Ciclo principal de la aplicación
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Dibujar la superficie de Bezier
    pygame.draw.lines(screen, (255, 255, 255), False, puntos_control[0], 2)
    pygame.draw.lines(screen, (255, 255, 255), False, [puntos_control[i][0] for i in range(9)], 2)
    for i in range(100):
        for j in range(100):
            # Calcular la posición de la superficie en los puntos (i/100, j/100)
            x, y = 0, 0
            for k in range(4):
                for l in range(4):
                    coef = ((i/100)**k * (1-i/100)**(3-k) *
                            (j/100)**l * (1-j/100)**(3-l))
                    x += coef * puntos_control[k][l][0]
                    y += coef * puntos_control[k][l][1]
            # Dibujar un punto en la posición de la superficie
            pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 2)

    # Actualizar la pantalla
    pygame.display.flip()
