# Sistema de Batimentos Cardíacos
import random
import time

def Checar_Batimentos():
    while True:
        batimentos = random.uniform(0, 50)
        if batimentos >= 25:
          print("Os batimentos estão em ",int(batimentos),"; estão muito rápidos, tome cuidado.")
        elif batimentos <= 10:
          print("Os batimentos estão em ",int(batimentos),"; estão muito lentos, tome cuidado.")
        elif batimentos == 0:
          print("Sinto muito, mas você não resistiu...")
        else:
          print("Tudo normal com seus batimentos, estão em ",int(batimentos),".")
        time.sleep(5)

Checar_Batimentos()