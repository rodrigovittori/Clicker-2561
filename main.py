#pgzero

"""
M6.L3: Actividad #2 - "Aumentar la puntuacion"
Objetivo: Agregar condición de collide-point al Actor y animaciones

PACK DE ASSETS: https://kenney.nl/assets/animal-pack-redux

Paso Nº 1: Creamos una variable que controle el multiplicador de click (cuántos puntos sumamos al hacer click sobre nuestro Actor)

"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 30 # Fotogramas por segundo

# VARIABLES
puntuacion = 0
click_mult = 1 # multiplicador del valor por click

#OBJETOS
fondo = Actor("background")
animal = Actor("giraffe", (150, 250))

def draw():
    fondo.draw()
    animal.draw()
    screen.draw.text(str(puntuacion), center=(150, 70), color="white", fontsize = 96)
    
def on_mouse_down(button, pos):
    global puntuacion
    
    if (button == mouse.LEFT):
        if animal.collidepoint(pos):
            puntuacion += click_mult
            animal.y = 200
            animate(animal, tween="bounce_end", duration = 0.5, y = 250)