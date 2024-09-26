#pgzero

"""
M6.L3: Actividad #4 - "Temporizador"
Objetivo: Agregar lógica del click en los botones de bonificación pasiva y
            las invocaciones/llamadas programadas (schedule_interval)

PACK DE ASSETS: 
ANIMALES: https://kenney.nl/assets/animal-pack-redux 
BOTONES:  https://kenney.nl/assets/ui-pack

Paso Nº 1: Crear las funciones bonus
Paso Nº 2: Comprobar click sobre botones
Paso Nº 3: Verificar que el jugador tenga puntos suficientes para poder comprar el bonus (y restar esos puntos)
Paso Nº 4: Programar la llamada reiterativa a las funciones bonus y setearlas como activas

Extra: agregar animaciones a los botones en caso de compra y en caso de NO poder comprarlo
Extra Nº 2: Agregamos un "cheat" para poder probar los bonus sin farmear clicks

"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 30 # Fotogramas por segundo

# VARIABLES
puntuacion = 0
click_mult = 1 # multiplicador del valor por click
token = "💀"

#OBJETOS
fondo = Actor("background")
animal = Actor("giraffe", (150, 250))

bonus_1 = Actor("bonus", (450, 100))
bonus_1.precio = 15
bonus_1.potenciador = 1
bonus_1.ya_activado = False

bonus_2 = Actor("bonus", (450, 200))
bonus_2.precio = 200
bonus_2.potenciador = 15
bonus_2.ya_activado = False

"""
bonus_3 = Actor("bonus", (450, 300))
bonus_3.precio = 600
bonus_3.potenciador = 50
bonus_3.ya_activado = False
"""

""" #####################
   # FUNCIONES PROPIAS #
  ##################### """

def el_bonus_1():
    global puntuacion
    puntuacion += bonus_1.potenciador

def el_bonus_2():
    global puntuacion
    puntuacion += bonus_2.potenciador

"""
def el_bonus_3():
    global puntuacion
    puntuacion += bonus_3.potenciador
"""


""" ####################
   # FUNCIONES PGZERO #
  #################### """

def draw():
    fondo.draw()
    animal.draw()
    # Dibujamos puntuacion
    # To-do: Agregar control que chequee que el texto no se salga de la pantalla (ajusta vble fontsize) 
    screen.draw.text((str(puntuacion) + token), center=(150, 70), color="white", fontsize = 96)

    # Dibujamos botones bonus

    bonus_1.draw()
    screen.draw.text(("+" + str(bonus_1.potenciador) + " " + token + " cada 2 seg"), center = (450, 80), color = "black", fontsize = 20)
    screen.draw.text(("PRECIO: " + str(bonus_1.precio) + " " + token), center = (450, 110), color = "black", fontsize = 20)
        
    bonus_2.draw()
    screen.draw.text(("+" + str(bonus_2.potenciador) + " " + token + " cada 2 seg"), center = (450, 180), color = "black", fontsize = 20)
    screen.draw.text(("PRECIO: " + str(bonus_2.precio) + " " + token), center = (450, 210), color = "black", fontsize = 20)

    """bonus_3.draw()
    screen.draw.text(("+" + str(bonus_3.potenciador) + " " + token + " cada 2 seg"), center = (450, 280), color = "black", fontsize = 20)
    screen.draw.text(("PRECIO: " + str(bonus_3.precio) + " " + token), center = (450, 310), color = "black", fontsize = 20)
    """

def on_mouse_down(button, pos):
    global puntuacion
    
    if (button == mouse.LEFT):
        
        if animal.collidepoint(pos):
            puntuacion += click_mult
            animal.y = 200
            animate(animal, tween="bounce_end", duration = 0.5, y = 250)

        elif bonus_1.collidepoint(pos):
            # Si el click fue sobre el botón de bonus # 1:
            if (puntuacion >= bonus_1.precio):
                # Chequeamos si tiene suficientes puntos para comprarlo:
                # Chequeamos si ya está activo
                if (not bonus_1.ya_activado):
                    schedule_interval(el_bonus_1, 2)
                    bonus_1.ya_activado = True
                else:
                    bonus_1.potenciador += 1
                # Restamos los puntos gastados para compar el bonus:
                puntuacion -= bonus_1.precio
                # bonus_1.precio *= 2

                # Animamos el botón cuando pueda comprarlo
            
            else:
                # Si no tiene suficientes puntos para comprarlo
                bonus_1.x = 445
                animate(bonus_1, tween='bounce_end', duration=0.25, x=450)
                bonus_1.x = 455
                animate(bonus_1, tween='bounce_end', duration=0.25, x=450)

        elif bonus_2.collidepoint(pos):
            # Si el click fue sobre el botón de bonus # 2:
            if (puntuacion >= bonus_2.precio):
                # Chequeamos si tiene suficientes puntos para comprarlo:
                # Chequeamos si ya está activo
                if (not bonus_2.ya_activado):
                    schedule_interval(el_bonus_2, 2)
                    bonus_2.ya_activado = True
                else:
                    bonus_2.potenciador += 15
                    
                # Restamos los puntos gastados para compar el bonus:
                puntuacion -= bonus_2.precio
                # bonus_2.precio *= 2

                # Animamos el botón cuando pueda comprarlo
                
            else:
                # Si no tiene suficientes puntos para comprarlo
                bonus_2.x = 445
                animate(bonus_2, tween='bounce_end', duration=0.25, x=450)
                bonus_2.x = 455
                animate(bonus_2, tween='bounce_end', duration=0.25, x=450)

        # To-do: agregar lógica para el bonus 3


######################

def on_key_down(key):
    global puntuacion
    
    if keyboard.d:
        puntuacion += 500
        
    if keyboard.a:
        puntuacion = 0
    
