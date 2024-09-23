import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
ancho, alto = 600, 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Dibujar Casa con Nubes en Forma de Corazón')

# Colores
color_casa = (139, 69, 19)  # Marrón para la casa
color_techo = (255, 0, 0)    # Rojo para el techo
color_puerta = (100, 50, 0)  # Marrón oscuro para la puerta
color_nube = (255, 255, 255) # Blanco para las nubes

# Función para dibujar un corazón
def dibujar_corazon(x, y):
    pygame.draw.polygon(pantalla, color_nube, [(x, y), (x + 20, y - 20), (x + 40, y), (x + 20, y + 20)])
    pygame.draw.circle(pantalla, color_nube, (x + 10, y - 10), 10)
    pygame.draw.circle(pantalla, color_nube, (x + 30, y - 10), 10)

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar fondo azul claro
    pantalla.fill((135, 206, 235))

    # Dibujar la casa
    pygame.draw.rect(pantalla, color_casa, (200, 200, 200, 200))  # Casa
    pygame.draw.polygon(pantalla, color_techo, [(200, 200), (400, 200), (300, 100)])  # Techo
    pygame.draw.rect(pantalla, color_puerta, (280, 300, 40, 100))  # Puerta

    # Dibujar nubes en forma de corazón
    dibujar_corazon(50, 50)
    dibujar_corazon(150, 70)
    dibujar_corazon(500, 30)
    dibujar_corazon(450, 70)

    # Actualizar la pantalla
    pygame.display.flip()
