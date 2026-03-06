import random
from data import preguntas

def hacer_pregunta():

    pregunta = random.choice(preguntas)

    texto = pregunta[0]
    respuesta = pregunta[1]

    return texto, respuesta