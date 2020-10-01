import time, random, pygame
from pygame.locals import *
import pygame.mixer

pygame.mixer.pre_init(44100, 16, 2, 4096)
GRILLE_LARGEUR = 300  # définition de la taille de la grille
GRILLE_LONGUEUR = 550  # Définition de la hauteur de la grille
LIGNES = 12  # Définition du nombre de lidne dans grille
COLONNES = 22  # Définition du nombre de colonne dans la grille
TAILLE_BOITE = 25
VIDE = "."
pygame.init()
pygame.mixer.music.load("Tetris.mp3")
pygame.mixer.music.play(-1)

# DEFINITION DES COULEUR DU JEU
#               R    G    B
BLANC = (255, 255, 255)
GRIS = (185, 185, 185)
NOIR = (0, 0, 0)
ROUGE = (155, 0, 0)
ROUGE_CLAIR = (175, 20, 20)
VERT = (0, 155, 0)
VERT_CLAIR = (20, 175, 20)
BLEU = (0, 0, 155)
BLEU_CLAIR = (20, 20, 175)
JAUNE = (155, 155, 0)
JAUNE_CLAIR = (175, 175, 20)
ORANGE = (255, 165, 0)
ORANGE_CLAIR = (255, 140, 0)
VIOLET = (148, 0, 211)
VIOLET_CLAIR = (153, 50, 204)
ROSE = (253, 108, 158)
COULEURS = (BLEU, VERT) 
BN=(BLANC,NOIR) 
# Tuple de couleurs
COULEURS_CLAIRES = (
BLEU_CLAIR, VERT_CLAIR, ROUGE_CLAIR, JAUNE_CLAIR, ORANGE_CLAIR, VIOLET_CLAIR)  # Tuple de couleurs claires
col = (250, 235, 215)
## Création des 7 pièces
L_C = [['..0..0', '000000', '...0..'], ['..0..0', '000000', '...0..']]
G_C = [['00.00', '0.0.0'], ['00.00', '0.0.0']]
OB3_FORME = [['.0.',
              '000',
              '.0.',
              ],
             ['.0.',
              '000',
              '.0.']]

S_FORME = [['.00',
            '00.', ],
           ['0.',
            '00',
            '.0', ]]

Z_FORME = [['00.',
            '.00'],
           ['.0',
            '00',
            '0.']]

I_FORME = [['0',
            '0',
            '0',
            '0'],
           ['0000']]

O_FORME = [['00',
            '00']]

J_FORME = [['0..',
            '000'],
           ['00',
            '0.',
            '0.'],
           ['000',
            '..0'],
           ['.0',
            '.0',
            '00']]

L_FORME = [['..0',
            '000'],
           ['0.',
            '0.',
            '00'],
           ['000',
            '0..'],
           ['00',
            '.0',
            '.0.']]

T_FORME = [['.0.',
            '000'],
           ['0.',
            '00',
            '0.'],
           ['000',
            '.0.'],
           ['.0',
            '00',
            '.0']]

PIECES = {'S': S_FORME, 'Z': Z_FORME, 'J': J_FORME, 'L': L_FORME, 'I': I_FORME, 'O': O_FORME,
          'T': T_FORME}  # regroupe toute les pièces
PIECESB = {'G': G_C, 'S': S_FORME, 'Z': Z_FORME, 'J': J_FORME, 'L': L_FORME, 'I': I_FORME, 'O': O_FORME, 'T': T_FORME}
PIECES2 = {'S': S_FORME, 'Z': Z_FORME, 'J': J_FORME, 'L': L_FORME, 'I': I_FORME, 'O': O_FORME,
          'T': T_FORME}

class GRILLE(object):
    def __init__(self):
        self.m_grille = [[VIDE] * LIGNES for i in range(COLONNES)]

    ##Création  de la Grille avec vide largeur=LIGNES et longeur= COLONNES

    def AjoutELEMENT(self, piece):
        FORME = PIECES[piece.getFORMEIndex()][piece.getPieceSuivante()]  # Récupérer les pièces dans la liste
        # La variable FORME sélectionne dans le tuple contenant les différentes pièce du jeu, les pièces du jeu à l'aide des index en utilisant (en faisiant appel) la fonction getPieceSuivante()

        # qui sélectionne aléatoirement la pièce suivante parmi toutes les pièces du jeu
        # la variable FORME définit les pièces et leur mouvement de rotation.
        LONGUEUR = len(FORME)
        # Longeur = au nombre d'éléments se trouvant dans la variable FORME
        LARGEUR = len(FORME[0])
        # lARGEUR = len(FORME[0])
        # Largeur = au nombre de forme qu'il y a dans le dictionnaire PIECES
        # QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
        for y in range(LONGUEUR):
            for x in range(LARGEUR):
                if FORME[y][x] != VIDE:
                    self.m_grille[y + int(piece.getPosY() / TAILLE_BOITE)][
                        x + int(piece.getPosX() / TAILLE_BOITE)] = piece.getColor()

    

    # création d'une double boucle dans la quelle on vérifie si la grille est vide toute en prenant compte la taille de la boîte, la position en x et en y
    # des pièces

    def lignecomplete(self, y):
        for x in range(LIGNES):
            if self.m_grille[y][x] == VIDE:
                return False
        return True

    ## une fonction pour tester si la ligne contient ou non des éléments.

    def effaceLigneComplete(self):
        y = COLONNES - 1
        nombreLignecomplete = 0
        ## on initialise y égal à la longueur de la grille (-1) (21 lignes)
        ## on initialise le nombre de ligne complète à 0

        while y >= 0:  ## on teste tant que le nombre de ligne est supérieur ou égale à 0
            if self.lignecomplete(y):
                nombreLignecomplete += 1
                ## un nombre de ligne complète s'ajoute
                for DansY in range(y, 0, -1):
                    for x in range(LIGNES):
                        ## parcours des lignes et des colonnes de la grille
                        self.m_grille[DansY][x] = self.m_grille[DansY - 1][
                            x]
                        ##pour une ligne complète de la grulle les coordonnées des colonnes décrémentent de -1
                for x in range(LIGNES):
                    self.m_grille[0][x] = VIDE
                    ## ainsi une nouvelle ligne s'ajoute au début de la grille
            else:
                y -= 1

        return nombreLignecomplete
        ## si la condition de la fonction lignecomplete() est vérifiéé on ajoute une ligne au premier rang, sinon on supprime la ligne complète

    def get(self, x, y):
        return self.m_grille[y][x]

    ## Dans cette donction on fait une mise à jour de la grille suivant les fonctions prédéfinies auparavant

    ## PYGAME ## DESSIN ### GRILLE ###

    def dessinergrille(self, screen):
        for y in range(COLONNES):
            for x in range(LIGNES):
                if self.m_grille[y][x] != VIDE:
                    pygame.draw.rect(screen, COULEURS[int(self.m_grille[y][x])],
                                     (x * TAILLE_BOITE, y * TAILLE_BOITE, TAILLE_BOITE, TAILLE_BOITE))
                    pygame.draw.rect(screen, COULEURS_CLAIRES[int(self.m_grille[y][x])],
                                     (x * TAILLE_BOITE, y * TAILLE_BOITE, TAILLE_BOITE, TAILLE_BOITE))
