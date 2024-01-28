#IMPORTAÇÕES
import pygame
from pygame.locals import *
from sys import exit
from random import randint


#INICIALIZANDO O PYGAME
pygame.init()


#VÍDEO
'''CONFIGURAÇÕES DE TELA:'''
Largura = 640
Altura = 480
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Snake Game')


#ÁUDIO
'''CONFIGURAÇÕES DE SOM:'''
Som_Pontuação = pygame.mixer.Sound('Fireball.wav')
Som_Pontuação.set_volume(1)


#JOGO
'''CONFIGURAÇÕES DO JOGO:'''
Fim_de_Jogo = False
Dificuldade = 7
Pontos = 0
Maior_Pontuação = 0
Fonte01 = pygame.font.SysFont('arial', 22, True, False)
Comprimento_Inicial = 3
Lista_Cobra = []

'''POSIÇÕES ALEATÓRIAS DA MAÇÃ:'''
X_Maçã = randint(15, 627)
Y_Maçã = randint(15, 467)

'''POSIÇÃO INICIAL DA COBRA:'''
X_Cobra = Largura//2
Y_Cobra = Altura//2
X_Controle = 20
Y_Controle = 0

'''DEFININDO COMO A COBRA DEVERÁ CRESCER:'''
def Aumenta_Cobra(Lista_Cobra):
    for XeY in Lista_Cobra:
        pygame.draw.rect(Tela, (0, 180, 0), (XeY[0], XeY[1], 20, 20))

'''LAÇO DE REPETIÇÃO PARA MANTER A TELA DO JOGO ABERTA:'''
while True:
    '''DEFININDO VELOCIDADE DO JOGO:'''
    Velocidade_do_Jogo = pygame.time.Clock()
    Velocidade_do_Jogo.tick(Dificuldade)

    '''DEFININDO COR DE FUNDO:'''
    Tela.fill((167, 167, 167))

    '''CONDIÇÃO PARA ARMAZENAR A MAIOR PONTUAÇÃO:'''
    if Pontos > Maior_Pontuação:
        Maior_Pontuação = Pontos

    '''EXIBINDO "PONTOS" NA TELA:'''
    Mensagem = f'Escore: {Pontos} / Maior Pontuação: {Maior_Pontuação}'

    '''DEFININDO A FORMATAÇÃO DE "PONTOS" NA TELA:'''
    Texto = Fonte01.render(Mensagem, True, (0, 60, 255))

    '''DEFININDO A POSIÇÃO DE "PONTOS" NA TELA:'''
    Tela.blit(Texto, (10, 10))
    
    '''DEFININDO COR, LARGURA E ALTURA DOS ELEMENTOS PRINCIPAIS:'''
    Cobra = pygame.draw.rect(Tela, (0, 180, 0), (X_Cobra, Y_Cobra, 20, 20))
    Maçã = pygame.draw.rect(Tela, (255, 0, 0), (X_Maçã, Y_Maçã, 15, 15))

    '''CONDIÇÃO CASO A COBRA COMA A MAÇÃ:'''
    if Cobra.colliderect(Maçã):
        X_Maçã = randint(15, 627)
        Y_Maçã = randint(15, 467)
        Pontos = Pontos + 1
        Som_Pontuação.play()
        Dificuldade = Dificuldade + 0.3
        Comprimento_Inicial = Comprimento_Inicial + 1
    Lista_Cabeça = []
    Lista_Cabeça.append(X_Cobra)
    Lista_Cabeça.append(Y_Cobra)
    Lista_Cobra.append(Lista_Cabeça)
    if len(Lista_Cobra) > Comprimento_Inicial:
        del Lista_Cobra[0]
    Aumenta_Cobra(Lista_Cobra)

    '''CONDIÇÃO CASO A COBRA MORDA ELA MESMO OU BATA CONTRA A PAREDE:'''
    if Lista_Cobra.count(Lista_Cabeça) > 1 or X_Cobra > Largura or X_Cobra < 0 or Y_Cobra < 0 or Y_Cobra > Altura:
        Fonte02 = pygame.font.SysFont('arial', 20, True, False)
        Mensagem = f'Maior Pontuação: {Maior_Pontuação}. Pressione [R] para recomeçar'
        Texto = Fonte02.render(Mensagem, True, (167, 167, 167))
        Centralizar = Texto.get_rect()
        Fim_de_Jogo = True

        '''CONFIGURAÇÕES DE FIM DE JOGO:'''
        while Fim_de_Jogo:
            Tela.fill((0, 60, 255))
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        Reiniciar()

            '''DEFININDO POSIÇÃO DA MENSAGEM DE FIM DE JOGO:'''
            Centralizar.center = (Largura//2, Altura//2)
            Tela.blit(Texto, Centralizar)
            pygame.display.update()
        
    '''DEFININDO COMO O JOGO DEVERÁ RECOMEÇAR:'''
    def Reiniciar():
        global Pontos, Dificuldade, Comprimento_Inicial, X_Cobra, Y_Cobra, Lista_Cobra, Lista_Cabeça, X_Maçã, Y_Maçã, Fim_de_Jogo
        Fim_de_Jogo = False
        Pontos = 0
        Dificuldade = 7
        Comprimento_Inicial = 3
        X_Cobra = Largura//2
        Y_Cobra = Altura//2
        Lista_Cobra = []
        Lista_Cabeça = []
        X_Maçã = randint(15, 627)
        Y_Maçã = randint(15, 467)
    pygame.display.update()


    #CONTROLES
    '''CONFIGURAÇÕES DE CONTROLE DO JOGO:
    OBSERVAÇÃO: O COMANDO "PASS" BLOQUEIA A TECLA OPOSTA.'''
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                if Y_Controle == 20:
                    pass
                else:
                    Y_Controle = -20
                    X_Controle = 0

            if event.key == K_s or event.key == K_DOWN:
                if Y_Controle == -20:
                    pass
                else:
                    Y_Controle = 20
                    X_Controle = 0

            if event.key == K_a or event.key == K_LEFT:
                if X_Controle == 20:
                    pass
                else:
                    X_Controle = -20
                    Y_Controle = 0

            if event.key == K_d or event.key == K_RIGHT:
                if X_Controle == -20:
                    pass
                else:
                    X_Controle = 20
                    Y_Controle = 0
    X_Cobra = X_Cobra + X_Controle
    Y_Cobra = Y_Cobra + Y_Controle
