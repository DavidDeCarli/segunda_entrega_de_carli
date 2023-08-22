#Tiro con arco

import random

class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self) -> str:
        return f"Bienvenido {self.nombre} {self.apellido} al tiro con arco"
    
class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, flechas, aciertos):
        super().__init__(nombre, apellido, edad)
        self.flechas = flechas
        self.aciertos = aciertos

        if self.edad <= 18:
            print("Las personas menores de edad no pueden ingresar al tiro con arco")

    def tirar(self):
        if self.flechas > 0:
            self.flechas -= 1
            carcaj.append(1)
            if random.random() < 0.5:
                self.aciertos += 1
                print(f"{self.nombre}, Acertaste! Te quedan {self.flechas} flechas")
            else:
                print(f"{self.nombre}, fallaste. Te quedan {self.flechas} flechas")
        else:
            print("Te quedaste sin flechas")
    
    def calcular_aciertos(self):
        if self.flechas == 0:
            return 0
        porcentaje = (self.aciertos / self.flechas) * 100
        return porcentaje

carcaj=[]