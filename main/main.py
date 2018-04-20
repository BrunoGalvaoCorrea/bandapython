from classes.baixo import Baixo
from classes.banda import Banda
from classes.bateria import Bateria
from classes.guitarra import Guitarra
from classes.musico import Musico


class Main:
    def  __init__(self):
        pass

if __name__ == '__main__':
    # Instrumentos
    guitarra = Guitarra()
    baixo = Baixo()
    bateria = Bateria()
    # Musicos
    guitarrista1 = Musico('Steve', 25, guitarra)
    #guitarrista2 = Musico('Cabeca', 27, guitarra)
    baixista = Musico('Brito', 30, baixo)
    baterista = Musico('Barker', 42, bateria)

    lista_musicos = [guitarrista1, baixista, baterista]
    #Banda

    banda = Banda(lista_musicos, 'Rock', 'FH')
    banda.tocar()



