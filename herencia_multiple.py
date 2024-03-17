# Herencia Multiple
class Telefono:
    def __init__(self):
        pass
    
    def llamar(self):
        print("Llamando")
    def ocupado(self):
        print("Ocupado")

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print('Tomando fotos...')

class Reproduccion:
    def __init__(self):
        pass
    def reproduccion_musica(self):
        print('Reproduciendo musica...')
    def reproduccion_video(self):
        print('Reproduciendo video...')