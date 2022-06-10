import math
import numpy as np
import matplotlib.pyplot as plt

def generaAleatorios(generador,listaGenerador,funcion,listaFuncion,N,M):
    global x0,a,c,m,xn,numerosGenerados,tipo
    tipo=generador
    numerosGenerados=[]
    if generador=="mixto":

        x0=listaGenerador[0]
        a=listaGenerador[1]
        c=listaGenerador[2]
        m=listaGenerador[3]
        xn=x0

    if generador=="multiplicativo":
        x0=listaGenerador[0]
        a=listaGenerador[1]
        m=listaGenerador[2]
        xn=x0

    if funcion == "uniforme":
        for _ in range(N):
            numerosGenerados.append(uniforme(listaFuncion))
    if funcion == "exponencial":
        for _ in range(N):
            numerosGenerados.append(exponencial(listaFuncion))
    if funcion == "normal":
        for _ in range(N):
            numerosGenerados.append(normal(listaFuncion))
    if funcion == "poisson":
        for _ in range(N):
            numerosGenerados.append(poisson(listaFuncion))
    if funcion == "binomial":
        for _ in range(N):
            numerosGenerados.append(binomial(listaFuncion))

    histograma(M,numerosGenerados)
    return numerosGenerados

def uniforme(listaFuncion):
    a=listaFuncion[0]
    b=listaFuncion[1]
    x=generadores()

    return(x*(b-a))+a


def exponencial(listaFuncion):
    #TODO
    x=listaFuncion[0]
    m=listaFuncion[1]
    random=generadores()
    exp=(-1/m)*math.log(random)
    return exp

def normal(listaFuncion):
    m=listaFuncion[1]
    sd=listaFuncion[0]
    u=0
    v=0

    u=generadores()
    v=generadores()
    print(u)
    x=math.sqrt( -2.0 * math.log( u ) ) * math.cos( 2.0 * math.pi * v )
    return x*sd-(-1*m)

def poisson(listaFuncion):
    n=0
    p=1
    r=0
    limit=math.e**-listaFuncion[0]
    while True:
        r=generadores()
        p=p*r
        if p<limit:
            return n
        else:
            n+=1

def binomial(listaFuncion):
    n=listaFuncion[1]
    p=listaFuncion[0]
    m=int((n+1)*p)
    while True:
        k=int(generadores()*n)
        x=np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k))*(p**k)*((1-p)**(n-k))
        x=x/m
        r=generadores()
        if r < x:
            return k

def histograma(M,numerosGenerados):
    plt.hist(numerosGenerados,M)
    plt.show()

def generadores():
    global xn
    if tipo=="mixto":
        xn= (((a*xn)+c) % m)
        return xn/m

    if tipo=="multiplicativo":
        xn= ((a*xn) % m)
        return xn/m
