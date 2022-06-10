import math
import numpy as np
import random

def uniforme(listaFuncion):
    a=listaFuncion[0]
    b=listaFuncion[1]
    x=random.random()

    return(x*(b-a))+a

def exponencial(listaFuncion):
    #TODO
    x=listaFuncion[0]
    m=listaFuncion[1]
    r=random.random()
    exp=(-1/m)*math.log(r)
    return exp

def normal(listaFuncion):
    m=listaFuncion[1]
    sd=listaFuncion[0]
    u=0
    v=0

    u=random.random()
    v=random.random()

    x=math.sqrt( -2.0 * math.log( u ) ) * math.cos( 2.0 * math.pi * v )
    return x*sd-(-1*m)
