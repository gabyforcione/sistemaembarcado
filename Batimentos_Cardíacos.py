# Sistema de Batimentos Cardíacos
import random
import time

def Checar_Batimentos():
    while True:
        batimentos = random.uniform(50, 180)
        if batimentos >= 120:
          print("Os batimentos estão em ",int(batimentos),"; estão muito rápidos, marcapasso ativado.")
        elif batimentos < 60:
          print("Os batimentos estão em ",int(batimentos),"; estão muito lentos, marcapasso ativado.")
        elif batimentos == 50:
          print("Sinto muito, mas você não resistiu...")
        elif batimentos == 180:
          print("Sinto muito, mas você não resistiu...")
        else:
          print("Tudo normal com seus batimentos, estão em ",int(batimentos),".")
        time.sleep(5)

Checar_Batimentos()