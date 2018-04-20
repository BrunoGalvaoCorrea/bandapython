from classes.instrumento import Instrumento


class Guitarra(Instrumento):
    def __init__(self):
        super().__init__('..\\som\\guitar.wav')