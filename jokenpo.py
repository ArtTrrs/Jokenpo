# biblioteca de randoização

import random

# input de modo

modo = input("Selecione a forma de jogo:\n1 - Jogador contra jogador\n2 - Jogador contra Máquina;\n3 - Máquina contra Máquina;\nModo:")

# status inicial de jogo e máximo de rounds

jogo = False
revanche = True
calculo = True
revancheInput = ""
mdx = 0

# verificador de modo e duração de rounds desejada 

if modo in "123":
    jogo = True
    inputmdx = int(input("Escolha até quantos pontos a partida irá:\n1 - Jogo Único;\n3 - Melhor de 3;\n5 - Melhor de 5;\n7 - Melhor de 7;\nDuração:"))
    if inputmdx in [1,3,5,7]:
        mdx = inputmdx
    else:
        print("Entrada não corresponde a uma duração de jogo!")
else:
    jogo = False
    print("Entrada não corresponde a um modo de jogo!")

# variáveis de jogo

pontosP1 = 0
pontosP2 = 0
maxponto = mdx//2 + 1
nomesBOT = ['GePeto','Clanker','Bob','Homo Ludens']
vitorias = [' oblitera ',' destrói ',' triunfa perante ',' humilha ',' vence ']
dicionariojogadas = {
    "1": "Pedra",
    "2": "Papel",
    "3": "Tesoura"
}

# definição de nomes

if jogo:
    if modo == "1":
        nomeP1 = input("\nPrimeiro jogador, escolhe seu nome:")
        nomeP2 = input("Segundo jogador, escohle seu nome:")
    elif modo == "2":
        nomeP1 = input("\nPrimeiro jogador, escolhe seu nome:")
        nomeP2 = random.choice(nomesBOT)
        print("Jogador 2 é " + nomeP2 + "\n")
    elif modo == "3":
        nomeP1 = random.choice(nomesBOT)
        print("\nJogador 1 é " + nomeP1)
        nomesBOT.remove(nomeP1)
        nomeP2 = random.choice(nomesBOT)
        print("Jogador 2 é " + nomeP2 + "\n")
        nomesBOT.append(nomeP1)

# detecção de vitória e repetição de rodadas

while revanche:
    pontosP1 = 0
    pontosP2 = 0
    revancheInput = ""
    rodada = 1
    while pontosP1 < maxponto and pontosP2 < maxponto and calculo == True:

        # atribuição de jogada por modo

        if modo == "1":
            jogadaP1 = int(input(nomeP1 + ", escolha sua jogada: \n (não deixe seu oponente ver sua escolha!) \n 1 - Pedra; \n 2 - Papel; \n 3 - Tesoura;\n"))
            jogadaP2 = int(input(nomeP2 + ", escolha sua jogada: \n (não deixe seu oponente ver sua escolha!) \n 1 - Pedra; \n 2 - Papel; \n 3 - Tesoura;\n"))
        elif modo == "2":
            start = input("Simular rodada n°" + str(rodada)  + " entre " + nomeP1  + " e " + nomeP2  + "?\n1 - Sim;\n2 - Não (reiniciar código);")
            if start == "1":
                rodada += 1
                jogadaP1 = int(input(nomeP1 + ", escolha sua jogada: \n 1 - Pedra; \n 2 - Papel; \n 3 - Tesoura;\n"))
                jogadaP2 = random.randint(1,3)
                print(nomeP2 + "escolhe" + dicionariojogadas[str(jogadaP2)] + "\n")
            else:
                print("Fim da simulação, para testar outros modos e jogar novamente reinicie o programa.")
        elif modo == "3":
            start = input("Simular rodada n°" + str(rodada)  + " entre " + nomeP1  + " e " + nomeP2  + "?\n1 - Sim;\n2 - Não (reiniciar código);")
            if start == "1":
                rodada += 1
                jogadaP1 = random.randint(1,3)
                jogadaP2 = random.randint(1,3)
                print("\n" + nomeP1 + " escolhe " + dicionariojogadas[str(jogadaP1)])
                print(nomeP2 + " escolhe " + dicionariojogadas[str(jogadaP2)] + "\n")
                calculo = True
            else:
                print("Fim da simulação, para testar outros modos e jogar novamente reinicie o programa.")
                calculo = False

        # cálculo e output, em texto e pontuação, de jogada

        if calculo == True:
            if jogadaP1 == jogadaP2:
                print("Empate! " + nomeP1 + " e " + nomeP2 + " escolheram " + dicionariojogadas[str(jogadaP1)] + ". Tentem novamente!\nPontuação " + nomeP1 + ": " + str(pontosP1) + "\nPontuação " + nomeP2 + ": " + str(pontosP2) + "\n")
            elif jogadaP1 != jogadaP2:
                if jogadaP1 + jogadaP2 == 4:
                    objvitoria = "Pedra"
                    objderrota = "Tesoura"
                    if jogadaP1 == 1:
                        vencedor = nomeP1
                        pontosP1 += 1
                    else:
                        vencedor = nomeP2
                        pontosP2 += 1
                else:
                    if jogadaP1 > jogadaP2:
                        vencedor = nomeP1
                        pontosP1 += 1
                        objvitoria = dicionariojogadas[str(jogadaP1)]
                        objderrota = dicionariojogadas[str(jogadaP2)]
                    elif jogadaP2 > jogadaP1:
                        vencedor = nomeP2
                        pontosP2 += 1
                        objvitoria = dicionariojogadas[str(jogadaP2)]
                        objderrota = dicionariojogadas[str(jogadaP1)]
                print(objvitoria + random.choice(vitorias) + objderrota + ", " + vencedor + " recebe um ponto!\nPontuação " + nomeP1 + ": " + str(pontosP1) + "\nPontuação " + nomeP2 + ": " + str(pontosP2) + "\n")

        # detecção e mensagem de fim de jogo

        if pontosP1 == maxponto or pontosP2 == maxponto:
            if pontosP1 == maxponto:
                print("Parabéns " + nomeP1 + ", você venceu!!!\nPontuação Final: " + nomeP1 + ": " + str(pontosP1) + "\nPontuação Final: " + nomeP2 + ": " + str(pontosP2) + "\n")
                while revancheInput not in ["1","2"]:
                    revancheInput = input("Desejam jogar uma revanche?\n1 - Sim;\n2 - Não;\n")
                    if revancheInput == "1":
                        revanche = True
                        break
                    elif revancheInput == "2":
                        revanche = False
                        break
                    else:
                        print("Entrada não corresponde a uma opção válida!")
            elif pontosP2 == maxponto:
                print("Parabéns " + nomeP2 + ", você venceu!!!\nPontuação Final: " + nomeP1 + ": " + str(pontosP1) + "\nPontuação Final: " + nomeP2 + ": " + str(pontosP2) + "\n")
                while revancheInput not in ["1","2"]:
                    revancheInput = input("Desejam jogar uma revanche?\n1 - Sim;\n2 - Não;\n")
                    if revancheInput == "1":
                        revanche = True
                        break
                    elif revancheInput == "2":
                        revanche = False
                        break
                    else:
                        print("Entrada não corresponde a uma opção válida!")

print("Fim de jogo, para testar outros modos e jogar novamente reinicie o programa.")