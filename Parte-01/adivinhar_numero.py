import random

num_aleatorio = random.randint(1, 10)
tentativas = 0

while True:
    try:
        palpite = int(input("Adivinhe o número aleatorio que foi gerado!\n"))
    except ValueError: 
        print("Caracter não aceito, informe um valor entre 1 e 10!\n")
        continue

    if not 1 <= palpite <= 10:
        print("Atenção: O valor deve estar entre 1 e 10!\n")
        continue

    tentativas += 1

    if palpite > num_aleatorio:
        print(f"O número é menor {palpite}")
    elif palpite < num_aleatorio:
        print(f"O número é maior que {palpite}")
    else:
        print(f"🎉 PARABÉNS! Você acertou o número {num_aleatorio} na tentativa número {tentativas}!")
        break
