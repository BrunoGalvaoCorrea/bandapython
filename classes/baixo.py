from classes.instrumento import Instrumento


class Baixo(Instrumento):
    def __init__(self):
        super().__init__('..\\som\\baixo.wav')