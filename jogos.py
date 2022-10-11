import adivinhacao
import forca

def escolher_jogo():
    print("*********************************")
    print("*********Escolher o jogo!********")
    print("*********************************")

    print("Seleção de jogos")
    print("(1) Adivinhação (2) Forca")

    jogo = int(input("Escolha o jogo: "))

    if(jogo == 1):
        print("Jogando adivinhacao")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolher_jogo()
