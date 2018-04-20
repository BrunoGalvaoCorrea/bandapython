class Musico:
    def __init__(self, nm, id, inst):
        self._nome = nm
        self._idade = id
        self._instrumento = inst

    def tocar(self):
        self._instrumento.tocar()


