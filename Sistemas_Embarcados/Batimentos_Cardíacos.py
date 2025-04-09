# Sistema de Batimentos Cardíacos
import random
import time

def Checar_Batimentos():
# Esta função deve checar os batimentos cardíacos a cada 5 segundos; de acordo com minhas pesquisas, eu coloquei como se
# os batimentos estiverem maiores ou iguais a 120, apresenta sinal de perigo; menores que 60, apresenta sinal de perigo;
# se estiverem igual a 50 ou 180, você morreu; e se não for nenhum desses (estiver entre 61 e 119), está tudo normal.
# Também, quando há sinal de perigo ele mostra que o marcapasso foi ativado.

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