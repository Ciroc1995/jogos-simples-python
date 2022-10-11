import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Dificuldades do jogo")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha a dificuldade: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        elif(maior):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto")
        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos

print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()