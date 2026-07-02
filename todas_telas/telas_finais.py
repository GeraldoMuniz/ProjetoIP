import pygame


tela_derrota = pygame.image.load(
    "imagem/tela_derrota.png"
).convert()


def mostrar_derrota(tela):

    tela.blit(tela_derrota, (0, 0))
    pygame.display.flip()

    esperando = True

    while esperando:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN:
                esperando = False
