import pygame
#define onde spawnar o boneco
x, y = 400, 300
#quanto ele vai andar
velocidade = 1
#tamanho dele
tamanho = 40
#função de locomoção
def movimento ():
    global x, y

    teclas = pygame.key.get_pressed ()

    if (teclas [pygame.K_LEFT] or teclas [pygame.K_a]):
        x -= velocidade
    elif (teclas [pygame.K_RIGHT] or teclas [pygame.K_d]):
        x += velocidade
    elif (teclas [pygame.K_UP] or teclas [pygame.K_w]):
        y -= velocidade
    elif (teclas [pygame.K_DOWN] or teclas [pygame.K_s]):
        y += velocidade
#checa se não vai ultrapassar o limite do mapa e deixa ele totalmente visível
    if (x < 0):
        x = 0
    elif (x > 800 - tamanho):
        x = 800 - tamanho

    elif (y < 0):
        y = 0
    elif (y > 600 - tamanho):
        y = 600 - tamanho