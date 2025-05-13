import time

def adivinhar_numero():
    print("Pense em um número entre 1 e 1000, e eu vou tentar adivinhar!")
    time.sleep(1)
    
    baixo = 1
    alto = 1000
    tentativas = 1

    while baixo <= alto:
        tentativas += 1
        meio = (baixo + alto) // 2
        resposta = input(f"É o número {meio}? (Digite 'maior', 'menor', ou 'correto'): ").strip().lower()

        if resposta == "correto":
            print(f"Eu adivinhei seu número em {tentativas} tentativas! O número era {meio}.")
            break
        elif resposta == "maior":
            baixo = meio + 1
        elif resposta == "menor":
            alto = meio - 1
        else:
            print("Resposta inválida. Por favor, digite 'maior', 'menor', ou 'correto'.")
            
        time.sleep(1)