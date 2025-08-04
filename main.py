"""
Shayane KATCHERA
Bird of Prey Main file
"""

import numpy as np
import pygame

# ===== parametres globaux =====
# l'ecran
WIDTH = 800
HEIGHT = 600

# ===== parametres de la simulation =====

# ===== partie principale =====
# classes

# fonctions
def main():
   # reset de l'ecran

   # affichage

   # mise a jour de l'ecran
   pygame.display.flip()

# ===== frontend =====
# creation de la fenetre
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

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