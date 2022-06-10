from generador import *
import threading
import time

inicio=0

limit=0
start=0
servidos=[]
atendiendo=[]
esperando=[]

funcion={
    'normal':normal,
    'exponencial':exponencial,
    'uniforme':uniforme
}

class Cliente:
    entrada=0
    salida=-1
    servicio=-1

    def __init__(self, tiempo):
        self.entrada=tiempo

    def servicio(self, tiempo):
        self.servicio=tiempo

    def salida(self,tiempo):
        self.salida=tiempo
