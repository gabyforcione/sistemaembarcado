import random
import time

# Definindo o número máximo de vagas no estacionamento
vagas_maximas = 50
vagas_ocupadas = 0

def entrada_veiculo(vagas_ocupadas):
    """Simula a entrada de um veículo no estacionamento."""
    if vagas_ocupadas < vagas_maximas:
        vagas_ocupadas += 1
        print(f"Veículo entrou. Vagas ocupadas: {vagas_ocupadas}/{vagas_maximas}")
    else:
        print("Estacionamento cheio! Nenhuma vaga disponível.")
    return vagas_ocupadas

def saida_veiculo(vagas_ocupadas):
    """Simula a saída de um veículo do estacionamento."""
    if vagas_ocupadas > 0:
        vagas_ocupadas -= 1
        print(f"Veículo saiu. Vagas ocupadas: {vagas_ocupadas}/{vagas_maximas}")
    else:
        print("Não há veículos no estacionamento.")
    return vagas_ocupadas

def simular_movimento(vagas_ocupadas):
    """Simula aleatoriamente a entrada e saída de veículos."""
    while True:
        # Gera um número aleatório entre 1 e 2
        movimento = random.randint(1, 2)

        if movimento == 1:  # 1 representa a entrada
            vagas_ocupadas = entrada_veiculo(vagas_ocupadas)
        elif movimento == 2:  # 2 representa a saída
            vagas_ocupadas = saida_veiculo(vagas_ocupadas)

        # Intervalo de 1 a 3 segundos entre os movimentos
        time.sleep(random.randint(1, 3))

# Simula o movimento de veículos
simular_movimento(vagas_ocupadas)
