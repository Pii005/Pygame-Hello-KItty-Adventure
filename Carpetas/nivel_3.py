import pygame
import sys
from AA_Kitty import *
from Modulo import *
from CC_Pantalla import *
from DD_Plataformas import *
from AA_Enemigos import *
from CC_Recolectar import *
from CC_textos import *
from AA_trampas import *
import time
from AA_kittana import *
from CC_Barra import *
from CC_Puntos import *
from AA_puerta_final import Puerta, diccionario_puerta
from DD_piso import *

from FF_Crear_nivel import *

pygame.init()
pygame.font.init()



class nivelUno(Nivel):
    def __init__(self, pantalla: pygame.surface) -> None:
        w = pantalla.get_width()
        h = pantalla.get_height()

        fondo = pygame.image.load("Fotos\Fondo_Uno.png")
        
        # fondo = pygame.image.load("Imagenes\Fondo_dos.jpg")
        fondo = pygame.transform.scale(fondo, (W, H))

        mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 8)

        # piso = pygame.Rect(0, 380, W, 20)
        # piso.top = mi_personaje.lados["main"].bottom
        # lados_piso = obtener_rectangulo(piso)
        
        piso = Piso(0, 730, W, 20)

        piso.crear_piso(pantalla)
        
        contador_reloj(tiempo_inicial, pantalla)
        # Vidas_personaje(pantalla, mi_personaje)

        plataforma_uno = Plataformas("Fotos\Piedra.png",(276, 633),(400,75), (500,620))
        plataforma_dos = Plataformas("Fotos\Piedra.png",(606, 513), (400,75), (1076, 503))
        plataforma_tres = Plataformas("Fotos\Piedra.png",(1024, 410), (400,75), (0, 0))
        plataforma_cuatro = Plataformas("Fotos\Piedra.png",(520, 285), (400,75), (0, 0))
        plataforma_cinco = Plataformas("Fotos\Piedra.png",(26, 180), (400,75), (509, 193))

        lista_plataformas_uno = [plataforma_uno, plataforma_dos, plataforma_tres, plataforma_cuatro, plataforma_cinco]

        lista_gravedad_uno = [piso.lados["top"], plataforma_uno.lados["top"], plataforma_dos.lados["top"],
                    plataforma_tres.lados["top"], plataforma_cuatro.lados["top"], plataforma_cinco.lados["top"]]
        
        enemigo_uno = enemigo((284, 545),(597, 557),diccionario_enemigo, Tamaño_enemigo, 1)
        

        Enemigos = [enemigo_uno]

        


        lista_objetos = []

        elemento_recuperar_uno = Elementos(animacion_mas_vidas, (1328, 364), (40,40))

        lista_recuperar = [elemento_recuperar_uno]

        llave_nivel_uno = Elementos(animaciones_llave, (72, 107), (25, 60))
        lista_llave_uno = [llave_nivel_uno]

        flor_trampa_uno = Trampas((1292, 72), (1287, 364), (80,80))

        listas_trampas = [flor_trampa_uno]

        puerta_nivel_uno = Puerta(diccionario_puerta, (1353, 603))

        super().__init__(pantalla, fondo, mi_personaje, lista_plataformas_uno, lista_gravedad_uno, Enemigos, lista_objetos, lista_recuperar, listas_trampas, lista_llave_uno, puerta_nivel_uno, None, False)


# nivel_uno = nivel_uno(pantalla)
