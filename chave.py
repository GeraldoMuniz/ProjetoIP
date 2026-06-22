import pygame
tamanho = 20
cor = (255, 215, 0)
lista_chaves = [

    {
        "nome": "Chave Azul",
        "x": 300,
        "y": 200,
        "pegou": False
    },

    {
        "nome": "Chave Vermelha",
        "x": 1500,
        "y": 850,
        "pegou": False
    },

    {
        "nome": "Chave Mestre",
        "x": 1200,
        "y": 700,
        "pegou": False
    }

]

def desenhar_chaves(tela):
    for chave in lista_chaves:
        if chave["pegou"] == False:
            pygame.draw.rect(
                tela,
                cor,
                (chave["x"], chave["y"], tamanho, tamanho)
            )
