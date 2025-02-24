import pygame
import math
import random

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600 #ancho y alto
#colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
Color1 = (255, 255, 255)
Color2 = (18,161,164)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Practica 2")


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        radio = math.sqrt(self.x ** 2 + self.y ** 2)
        angulo = math.degrees(math.atan2(self.y, self.x))
        return radio, angulo

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def transformar(self):
        """Transforma coordenadas cartesianas a las de la pantalla de pygame (invertir Y)"""
        return self.x + WIDTH // 2, HEIGHT // 2 - self.y


class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def dibujaLinea(self):
        pygame.draw.line(screen, Color2, self.p1.transformar(), self.p2.transformar(), 2)


class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def dibujaCirculo(self):
        pygame.draw.circle(screen, Color1, self.centro.transformar(), self.radio, 2)


#1 = Punto(0,3)
#print(p1)
#x,y = p1.coord_cartesianas()
#print(x,y)
#r,a = p1.coord_polares()
#print(r,a)

# Crear elementos

#p1 = Punto(-150, 50)
p1 = Punto(random.randint(-100,100), random.randint(-100,100))
#p2 = Punto(50, 50)
p2 = Punto(random.randint(-100,100), random.randint(-100,100))

print(p1)
print(p2)
x,y = p1.coord_cartesianas()
print(x,y)
r,a = p1.coord_polares()
print(r,a)



#texto
pygame.font.init()
font = pygame.font.Font(None, 25)  # Tamaño de fuente 36

# Color del texto (RGB)
text_color = (255, 255, 255)  # Blanco

# Renderizar el texto
text1 = font.render(f"p1 = {p1}", True, text_color)
text2 = font.render(f"p2 = {p2}", True, text_color)
text3 = font.render(f"radio: {r:.2f}, angulo {a:.2f}", True, text_color)




linea = Linea(p1,p2)
circulo = Circulo(p1, r)

# Loop de pygame
running = True
while running:
    screen.fill(BLACK)
    linea.dibujaLinea()
    circulo.dibujaCirculo()

    # Posicionar el texto en la pantalla
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 30))
    screen.blit(text3, (10, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
