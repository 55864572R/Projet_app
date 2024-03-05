# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:54:28 2024

@author: ROMEO_YOTA
"""

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
largeur, hauteur = 500, 200
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Informations sur les touches du clavier")

# Police d'écriture
police = pygame.font.Font(None, 24)

# Boucle principale
while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evenement.type == pygame.KEYDOWN:
            # Récupération des informations sur la touche pressée
            touche_id = evenement.key
            touche_nom = pygame.key.name(touche_id)
            port_id = pygame.key.get_mods()

            # Création du texte à afficher
            texte_touche = f"Touche pressée : {touche_nom}"
            texte_id = f"ID de la touche : {touche_id}"
            texte_port = f"ID du port du clavier : {port_id}"

            # Affichage des informations dans la fenêtre
            fenetre.fill((0, 0, 0))  # Efface l'écran
            fenetre.blit(police.render(texte_touche, True, (255, 255, 255)), (10, 10))
            fenetre.blit(police.render(texte_id, True, (255, 255, 255)), (10, 40))
            fenetre.blit(police.render(texte_port, True, (255, 255, 255)), (10, 70))

            pygame.display.flip()  # Met à jour l'affichage

# Nettoyage et fermeture
pygame.quit()
sys.exit()
