# bibliotecas

import random
import pygame
import sys

# pygame start e definições estéticas

pygame.init()
tela = pygame.display.set_mode((1080, 720))
fundocor = [50,200,200]
aba = "inicio"

# fontes e cores

fonte = pygame.font.Font(None, 50)
textocor = [255,255,255]
titulofonte = pygame.font.Font(None, 100)
titulocor = [0,0,0]

# cores botão - [R, G, B]

botaocorstorage = [200,20,20]
botao1cor = botaocorstorage
botao2cor = botaocorstorage
botao3cor = botaocorstorage
botao4cor = botaocorstorage
botao5cor = botaocorstorage
botao6cor = botaocorstorage
botao7cor = botaocorstorage
botao8cor = botaocorstorage
botao9cor = botaocorstorage
botaocorhover = [250,50,50]

# retângulos - (x, y, tamanho x, tamanho y)

tituloborda = pygame.Rect(270, 100, 540, 110)
botao1 = pygame.Rect(440, 300, 200, 80)
botao2 = pygame.Rect(440, 450, 200, 80)
botao3 = pygame.Rect(440, 600, 200, 80)

botao4 = pygame.Rect(110, 400, 200, 80)
botao5 = pygame.Rect(440, 400, 200, 80)
botao6 = pygame.Rect(770, 400, 200, 80)

botao7 = pygame.Rect(440, 300, 200, 80)
botao8 = pygame.Rect(440, 450, 200, 80)
botao9 = pygame.Rect(440, 600, 200, 80)

# textos

titulo1 = titulofonte.render("Jo-ken-po!", True, titulocor)
texto1 = fonte.render("Jogar", True, textocor)
texto2 = fonte.render("Opções", True, textocor)
texto3 = fonte.render("Sair", True, textocor)

titulo2 = titulofonte.render("Modo de Jogo:", True, titulocor)
texto4 = fonte.render("P v P", True, textocor)
texto5 = fonte.render("P v E", True, textocor)
texto6 = fonte.render("E v E", True, textocor)

titulo3 = titulofonte.render("Sobre:", True, titulocor)
texto7 = fonte.render("É um jogo normal de Jokenpo, o 'Pedra, Papel, Tesoura'. Tessoura vence Papel. Papel vence Pedra. Pedra vence Tesoura." , True, textocor)
texto8 = fonte.render("O jogo contém quatro nomes de BOT, são eles: -> GePeTô; -> Clanker; -> Homo Ludens; -> Bob;", True, textocor)
texto9 = fonte.render("Voltar", True, textocor)

# loop da interface

while True:

    # chamados de variaveis

    mousePos = pygame.mouse.get_pos()
    events = pygame.event.get()

    # loop de detecção de clique

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if aba == "inicio":
                    if botao1.collidepoint(event.pos):
                        aba = "jogar"
                    if botao2.collidepoint(event.pos):
                        aba = "sobre"
                    if botao3.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()                    
                elif aba == "jogar":
                    if botao9.collidepoint(event.pos):
                        aba = "inicio"
                elif aba == "sobre":
                    if botao9.collidepoint(event.pos):
                        aba = "inicio"

    # detecção de hover e troca de cor

    if botao1.collidepoint(mousePos):
        botao1cor = botaocorhover    
    else:
        botao1cor = botaocorstorage
    if botao2.collidepoint(mousePos):
        botao2cor = botaocorhover
    else:
        botao2cor = botaocorstorage
    if botao3.collidepoint(mousePos):
        botao3cor = botaocorhover
    else:
        botao3cor = botaocorstorage
    if botao4.collidepoint(mousePos):
        botao4cor = botaocorhover
    else:
        botao4cor = botaocorstorage
    if botao5.collidepoint(mousePos):
        botao5cor = botaocorhover
    else:
        botao5cor = botaocorstorage
    if botao6.collidepoint(mousePos):
        botao6cor = botaocorhover
    else:
        botao6cor = botaocorstorage
    if botao7.collidepoint(mousePos):
        botao7cor = botaocorhover
    else:
        botao7cor = botaocorstorage
    if botao8.collidepoint(mousePos):
        botao8cor = botaocorhover
    else:
        botao8cor = botaocorstorage
    if botao9.collidepoint(mousePos):
        botao9cor = botaocorhover
    else:
        botao9cor = botaocorstorage

    # troca e desenho de aba

    if aba == "inicio":
        tela.fill(fundocor)
        pygame.draw.rect(tela, botaocorstorage, tituloborda)
        pygame.draw.rect(tela, botao1cor, botao1)
        pygame.draw.rect(tela, botao2cor, botao2)
        pygame.draw.rect(tela, botao3cor, botao3)
        tela.blit(titulo1, (tituloborda.x + 90, tituloborda.y + 20 ))
        tela.blit(texto1, (botao1.x + 50, botao1.y + 23 ))
        tela.blit(texto2, (botao2.x + 40, botao2.y + 23 ))
        tela.blit(texto3, (botao3.x + 65, botao3.y + 23 ))
    elif aba == "jogar":
        tela.fill(fundocor)
        pygame.draw.rect(tela, botaocorstorage, tituloborda)
        pygame.draw.rect(tela, botao4cor, botao4)
        pygame.draw.rect(tela, botao5cor, botao5)
        pygame.draw.rect(tela, botao6cor, botao6)
        pygame.draw.rect(tela, botao9cor, botao9)
        tela.blit(titulo2, (tituloborda.x + 20, tituloborda.y + 20 ))
        tela.blit(texto4, (botao4.x + 50, botao4.y + 23 ))
        tela.blit(texto5, (botao5.x + 50, botao5.y + 23 ))
        tela.blit(texto6, (botao6.x + 50, botao6.y + 23 ))
        tela.blit(texto9, (botao9.x + 50, botao9.y + 23 ))
    elif aba == "sobre":
        tela.fill(fundocor)
        pygame.draw.rect(tela, botaocorstorage, tituloborda)
        pygame.draw.rect(tela, botao7cor, botao7)
        pygame.draw.rect(tela, botao8cor, botao8)
        pygame.draw.rect(tela, botao9cor, botao9)
        tela.blit(titulo3, (tituloborda.x + 165, tituloborda.y + 20 ))
        tela.blit(texto7, (botao7.x + 50, botao7.y + 23 ))
        tela.blit(texto8, (botao8.x + 40, botao8.y + 23 ))
        tela.blit(texto9, (botao9.x + 50, botao9.y + 23 ))

    pygame.display.update()

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
