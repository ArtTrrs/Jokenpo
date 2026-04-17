# biblioteca

import random

# status inicial das variavies de jogo

jogo = False
revanche = True
calculo = True
revancheInput = ""
mdx = 0

# input de modo

modo = input("Selecione a forma de jogo:\n1 - Jogador contra jogador\n2 - Jogador contra Máquina;\n3 - Máquina contra Máquina;\nModo:")

# verificador de modo e duração de rounds desejada

if modo in "123":
    jogo = True
    inputmdx = int(input("Escolha até quantos pontos a partida irá:\n1 - Jogo Único;\n3 - Melhor de 3;\n5 - Melhor de 5;\n7 - Melhor de 7;\nDuração:"))
    if str(inputmdx) in "1357":
        mdx = inputmdx
    else:
        print("Entrada não corresponde a uma duração de jogo!")
else:
    jogo = False
    print("Entrada não corresponde a um modo de jogo!")

# variáveis de cálculo

pontosP1 = 0
pontosP2 = 0
maxponto = mdx//2 + 1

# definição de nomes

if jogo:
    if modo == "1":
        nomeP1 = input("\nPrimeiro jogador, escolhe seu nome:")
        nomeP2 = input("Segundo jogador, escohle seu nome:")
    elif modo == "2":
        nomeP1 = input("\nPrimeiro jogador, escolhe seu nome:")
        nomeP2 = random.randint(1,4)
        if nomeP2 == 1:
            nomeP2 = "GePeTô"
        elif nomeP2 == 2:
            nomeP2 = "Bob"
        elif nomeP2 == 3:
            nomeP2 = "Homo Ludens"
        elif nomeP2 == 4:
            nomeP2 = "Clanker"
        print("Jogador 2 é " + nomeP2 + "\n")
    elif modo == "3":
        nomeP1 = random.randint(1,4)
        if nomeP1 == 1:
            nomeP1 = "GePeTô"
        elif nomeP1 == 2:
            nomeP1 = "Bob"
        elif nomeP1 == 3:
            nomeP1 = "Homo Ludens"
        elif nomeP1 == 4:
            nomeP1 = "Clanker"
        print("\nJogador 1 é " + nomeP1)
        nomeP2 = random.randint(1,4)
        if nomeP2 == 1:
            nomeP2 = "GePeTô"
        elif nomeP2 == 2:
            nomeP2 = "Bob"
        elif nomeP2 == 3:
            nomeP2 = "Homo Ludens"
        elif nomeP2 == 4:
            nomeP2 = "Clanker"
        print("Jogador 2 é " + nomeP2 + "\n")
        

# loop principal de jogo

while revanche:

    # reatribuição estado inicial para cálculo

    pontosP1 = 0
    pontosP2 = 0
    revancheInput = ""
    rodada = 1

    # loop de detecção de vitória

    while pontosP1 < maxponto and pontosP2 < maxponto and calculo == True:

        # definição de modo, jogada e respectivo nome

        if modo == "1":
            jogadaP1 = int(input(nomeP1 + ", escolha sua jogada: \n (não deixe seu oponente ver sua escolha!) \n 1 - Pedra; \n 2 - Papel; \n 3 - Tesoura;\n"))
            jogadaP2 = int(input(nomeP2 + ", escolha sua jogada: \n (não deixe seu oponente ver sua escolha!) \n 1 - Pedra; \n 2 - Papel; \n 3 - Tesoura;\n"))
        elif modo == "2":
            start = input("Simular rodada n°" + str(rodada)  + " entre " + nomeP1  + " e " + nomeP2  + "?\n1 - Sim;\n2 - Não (reiniciar código);")
            if start == "1":
                rodada += 1
                jogadaP1 = int(input(nomeP1 + ", escolha sua jogada: \n 1 - Pedra; \n 2 - Papel; \n 3 - Tesoura;\n"))
                jogadaP2 = random.randint(1,3)
                if jogadaP2 == 1:
                    jogada2nome = "Pedra"
                elif jogadaP2 == 2:
                    jogada2nome = "Papel"
                elif jogadaP2 == 3:
                    jogada2nome = "Tesoura"
                print(nomeP2 + "escolhe" + jogada2nome + "\n")
            else:
                print("Fim da simulação, para testar outros modos e jogar novamente reinicie o programa.")
        elif modo == "3":
            start = input("Simular rodada n°" + str(rodada)  + " entre " + nomeP1  + " e " + nomeP2  + "?\n1 - Sim;\n2 - Não (reiniciar código);")
            if start == "1":
                rodada += 1
                jogadaP1 = random.randint(1,3)
                jogadaP2 = random.randint(1,3)
                if jogadaP1 == 1:
                    jogada1nome = "Pedra"
                elif jogadaP1 == 2:
                    jogada1nome = "Papel"
                elif jogadaP1 == 3:
                    jogada1nome = "Tesoura"
                if jogadaP2 == 1:
                    jogada2nome = "Pedra"
                elif jogadaP2 == 2:
                    jogada2nome = "Papel"
                elif jogadaP2 == 3:
                    jogada2nome = "Tesoura"
                print("\n" + nomeP1 + " escolhe " + jogada1nome)
                print(nomeP2 + " escolhe " + jogada2nome + "\n")
                calculo = True
            else:
                print("Fim da simulação, para testar outros modos e jogar novamente reinicie o programa.")
                calculo = False

        # cálculo e output de jogada

        if calculo == True:
            if jogadaP1 == jogadaP2:
                print("Empate! " + nomeP1 + " e " + nomeP2 + " escolheram " + jogada1nome + ". Tentem novamente!\nPontuação " + nomeP1 + ": " + str(pontosP1) + "\nPontuação " + nomeP2 + ": " + str(pontosP2) + "\n")
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
                        objvitoria = jogada1nome
                        objderrota = jogada2nome
                    elif jogadaP2 > jogadaP1:
                        vencedor = nomeP2
                        pontosP2 += 1
                        objvitoria = jogada2nome
                        objderrota = jogada1nome
                vitoria = random.randint(1,5)        
                if vitoria == 1:
                    vitoria = " vence "
                elif vitoria == 2:
                    vitoria = " humilha "
                elif vitoria == 3:
                    vitoria = " oblitera "
                elif vitoria == 4:
                    vitoria = " triunfa perante "
                elif vitoria == 5:
                    vitoria = " destrói "
                print(objvitoria + vitoria + objderrota + ", " + vencedor + " recebe um ponto!\nPontuação " + nomeP1 + ": " + str(pontosP1) + "\nPontuação " + nomeP2 + ": " + str(pontosP2) + "\n")

        # detecção e mensagem de fim de jogo

        if pontosP1 == maxponto or pontosP2 == maxponto:
            if pontosP1 == maxponto:
                print("Parabéns " + nomeP1 + ", você venceu!!!\nPontuação Final: " + nomeP1 + ": " + str(pontosP1) + "\nPontuação Final: " + nomeP2 + ": " + str(pontosP2) + "\n")
                while revancheInput != "1" and revancheInput!= "2":                
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
                while revancheInput != "1" and revancheInput!= "2":
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
