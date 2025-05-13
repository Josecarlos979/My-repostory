import pygame # type: ignore
import random

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
largura_tela = 600
altura_tela = 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Catch the Falling Objects")

# Definir cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Definir fontes
fonte = pygame.font.SysFont(None, 36)



# Definir o jogador (cesta)
class Cesta:
    def __init__(self):
        self.largura = 100
        self.altura = 20
        self.x = largura_tela // 2 - self.largura // 2
        self.y = altura_tela - self.altura - 10
        self.velocidade = 10

    def mover(self, esquerda, direita):
        if esquerda and self.x > 0:
            self.x -= self.velocidade
        if direita and self.x < largura_tela - self.largura:
            self.x += self.velocidade

    def desenhar(self):
        pygame.draw.rect(tela, VERDE, (self.x, self.y, self.largura, self.altura))

# Definir o objeto que cai
class Objeto:
    def __init__(self):
        self.largura = 20
        self.altura = 20
        self.x = random.randint(0, largura_tela - self.largura)
        self.y = -self.altura
        self.velocidade = random.randint(5, 10)

    def cair(self):
        self.y += self.velocidade

    def desenhar(self):
        pygame.draw.rect(tela, AZUL, (self.x, self.y, self.largura, self.altura))

# Função para mostrar o placar
def mostrar_placar(pontos, vidas):
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, PRETO)
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, PRETO)
    tela.blit(texto_pontos, (10, 10))
    tela.blit(texto_vidas, (largura_tela - texto_vidas.get_width() - 10, 10))

# Função principal do jogo
def jogo():
    # Variáveis de controle
    cesta = Cesta()
    objetos = [Objeto()]
    pontos = 0
    vidas = 3
    clock = pygame.time.Clock()

    # Loop principal do jogo
    rodando = True
    while rodando:
        tela.fill(BRANCO)
        
        # Verificar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Obter teclas pressionadas
        teclas = pygame.key.get_pressed()
        esquerda = teclas[pygame.K_LEFT]
        direita = teclas[pygame.K_RIGHT]

        # Mover a cesta
        cesta.mover(esquerda, direita)

        # Atualizar objetos que caem
        for objeto in objetos:
            objeto.cair()
            objeto.desenhar()

            # Verificar se o objeto tocou a cesta
            if objeto.y + objeto.altura >= cesta.y and cesta.x < objeto.x < cesta.x + cesta.largura:
                pontos += 1
                objetos.remove(objeto)
                objetos.append(Objeto())  # Adicionar novo objeto

            # Verificar se o objeto caiu no chão
            elif objeto.y > altura_tela:
                vidas -= 1
                objetos.remove(objeto)
                objetos.append(Objeto())  # Adicionar novo objeto

        # Verificar fim de jogo
        if vidas <= 0:
            texto_fim = fonte.render("Game Over", True, VERMELHO)
            tela.blit(texto_fim, (largura_tela // 2 - texto_fim.get_width() // 2, altura_tela // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            rodando = False

        # Desenhar a cesta
        cesta.desenhar()

        # Mostrar o placar
        mostrar_placar(pontos, vidas)

        # Atualizar a tela
        pygame.display.update()

        # Controlar o FPS
        clock.tick(60)

    pygame.quit()

# 123 Iniciar o jogo
jogo()