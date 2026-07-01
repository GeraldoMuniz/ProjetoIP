import pygame
#OK
paredes_banheiro = [
    # Paredes e limites externos
    pygame.Rect(0, 0, 1672, 65),
    pygame.Rect(0, 65, 30, 876),
    pygame.Rect(1642, 65, 30, 876),
    pygame.Rect(30, 755, 715, 40),
    pygame.Rect(925, 755, 717, 40),
    pygame.Rect (1500, 215, 180, 120),
    # Cabines de privadas superiores
    pygame.Rect(50, 65, 580, 310),

    # Mictórios
    pygame.Rect(580, 65, 390, 220),

    # Chuveiros e banco
    pygame.Rect(1075, 65, 250, 270),
    pygame.Rect(1360, 215, 180, 50),

    # Cabines de privadas inferiores
    pygame.Rect(1160, 430, 482, 340),

    # Bancada das pias
    pygame.Rect(90, 630, 430, 115),

    # Plantas e lixeira
    pygame.Rect(40, 650, 70, 105),
    pygame.Rect(1100, 500, 60, 140),
    pygame.Rect(620, 170, 65, 110),
    pygame.Rect(520, 690, 50, 65),
]