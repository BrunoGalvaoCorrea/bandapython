import random
from time import sleep


class Banda:
    def __init__(self, musicos, tipo, nome):
        self._musicos = musicos
        self._estilo = tipo
        self._nome = nome

    def tocar(self):
        while True:
            numero = random.randint(0, len(self._musicos)-1)
            self._musicos[numero].tocar()



