import pygame

NEGRO  = (   0,   0,   0)
BLANCO = ( 255, 255, 255)
VERDE  = (   0, 255,   0)
ROJO   = ( 255,   0,   0)

tamPantalla = [527, 398]

pantalla = pygame.display.set_mode(tamPantalla)
pygame.display.set_caption("POKEMON")


def imagenes(tamano,posicion,ruta):
  imagen = pygame.image.load(ruta)
  imagen = pygame.transform.scale(imagen,tamano)
  pantalla.blit(imagen,posicion)
  pygame.display.flip()


    #CICLO PRESENTACION
    # Se muestra la imagen de dragon con el nombre del juego
    # Despues de contar hasta 200 pasa a la siguiente imagen
    # sale la imagen para oprimir la barra espaciadora y pasar a la introduccion
#'''
def Presentacion():
    reloj = pygame.time.Clock()
    pag,ver_pag, terminar = 1, True, False
    while not terminar and ver_pag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar = True
                return terminar
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pantalla.fill(NEGRO)
                    ver_pag = False
        if pag == 1:
            imagenes(tamPantalla,[0,0],"img/Pinicial/inicial1.jpg")
            reloj.tick(0.5)
        if pag == 2:
            imagenes([527,398],[0,0],"img/Pinicial/inicial2.jpg")
            reloj.tick(0.7)
        if pag == 3:
            imagenes([260,80],[133,310],"img/Pinicial/barespa.png")
        pag += 1
    return False # Para indicar que la presentacion sigue
        #'''
def Introduccion(terminar):
    reloj = pygame.time.Clock()
    pag,ver_pag = 1, True
    while not terminar and ver_pag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar = True
                return terminar
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pag += 1
                    pantalla.fill(NEGRO)
        if pag == 1:
    		imagenes([527,308],[0,0],"img/Introduccion/Oak1.png")
    		imagenes([400,80],[60,310],"img/Introduccion/Introduccion1.png")
    		reloj.tick(0.7)
        imagenes([20,20],[480,330],"img/Teclado/A.png")
        if pag == 2:
            imagenes([527,308],[0,0],"img/Introduccion/OakLab.png")
            imagenes([400,80],[60,310],"img/Introduccion/Introduccion2.png")
            reloj.tick(0.7)
        imagenes([20,20],[480,330],"img/Teclado/A.png")
        if pag == 3:
            imagenes([527,308],[0,0],"img/Introduccion/Oak2.png")
            imagenes([400,80],[60,310],"img/Introduccion/Introduccion3.png")
            reloj.tick(0.7)
        imagenes([20,20],[480,330],"img/Teclado/A.png")
        if pag == 4:
            imagenes([527,308],[0,0],"img/Introduccion/Oak3.png")
            imagenes([400,80],[60,310],"img/Introduccion/Introduccion4.png")
            reloj.tick(0.7)
        imagenes([20,20],[480,330],"img/Teclado/A.png")
        if pag == 5:
            imagenes([527,308],[0,0],"img/Introduccion/Nieto.png")
            imagenes([400,80],[60,310],"img/Introduccion/Introduccion5.png")
            reloj.tick(0.7)
        imagenes([20,20],[480,330],"img/Teclado/A.png")
        if pag == 6:
            imagenes([527,308],[0,0],"img/Introduccion/Blue.png")
            imagenes([400,80],[60,310],"img/Introduccion/Introduccion6.png")
            reloj.tick(0.7)
        imagenes([20,20],[480,330],"img/Teclado/A.png")
        if pag == 7:
            imagenes([527,308],[0,0],"img/Introduccion/Vs.png")
            imagenes([400,80],[60,310],"img/Introduccion/Introduccion7.png")
            reloj.tick(0.7)
        imagenes([20,20],[480,330],"img/Teclado/A.png")
        if pag == 8:
            ver_pag = False
    if terminar:
        return True
    else:
        return False

def Controles(terminar):
    reloj = pygame.time.Clock()
    pag,ver_pag = 1, True
    while not terminar and ver_pag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar = True
                return terminar
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pag += 1
                    pantalla.fill(NEGRO)
        if pag == 1:
            imagenes([527,398],[0,0],"img/Controles/Controles.jpg")
            reloj.tick(0.7)
    	imagenes([20,20],[480,330],"img/Teclado/A.png")
        if pag == 2:
            ver_pag = False
    if terminar:
        return True
    else:
        return False # Indica que el juego va a comenzar

if __name__=='__main__':
    pygame.init()
    dim = tamPantalla

    presentacion = Presentacion()
    introduccion = Introduccion(presentacion)
    controles = Controles(introduccion)
