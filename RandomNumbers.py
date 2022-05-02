
def generaAleatorios(generador,listaGenerador,funcion,listaFuncion,N,M):
    numerosGenerados=[]
    if funcion == "uniforme":
        numerosGenerados.append(uniforme(listaFuncion))
    if funcion == "exponencial":
        numerosGenerados.append(exponencial(listaFuncion))
    if funcion == "normal":
        numerosGenerados.append(normal(listaFuncion))
    if funcion == "poisson":
        numerosGenerados.append(poisson(listaFuncion))
    if funcion == "binomial":
        numerosGenerados.append(binomial(listaFuncion))
    
    histograma(M,numerosGenerados)
    return numerosGenerados


def uniforme(listaFuncion):
    #TODO
    pass

def exponencial(listaFuncion):
    #TODO
    pass

def normal(listaFuncion):
    #TODO
    pass

def poisson(listaFuncion):
    #TODO
    pass

def binomial(listaFuncion):
    #TODO
    pass

def histograma(M,numerosGenerados):
    #TODO
    pass