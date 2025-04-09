import random
import time

# Definindo o número máximo de plantas que podem ser acomodadas na estufa
volume_maximo = 10  # volume máximo de plantas
volume_atual = 0

def adicionar_planta(volume_atual):
    """Simula a adição de uma planta na estufa."""
    if volume_atual < volume_maximo:
        volume_atual += 1
        print(f"Planta adicionada. Volume atual: {volume_atual}/{volume_maximo}")
    else:
        print("Estufa cheia! Não é possível adicionar mais plantas.")
    return volume_atual

def remover_planta(volume_atual):
    """Simula a remoção de uma planta da estufa."""
    if volume_atual > 0:
        volume_atual -= 1
        print(f"Planta removida. Volume atual: {volume_atual}/{volume_maximo}")
    else:
        print("Não há plantas na estufa para remover.")
    return volume_atual

def controlar_estufa(volume_atual):
    """Simula o controle de adição e remoção de plantas na estufa."""
    while True:
        # Gera um número aleatório entre 1 e 2
        movimento = random.randint(1, 2)

        if movimento == 1:  # 1 representa a adição de uma planta
            volume_atual = adicionar_planta(volume_atual)
        elif movimento == 2:  # 2 representa a remoção de uma planta
            volume_atual = remover_planta(volume_atual)

        # Intervalo de 1 a 3 segundos entre os movimentos
        time.sleep(random.randint(1, 3))

# Inicia o controle da estufa com o volume inicial de 0 plantas
controlar_estufa(volume_atual)
