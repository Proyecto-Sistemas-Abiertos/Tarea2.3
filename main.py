import herencia_multiple as h

class smartphone(h.Telefono, h.Camara, h.Reproduccion):
    def __del__(self): # Destructor (Recoger elementos basura, para el ahorro de memoria)
        print('Telefono apagado')

movil = smartphone()
#print(dir(movil)) #ver que metodos/atributos tenemos disponibles para ejecutar
print(movil.llamar())
print(movil.fotografia())
