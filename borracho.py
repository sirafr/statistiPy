# CLASE 6
import random

class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre

    def camina(self):
        return (
            random.choice([
                (random.random(), random.random() * -1),
                (random.random() * -1, random.random()),
                (random.random() * -1, random.random() * -1),
                (random.random(), random.random()),
            ])
        ) 


class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(-1, -2), (-2, 4), (-5, 5), (-1, 2)])