import winsound
from abc import ABC, abstractmethod

class Instrumento(ABC):

    @abstractmethod
    def __init__(self, som):
        self._som = som

    def tocar(self):
        print(self._som)
        winsound.PlaySound(self._som, winsound.SND_FILENAME)