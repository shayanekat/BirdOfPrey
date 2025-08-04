"""
Shayane KATCHERA
Bird of Prey Main file
"""

import numpy as np
import pygame

# l'ecran
WIDTH = 800
HEIGHT = 600

# creation de la fenetre
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# fonctions
def main():
    """ Boucle de jeu """
    # reset de l'ecran
    screen.fill((0, 0, 0))

    # affichage

    # mise a jour de l'ecran
    pygame.display.flip()

# boucle principale
running = True
while running:
    main()

    # gestion des evenements
    for event in pygame.event.get():
        # quitter
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.QUIT):
            running = False

    pygame.display.flip()