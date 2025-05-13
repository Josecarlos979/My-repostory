import time

def contar_ate_um_milhao():
    for i in range(1000001):  # Inclui o número 1.000.000
        print(i)
        time.sleep(0.000005)  # 0,0005 segundos (ajustável para modificar a velocidade)

# Executa a função
contar_ate_um_milhao()

