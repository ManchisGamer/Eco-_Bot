import random
from data import tips, retos, datos

def dar_tip():
    return random.choice(tips)

def dar_reto():
    return random.choice(retos)

def dar_dato():
    return random.choice(datos)