
from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *

Rosa_Bordes = (235,182,250)
Rosa_centro = (252,144,221)
LightCoral = (240,128,128)
Salmon = (250,128,114)

class FormAjustes(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        
        self.pantalla = screen
        self.volumen = pygame.mixer.music.get_volume()
        self.flag_play = True
        pygame.mixer.init()
        
        self.titulo = Label(self._slave, 100, 20, 250, 80, "", "Verdana", 0, Salmon, "sin_fondo\Img_ajustes_titulo-removebg-preview.png")
        self.apagar_prender = Label(self._slave, 40, 120, 180, 50, "Apagar/Prender musica:", "Verdana", 15, "Black", "sin_fondo\\nada.png")
        self.btn_play = Button(self._slave, x, y, 280, 130, 80, 30, Salmon, LightCoral, self.btn_play_click, "Play", "Pause",font = "Verdana", font_size=15, font_color="Black")
        self.label_volumen = Label(self._slave, 280, 200, 50, 50, "20%", "Comic Sans", 15, Salmon, "sin_fondo/vacio.png")
        self.slider_volumen = Slider(self._slave, x, y, 40, 210, 180, 15, self.volumen, LightCoral, Rosa_Bordes)
        
        self._btn_home = Button_Image(screen=self._slave, x=180, y=480, master_x=x, master_y=y, w=140, h=40, color_background=(255,0,0), color_border=(255,0,255), onclick=self.btn_home_click, onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="sin_fondo\\fHello_KItty_Adventure__10_-removebg-preview.png")
        

        pygame.mixer.music.load("Imagenes\Fondo.mp3")#musica que quiero
        pygame.mixer.music.set_volume(self.volumen) #Volumen
        pygame.mixer.music.play(-1) # play
        
        

        self.lista_widgets = []
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.titulo)
        self.lista_widgets.append(self.apagar_prender)

        self.render()

    def render(self):
        self._slave.fill(self._color_background)

    def btn_home_click(self, param): #Volver a los ajustes 
        self.end_dialog() 

    
    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause() #pausar musica
            self.btn_play._color_background = Salmon  #COLOR FONDO boton
            self.btn_play._font_color = "Black" # COLOR texto
            self.btn_play.set_text("Play") #NUEVO MENSAJE
        else: #vuelvo a lo de antes
            pygame.mixer.music.unpause() # despausa musica
            self.btn_play._color_background = Salmon 
            self.btn_play._font_color = "Black"
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play #Bandera de cambios 

    def update_volumen(self, lista_eventos): #AJUSTES DE VOLUMEN
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        


    def update(self, lista_eventos):
        if self.active:
            self.draw()
            self.render()
            self.update_volumen(lista_eventos)
            for wid in self.lista_widgets:
                wid.update(lista_eventos)
            


