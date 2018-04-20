from classes.instrumento import Instrumento


class Bateria(Instrumento):
    def __init__(self):
        super().__init__('..\\som\\drum.wav')