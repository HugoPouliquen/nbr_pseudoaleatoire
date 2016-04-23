import random

def nombres_aleatoires():
    i = z = 0
    i = 1
    for i in range(101):
        z = round(3*random.random())
        print(z, end=' ')

nombres_aleatoires()
