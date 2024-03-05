# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 07:22:43 2024

@author: ROMEO_YOTA
"""

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Gestion de la souris")

# Police d'écriture
police = pygame.font.Font(None, 24)

# Boucle principale
while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            # Récupération des informations sur le clic de souris
            position_souris = pygame.mouse.get_pos()
            bouton_gauche, bouton_droit, bouton_milieu = pygame.mouse.get_pressed()

            # Affichage des informations dans la fenêtre
            texte_position = f"Position de la souris : {position_souris}"
            texte_clic = f"Clic gauche : {bouton_gauche} | Clic droit : {bouton_droit}"

            fenetre.fill((0, 0, 0))  # Efface l'écran
            fenetre.blit(police.render(texte_position, True, (255, 255, 255)), (10, 10))
            fenetre.blit(police.render(texte_clic, True, (255, 255, 255)), (10, 40))

            pygame.display.flip()  # Met à jour l'affichage

# Nettoyage et fermeture
pygame.quit()
sys.exit()
