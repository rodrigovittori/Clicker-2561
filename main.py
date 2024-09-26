#pgzero

"""
M6.L3: Actividad #1 - "Clicker animal"
Objetivo: Crear ventana de juego

PACK DE ASSETS: https://kenney.nl/assets/animal-pack-redux
"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 30 # Fotogramas por segundo
puntuacion = 0

#OBJETOS
fondo = Actor("background")
animal = Actor("giraffe", (150, 250))

def draw():
    fondo.draw()
    animal.draw()
    screen.draw.text(str(puntuacion), center=(150, 70), color="white", fontsize = 96)
    
def on_mouse_down(button, pos):
    global puntuacion
    if button == mouse.LEFT:
        puntuacion += 1