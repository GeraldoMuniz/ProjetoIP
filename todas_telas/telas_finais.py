import pygame

tela_derrota = pygame.image.load(
    "imagem/tela_derrota.png"
).convert()

#retangulo do tente novamente
botao_reiniciar = pygame.Rect(500,657,666,142)

def mostrar_derrota(tela):

    tela.blit(tela_derrota, (0, 0))
    pygame.display.flip()

    while True:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if botao_reiniciar.collidepoint(evento.pos):
                    return "reiniciar"
