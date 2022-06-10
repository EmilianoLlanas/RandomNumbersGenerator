from helpers import *

def getTime():
    return time.time() - start

def insertaCliente(entrada,listaEntrada,lock):
    global funcion, esperando

    wait=funcion[entrada](listaEntrada)
    time.sleep(wait)

    while getTime() < limit:
        lock.acquire()

        print(f'Nuevo cliente en la cola, tiempo:{getTime()}')
        esperando.append(Cliente(getTime()))

        lock.release()

        wait=funcion[entrada](listaEntrada)
        time.sleep(wait)


def atiendeCliente(salida,listaSalida,index,lock):
    global funcion, esperando, atendiendo, servidos

    while getTime() < limit:
        if atendiendo[index]==None:
            lock.acquire()
            if len(esperando) > 0 :
                print(f'atendiendo a cliente en caja {index}, tiempo:{getTime()}')

                atendiendo[index]=esperando[0]
                esperando.pop(0)
                atendiendo[index].servicio(getTime())

                lock.release()

                wait=funcion[salida](listaSalida)
                time.sleep(wait)

                if getTime() < limit:
                    lock.acquire()

                    atendiendo[index].salida(getTime())
                    servidos.append(atendiendo[index])
                    atendiendo[index]=None

                    lock.release()
            else:
                lock.release()


def simulaColas(entrada='uniforme',salida='uniforme',servidores=2,listaEntrada=[1,3],listaSalida=[3,4],tiempo=10):
    global limit,start,atendiendo

    l = threading.Lock()
    limit = tiempo

    cajas=[]

    entradas = threading.Thread(target=insertaCliente, args=(entrada,listaEntrada,l))

    for i in range(servidores):
        atendiendo.append(None)
        cajas.append(threading.Thread(target=atiendeCliente, args=(salida,listaSalida,i,l)))

    start=time.time()

    entradas.start()
    for caja in cajas:
        caja.start()

    for caja in cajas:
        caja.join()

    entradas.join()

simulaColas()

print(esperando)
print(atendiendo)
print(servidos)

for c in servidos:
    print(f'Llegada: {c.entrada}, Servicio:{c.servicio}, Salida:{c.salida}')