## Dessin de la grille avec pygame, utilisation de la fonction pygame.draw.rect()
class GRILLE2(object):
    def __init__(self):
        self.m_grille = [[VIDE] * LIGNES for i in range(COLONNES)]

    ##Création  de la Grille avec vide largeur=LIGNES et longeur= COLONNES

    def AjoutELEMENT2(self, piece):
        FORME = PIECES2[piece.getFORMEIndex()][piece.getPieceSuivante()]  # Récupérer les pièces dans la liste
        # La variable FORME sélectionne dans le tuple contenant les différentes pièce du jeu, les pièces du jeu à l'aide des index en utilisant (en faisiant appel) la fonction getPieceSuivante()

        # qui sélectionne aléatoirement la pièce suivante parmi toutes les pièces du jeu
        # la variable FORME définit les pièces et leur mouvement de rotation.
        LONGUEUR = len(FORME)
        # Longeur = au nombre d'éléments se trouvant dans la variable FORME
        LARGEUR = len(FORME[0])
        # lARGEUR = len(FORME[0])
        # Largeur = au nombre de forme qu'il y a dans le dictionnaire PIECES
        # QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
        for y in range(LONGUEUR):
            for x in range(LARGEUR):
                if FORME[y][x] != VIDE:
                    self.m_grille[y + int(piece.getPosY() / TAILLE_BOITE)][
                        x + int(piece.getPosX() / TAILLE_BOITE)] = piece.getColor()

    
    # création d'une double boucle dans la quelle on vérifie si la grille est vide toute en prenant compte la taille de la boîte, la position en x et en y
    # des pièces

    def lignecomplete(self, y):
        for x in range(LIGNES):
            if self.m_grille[y][x] == VIDE:
                return False
        return True

    ## une fonction pour tester si la ligne contient ou non des éléments.

    def effaceLigneComplete(self):
        y = COLONNES - 1
        nombreLignecomplete = 0
        ## on initialise y égal à la longueur de la grille (-1) (21 lignes)
        ## on initialise le nombre de ligne complète à 0

        while y >= 0:  ## on teste tant que le nombre de ligne est supérieur ou égale à 0
            if self.lignecomplete(y):
                nombreLignecomplete += 1
                ## un nombre de ligne complète s'ajoute
                for DansY in range(y, 0, -1):
                    for x in range(LIGNES):
                        ## parcours des lignes et des colonnes de la grille
                        self.m_grille[DansY][x] = self.m_grille[DansY - 1][
                            x]
                        ##pour une ligne complète de la grulle les coordonnées des colonnes décrémentent de -1
                for x in range(LIGNES):
                    self.m_grille[0][x] = VIDE
                    ## ainsi une nouvelle ligne s'ajoute au début de la grille
            else:
                y -= 1

        return nombreLignecomplete
        ## si la condition de la fonction lignecomplete() est vérifiéé on ajoute une ligne au premier rang, sinon on supprime la ligne complète

    def get(self, x, y):
        return self.m_grille[y][x]

    ## Dans cette donction on fait une mise à jour de la grille suivant les fonctions prédéfinies auparavant

    ## PYGAME ## DESSIN ### GRILLE ###

    def dessinergrille(self, screen):
        for y in range(COLONNES):
            for x in range(LIGNES):
                if self.m_grille[y][x] != VIDE:
                    pygame.draw.rect(screen, COULEURS[int(self.m_grille[y][x])],
                                     (x * TAILLE_BOITE, y * TAILLE_BOITE, TAILLE_BOITE, TAILLE_BOITE))
                    pygame.draw.rect(screen, COULEURS_CLAIRES[int(self.m_grille[y][x])],
                                     (x * TAILLE_BOITE, y * TAILLE_BOITE, TAILLE_BOITE, TAILLE_BOITE))
## Dessin de la grille avec pygame, utilisation de la fonction pygame.draw.rect()

