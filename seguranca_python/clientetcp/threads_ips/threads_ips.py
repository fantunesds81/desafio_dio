from threading import Thread
import time 



def carro1(velicidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print('carro1: ', piloto,  trajeto)
        trajeto += velicidade
        time.sleep(0.5)
        

def carro2(velicidade):
    trajeto = 0
    while trajeto <= 100:
        print('carro2: ', trajeto)
        trajeto += velicidade



t_carro1 = Thread(target=carro1, args=[1])
t_carro2 = Thread(target=carro2, args=[1.5])

t_carro1.start()
t_carro2.start()
