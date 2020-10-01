import time, random, pygame
from pygame.locals import *
import pygame.mixer
pygame.mixer.pre_init(44100,16,2,4096)
BOITE_LARGEUR = 300 #définition de la taille de la fenêtre
BOITE_LONGUEUR = 550 #Définition de la hauteur de la fenêtre
LIGNES= 12 #Définition du nombre de lidne dans grille
COLONNES = 22 #Définition du nombre de colonne dans la grille
TAILLE_BOITE = 25
VIDE = "."
pygame.init()
pygame.mixer.music.load("Tetris.mp3")        
pygame.mixer.music.play(-1)

#DEFINITION DES COULEUR DU JEU
#               R    G    B
BLANC       = (255, 255, 255)
GRIS        = (185, 185, 185)
NOIR 	    = (  0,   0,   0)
ROUGE 	    = (155,   0,   0)
ROUGE_CLAIR = (175,  20,  20)
VERT        = (  0, 155,   0)
VERT_CLAIR  = ( 20, 175,  20)
BLEU        = (  0,   0, 155)
BLEU_CLAIR  = ( 20,  20, 175)
JAUNE       = (155, 155,   0)
JAUNE_CLAIR = (175, 175,  20)
ORANGE      = (255, 165,   0)
ORANGE_CLAIR= (255, 140,   0)
VIOLET      = (148,   0, 211)
VIOLET_CLAIR= (153,  50, 204)
ROSE        = (253, 108, 158) 
COULEURS    =(BLEU, VERT, ROUGE, JAUNE, ORANGE, VIOLET) #Tuple de couleurs
COULEURS_CLAIRES     =(BLEU_CLAIR, VERT_CLAIR, ROUGE_CLAIR, JAUNE_CLAIR, ORANGE_CLAIR, VIOLET_CLAIR) #Tuple de couleurs claires
col=(250,235,215)
## Création des 7 pièces
L_C=[['..0..0','000000','...0..'],['..0..0','000000','...0..']]
G_C=[['00.00','0.0.0'],['00.00','0.0.0']]
OB3_FORME = [['.0.',
            '000',
            '.0.',
            ],
          ['.0.',
            '000',
            '.0.']]

S_FORME = [['.00',
			'00.',],
		   ['0.',
		   '00',
		   '.0',]]

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

L_FORME  = [['..0',
		     '000'],
		    ['0.',
		     '0.',
		     '00'],
		    ['000',
		     '0..'],
		     ['00',
		     '.0',
		     '.0.']]

T_FORME  = [['.0.',
			 '000'],
			['0.',
			 '00',
			 '0.'],
			['000',
			 '.0.'],
			['.0',
			 '00',
			 '.0']]

PIECES = {'S': S_FORME, 'Z': Z_FORME, 'J': J_FORME, 'L' : L_FORME, 'I': I_FORME, 'O' : O_FORME, 'T' : T_FORME} # regroupe toute les pièces
PIECESB={'G':G_C,'S': S_FORME, 'Z': Z_FORME, 'J': J_FORME, 'L' : L_FORME, 'I': I_FORME, 'O' : O_FORME, 'T' : T_FORME}


class GRILLE(object):
	def __init__(self):
		self.m_grille = [[VIDE] * LIGNES for i in range (COLONNES )]
##Création  de la Grille avec vide largeur=LIGNES et longeur= COLONNES

	def AjoutELEMENT(self, piece):
		FORME = PIECES[piece.getFORMEIndex()][piece.getPieceSuivante()] 
        #Récupérer les pièces dans la liste
		# La variable FORME sélectionne dans le tuple contenant les différentes pièce du jeu, les pièces du jeu à l'aide des index en utilisant (en faisiant appel) la fonction getPieceSuivante()
		
		# qui sélectionne aléatoirement la pièce suivante parmi toutes les pièces du jeu
		# la variable FORME définit les pièces et leur mouvement de rotation.
		LONGUEUR = len(FORME)
		# Longeur = au nombre d'éléments se trouvant dans la variable FORME
		LARGEUR = len(FORME[0])
		# lARGEUR = len(FORME[0])
		# Largeur = au nombre de forme qu'il y a dans le dictionnaire PIECES
#QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
		for y in range(LONGUEUR):
			for x in range (LARGEUR):
				if FORME[y][x] != VIDE:
					self.m_grille[y + int(piece.getPosY() / TAILLE_BOITE)] [x + int(piece.getPosX() / TAILLE_BOITE)] = piece.getColor()

	def AjoutELEMENT2(self, piece):
		FORME = PIECESB[piece.getFORMEIndex()][piece.getPieceSuivante()] #Récupérer les pièces dans la liste
		# La variable FORME sélectionne dans le tuple contenant les différentes pièce du jeu, les pièces du jeu à l'aide des index en utilisant (en faisiant appel) la fonction getPieceSuivante()
		
		# qui sélectionne aléatoirement la pièce suivante parmi toutes les pièces du jeu
		# la variable FORME définit les pièces et leur mouvement de rotation.
		LONGUEUR = len(FORME)
		# Longeur = au nombre d'éléments se trouvant dans la variable FORME
		LARGEUR = len(FORME[0])
		# lARGEUR = len(FORME[0])
		# Largeur = au nombre de forme qu'il y a dans le dictionnaire PIECES

		for y in range(LONGUEUR):
			for x in range (LARGEUR):
				if FORME[y][x] != VIDE:
					self.m_grille[y + int(piece.getPosY() / TAILLE_BOITE)] [x + int(piece.getPosX() / TAILLE_BOITE)] = piece.getColor()
#création d'une double boucle dans la quelle on vérifie si la grille est vide toute en prenant compte la taille de la boîte, la position en x et en y
# des pièces



	def lignecomplete(self, y):
		for x in range (LIGNES):
			if self.m_grille[y][x]== VIDE:
				return False
		return True
## une fonction pour tester si la ligne contient ou non des éléments.


	def effaceLigneComplete(self):
		y = COLONNES  - 1
		nombreLignecomplete = 0
## on initialise y égal à la longueur de la grille (-1) (21 lignes)
## on initialise le nombre de ligne complète à 0

		while y >= 0:        ## on teste tant que le nombre de ligne est supérieur ou égale à 0
			if self.lignecomplete(y):
				nombreLignecomplete += 1   ## un nombre de ligne complète s'ajoute
				for colY in range(y, 0, -1):
					for x in range(LIGNES):  ## parcours des lignes et des colonnes de la grille
						self.m_grille[colY][x] = self.m_grille[colY-1 ][x] ##pour une ligne complète de la grulle les coordonnées des colonnes décrémentent de -1
				for x in range(LIGNES):
					self.m_grille[0][x] = VIDE ## ainsi une nouvelle ligne s'ajoute au début de la grille
			else:
				y -= 1


		return nombreLignecomplete     ## si la condition de la fonction lignecomplete() est vérifiéé on ajoute une ligne au premier rang, sinon on supprime la ligne complète


	def get(self, x, y):
		return self.m_grille[y][x]
## Dans cette donction on fait une mise à jour de la grille suivant les fonctions prédéfinies auparavant


## PYGAME ## DESSIN ### GRILLE ###

	def dessinergrille(self, screen):
		for y in range(COLONNES):
			for x in range (LIGNES):
				if self.m_grille[y][x] != VIDE:
					pygame.draw.rect(screen, COULEURS[int (self.m_grille[y][x])], (x * TAILLE_BOITE, y * TAILLE_BOITE, TAILLE_BOITE, TAILLE_BOITE))
					pygame.draw.rect(screen, COULEURS_CLAIRES[int(self.m_grille[y][x])], (x * TAILLE_BOITE , y * TAILLE_BOITE , TAILLE_BOITE , TAILLE_BOITE ))
## Dessin de la grille avec pygame, utilisation de la fonction pygame.draw.rect()



class Piece(object):
    def __init__(self): # Constructeur
        self.m_FORMEIndex = random.choice(list(PIECES.keys()))
        # self.m_FORMEIndex permet de sélectionner les pièces du jeu crées dans le dictionnaire formé à
        # l'aide de la méthode random.choice totu en sélectionnant les clés qui correspondent aux pièces du jeu.
        self.m_position = {'x' : int(BOITE_LARGEUR+0.5*BOITE_LARGEUR)-35, 'y' : BOITE_LONGUEUR/3.5}
        # self.m_position sert à positionner les pièces suivantes du jeu à droite de la grille (OAS ENCORE TERMINEE? EN PLEINE REFLEXION SUR LE SUJET).
        self.m_color = random.randint(0, len(COULEURS) - 1)
        # self.m_color sert à définir les couleurs des pièces aléatoirement à l'aide de la méthode random.randint dans le tuple COULEURS parmi tous les éléments de la liste.
        self.m_PieceSuivante = random.randint(0, len(PIECES[self.m_FORMEIndex])-1)
        # self.m_PieceSuivante sert à sélectionner aléatoirement les différentes du jeu à venir qui seront jouées parmi tous les éléments de la liste.
        self.m_FORME = PIECES[self.m_FORMEIndex][self.m_PieceSuivante]
        # self.m_FORME est égal à la
        self.LONGUEURPIECE = len(self.m_FORME)
        self.m_LARGEURPIECE = len(self.m_FORME[0])


    def getFORMEIndex(self):
        """
        Retourne la variable (m_FORMEIndex) définie dans le constructeur qui sélectionne les pièces du jeu dans la variable PIECES.
        """
        return self.m_FORMEIndex


    def getPieceSuivante(self):
        """
        Retourne la variable (m_PieceSuivante) définie dans le constructeur qui sélectionne les pièces de
        façon aléatoire parmi les pièces définies dans la variable PIECES.
        """
        return self.m_PieceSuivante


    def getPosX(self):
        """
        Retourne la variable (m_position['x']) définie dans le constructeur retourne ici les coordonnées
        en X dans l'affichage de la pièce suivante dans la BOITE.
        """
        return self.m_position['x']


    def getPosY(self):
        """
        Retourne la variable (m_position['y']) définie dans le constructeur retourne ici les coordonnées
        en Y dans l'affichage de la pièce suivante dans la BOITE.
        """
        return self.m_position['y']


    def getColor(self):
        """
        Retourne la variable (m_color) définie dans le constructeur qui sélectionne la couleur des pièces de
        façon aléatoire parmi les couleurs définies dans la variable COULEURS.
        """
        return self.m_color


    def setPos(self, x, y):
        """
        Affecte aux variables x et y, (m_position['x']) et (m_position['y'])
        utilisé ici pour définir les coordonnées dans la grille.
        """
        self.m_position['x'] = x
        self.m_position['y'] = y


    def setRotation(self, rotation):
        """
        Définition de la variable rotation.
        """
        self.rotation = rotation


    def bouger(self, x, y, GRILLE):
        """
        Dans cette fonction on ajoute aux coordonnées m_position['x'] et m_position['y'] les valeurs x et y lorsque la descente est valide.
        """
        if self.descenteValide(x, y, GRILLE):
            self.m_position['x'] += x
            self.m_position['y'] += y
            return True

        else:
            return False

    def bouger2(self, x, y, GRILLE):
        """
        Dans cette fonction on ajoute aux coordonnées m_position['x'] et m_position['y'] les valeurs x et y lorsque la descente est valide.
        """
        if self.descenteValide(x, y, GRILLE):
            self.m_position['x'] += x
            self.m_position['y'] += y
            return True

        else:
            return False


    def descenteValide(self, ajoutX, ajoutY, GRILLE):
        """
        Fonction qui vérifie une possibilité de descente de pièces dans la grille c-à-d que lors e la descente de la pièce, si elle
        croise la chaine de caractères '.' correspondant à la variable VIDE, on passe à la prochaine itération de la boucle grâce à
        l'instruction "continue"
        """
        for y in range(self.LONGUEURPIECE):
            for x in range(self.m_LARGEURPIECE):
                if self.m_FORME[y][x] == VIDE:
                    continue

                xPos = x + int((self.m_position['x'] + ajoutX) / TAILLE_BOITE) # Coordonnées de la pièce en x;
                yPos = y + int((self.m_position['y'] + ajoutY) / TAILLE_BOITE) # Coordonnées de la pièce en Y

                """
                Test : Si les coordonnées x de la pièce sont supérieures à zéro ou supérieures/égales à celles des lignes ou
                les coordonnées y de la pièce sont supérieures/égales à celles des colonnes ont retourne False.
                Si les lignes et les colonnes ne sont pas vides, on retourne aussi False.
                """

                if xPos < 0 or xPos >= LIGNES or yPos >= COLONNES:
                    return False
                if GRILLE.get(xPos, yPos) != VIDE:
                    return False

        return True


    def rotation(self, GRILLE):
        FORME = PIECES[self.m_FORMEIndex][(self.m_PieceSuivante + 1) % len(PIECES[self.m_FORMEIndex])]
        LARGEUR = len(FORME[0])

        rotation = self.m_PieceSuivante
        FORME = self.m_FORME
        FORMELONGUEUR = self.LONGUEURPIECE
        LARGEURPIECE  = self.m_LARGEURPIECE

        self.m_PieceSuivante = (self.m_PieceSuivante + 1) % len(PIECES[self.m_FORMEIndex])
        # Ici pour la rotation des PIECES des différentes pièces, on fait passer tour pour tour les différentes PIECES de pièces initialisées dans
        # chaque liste de la pièce suivante en ajoutant plus 1. Et on utilise  le modulo pour créer une sorte de boucle afin qu'on accède à
        # toutes les pièces au cours du jeu.
        self.m_FORME = PIECES[self.m_FORMEIndex][self.m_PieceSuivante]
        self.LONGUEURPIECE = len(self.m_FORME)
        self.m_LARGEURPIECE = len(self.m_FORME[0])

        if (self.m_position['x'] + LARGEUR * TAILLE_BOITE) <= BOITE_LARGEUR and self.descenteValide(0, 0, GRILLE):
            pass
        else:
            self.m_PieceSuivante = rotation
            self.m_FORME = FORME
            self.m_LARGEURPIECE = LARGEURPIECE
            self.LONGUEURPIECE = FORMELONGUEUR


    def dessinerpiece(self, screen):
        for y in range(self.LONGUEURPIECE):
            for x in range(self.m_LARGEURPIECE):
                if self.m_FORME[y][x] != VIDE:
                    pygame.draw.rect(screen, COULEURS[self.m_color], (self.m_position['x'] + x * TAILLE_BOITE, self.m_position['y'] + y * TAILLE_BOITE, TAILLE_BOITE, TAILLE_BOITE))
                    pygame.draw.rect(screen, COULEURS_CLAIRES[self.m_color], (self.m_position['x'] + x * TAILLE_BOITE + 1, self.m_position['y'] + y * TAILLE_BOITE + 1, TAILLE_BOITE - 2, TAILLE_BOITE - 2))









class Piece2(object):
    def __init__(self): # Constructeur
        self.m_FORMEIndex = random.choice(list(PIECES.keys()))
        # self.m_FORMEIndex permet de sélectionner les pièces du jeu crées dans le dictionnaire formé à
        # l'aide de la méthode random.choice totu en sélectionnant les clés qui correspondent aux pièces du jeu.
        self.m_position = {'x' : int(BOITE_LARGEUR+3.5*BOITE_LARGEUR)-35, 'y' : BOITE_LONGUEUR/3.5}
        # self.m_position sert à positionner les pièces suivantes du jeu à droite de la grille (OAS ENCORE TERMINEE? EN PLEINE REFLEXION SUR LE SUJET).
        self.m_color = random.randint(0, len(COULEURS) - 1)
        # self.m_color sert à définir les couleurs des pièces aléatoirement à l'aide de la méthode random.randint dans le tuple COULEURS parmi tous les éléments de la liste.
        self.m_PieceSuivante = random.randint(0, len(PIECES[self.m_FORMEIndex])-1)
        # self.m_PieceSuivante sert à sélectionner aléatoirement les différentes du jeu à venir qui seront jouées parmi tous les éléments de la liste.
        self.m_FORME = PIECES[self.m_FORMEIndex][self.m_PieceSuivante]
        # self.m_FORME est égal à la
        self.LONGUEURPIECE = len(self.m_FORME)
        self.m_LARGEURPIECE = len(self.m_FORME[0])


    def getFORMEIndex(self):
        """
        Retourne la variable (m_FORMEIndex) définie dans le constructeur qui sélectionne les pièces du jeu dans la variable PIECES.
        """
        return self.m_FORMEIndex


    def getPieceSuivante(self):
        """
        Retourne la variable (m_PieceSuivante) définie dans le constructeur qui sélectionne les pièces de
        façon aléatoire parmi les pièces définies dans la variable PIECES.
        """
        return self.m_PieceSuivante


    def getPosX(self):
        """
        Retourne la variable (m_position['x']) définie dans le constructeur retourne ici les coordonnées
        en X dans l'affichage de la pièce suivante dans la BOITE.
        """
        return self.m_position['x']


    def getPosY(self):
        """
        Retourne la variable (m_position['y']) définie dans le constructeur retourne ici les coordonnées
        en Y dans l'affichage de la pièce suivante dans la BOITE.
        """
        return self.m_position['y']


    def getColor(self):
        """
        Retourne la variable (m_color) définie dans le constructeur qui sélectionne la couleur des pièces de
        façon aléatoire parmi les couleurs définies dans la variable COULEURS.
        """
        return self.m_color


    def setPos(self, x, y):
        """
        Affecte aux variables x et y, (m_position['x']) et (m_position['y'])
        utilisé ici pour définir les coordonnées dans la grille.
        """
        self.m_position['x'] = x
        self.m_position['y'] = y


    def setRotation(self, rotation):
        """
        Définition de la variable rotation.
        """
        self.rotation = rotation


    def bouger(self, x, y, GRILLE):
        """
        Dans cette fonction on ajoute aux coordonnées m_position['x'] et m_position['y'] les valeurs x et y lorsque la descente est valide.
        """
        if self.descenteValide(x, y, GRILLE):
            self.m_position['x'] += x
            self.m_position['y'] += y
            return True

        else:
            return False

    def bouger2(self, x, y, GRILLE):
        """
        Dans cette fonction on ajoute aux coordonnées m_position['x'] et m_position['y'] les valeurs x et y lorsque la descente est valide.
        """
        if self.descenteValide(x, y, GRILLE):
            self.m_position['x'] += x
            self.m_position['y'] += y
            return True

        else:
            return False


    def descenteValide(self, ajoutX, ajoutY, GRILLE):
        """
        Fonction qui vérifie une possibilité de descente de pièces dans la grille c-à-d que lors e la descente de la pièce, si elle
        croise la chaine de caractères '.' correspondant à la variable VIDE, on passe à la prochaine itération de la boucle grâce à
        l'instruction "continue"
        """
        for y in range(self.LONGUEURPIECE):
            for x in range(self.m_LARGEURPIECE):
                if self.m_FORME[y][x] == VIDE:
                    continue

                xPos = x + int((self.m_position['x'] + ajoutX) / TAILLE_BOITE) # Coordonnées de la pièce en x;
                yPos = y + int((self.m_position['y'] + ajoutY) / TAILLE_BOITE) # Coordonnées de la pièce en Y

                """
                Test : Si les coordonnées x de la pièce sont supérieures à zéro ou supérieures/égales à celles des lignes ou
                les coordonnées y de la pièce sont supérieures/égales à celles des colonnes ont retourne False.
                Si les lignes et les colonnes ne sont pas vides, on retourne aussi False.
                """

                if xPos < 0 or xPos >= LIGNES or yPos >= COLONNES:
                    return False
                if GRILLE.get(xPos, yPos) != VIDE:
                    return False

        return True


    def rotation(self, GRILLE):
        FORME = PIECES[self.m_FORMEIndex][(self.m_PieceSuivante + 1) % len(PIECES[self.m_FORMEIndex])]
        LARGEUR = len(FORME[0])

        rotation = self.m_PieceSuivante
        FORME = self.m_FORME
        FORMELONGUEUR = self.LONGUEURPIECE
        LARGEURPIECE  = self.m_LARGEURPIECE

        self.m_PieceSuivante = (self.m_PieceSuivante + 1) % len(PIECES[self.m_FORMEIndex])
        # Ici pour la rotation des PIECES des différentes pièces, on fait passer tour pour tour les différentes PIECES de pièces initialisées dans
        # chaque liste de la pièce suivante en ajoutant plus 1. Et on utilise  le modulo pour créer une sorte de boucle afin qu'on accède à
        # toutes les pièces au cours du jeu.
        self.m_FORME = PIECES[self.m_FORMEIndex][self.m_PieceSuivante]
        self.LONGUEURPIECE = len(self.m_FORME)
        self.m_LARGEURPIECE = len(self.m_FORME[0])

        if (self.m_position['x'] + LARGEUR * TAILLE_BOITE) <= BOITE_LARGEUR and self.descenteValide(0, 0, GRILLE):
            pass
        else:
            self.m_PieceSuivante = rotation
            self.m_FORME = FORME
            self.m_LARGEURPIECE = LARGEURPIECE
            self.LONGUEURPIECE = FORMELONGUEUR


    def dessinerpiece2(self, screen):
        for y in range(self.LONGUEURPIECE):
            for x in range(self.m_LARGEURPIECE):
                if self.m_FORME[y][x] != VIDE:
                    pygame.draw.rect(screen, COULEURS[self.m_color], (self.m_position['x'] + x * TAILLE_BOITE, self.m_position['y'] + y * TAILLE_BOITE, TAILLE_BOITE, TAILLE_BOITE))
                    pygame.draw.rect(screen, COULEURS_CLAIRES[self.m_color], (self.m_position['x'] + x * TAILLE_BOITE + 1, self.m_position['y'] + y * TAILLE_BOITE + 1, TAILLE_BOITE - 2, TAILLE_BOITE - 2))








                    


class Multijoueur(object):
    def __init__(self):
        self.m_GRILLE = GRILLE() # On fait appel ici à la classe GRILLE() créee auparavant qu'on affecte à la variable m_GRILLE()
        self.m_PieceCourante = None    # Initialisation de la variable m_PieceCourante à laquelle définie aucune valeur
        self.m_SuivantePiece = Piece()  # On fait appel ici à la classe Piece() créee auparavant qu'on affecte à la variable m_SuivantePiece()
        self.m_piecechutes = False      # Définition de la variable m_piecechutes contenant des valeurs fausses (false ou 0)
        self.m_gameOver = False         # Définition de la variable m_gameOver contenant des valeurs fausses (false ou 0)
        self.m_direction = {'left' : False, 'right' : False, 'down' : False} # Création d'un dictionnaire m_direction contenant des
        # clés avec des valeurs fausses
        self.image=pygame.image.load("index.jpeg").convert()
        self.m_rotate = False # Définition de la variable m_rotate contenant des valeurs fausses (false ou 0)
        self.m_DernierrechuteTime = time.time() # Définition de la variable m_DernierchuteTime contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors de la chute d'une pièce
        self.m_DernierTempsMOuv = time.time()   # Définition de la variable m_DernierTempsMouv contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors du mouvement de la d'une pièce
        self.Vic="  "
        self.m_score = 0    # Initialisation de la variable m_score à 0
        self.m_niveau = 1
        self.plateau1=pygame.Surface((300,553))
        self.plateau2=pygame.Surface((300,553))
        self.m_score2 = 0 
        self.bigText = pygame.font.SysFont('PLANK___.TTF', 36)
        self.title_text = self.bigText.render("J2: "+str(self.m_score2),
                                    True, VERT)
        self.bigText2 = pygame.font.SysFont('PLANK___.TTF', 36)
        self.title_text2 = self.bigText2.render("J1: "+str(self.m_score),
                                    True, VERT)
        self.bigText3 = pygame.font.SysFont('PLANK___.TTF', 36)
        self.title_text3 = self.bigText3.render("VAINQUEUR: "+str(self.Vic),
                                    True, VERT)
        self.plateau_score=pygame.Surface((800,600))
        self.JOUEUR1=" "
        self.JOUEUR2=" "
        self.m_GRILLE2 = GRILLE() # On fait appel ici à la classe GRILLE() créee auparavant qu'on affecte à la variable m_GRILLE()
        self.m_PieceCourante2 = None    # Initialisation de la variable m_PieceCourante à laquelle définie aucune valeur
        self.m_SuivantePiece2 = Piece2()  # On fait appel ici à la classe Piece() créee auparavant qu'on affecte à la variable m_SuivantePiece()
        self.m_piecechutes2 = False      # Définition de la variable m_piecechutes contenant des valeurs fausses (false ou 0)
        self.m_gameOver = False         # Définition de la variable m_gameOver contenant des valeurs fausses (false ou 0)
        self.m_direction2 = {'gauche' : False, 'droite' : False, 'bas' : False} # Création d'un dictionnaire m_direction contenant des
        # clés avec des valeurs fausses
        self.m_rotate2 = False # Définition de la variable m_rotate contenant des valeurs fausses (false ou 0)
        self.m_DernierrechuteTime2 = time.time() # Définition de la variable m_DernierchuteTime contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors de la chute d'une pièce
        self.m_DernierTempsMOuv2 = time.time()   # Définition de la variable m_DernierTempsMouv contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors du mouvement de la d'une pièce
           # Initialisation de la variable m_score à 0

        self.m_niveau2 = 1
        pygame.init()   # initialiser tous les modules pygame importés
        self.boite = pygame.display.set_mode((BOITE_LARGEUR * 6, BOITE_LONGUEUR*3)) # Initialisation de l'écran pour l'affichage
        # Cette fonction créera une surface d'affichage. Les arguments transmis sont des demandes pour un type d'affichage.
        # L’affichage créé sera la meilleure correspondance possible prise en charge par le système.
        pygame.display.set_caption('Turner Teen') # Obtenir la légende de la fenêtre en cours


            
    
    def logic(self):


        if time.time() - self.m_DernierTempsMOuv > 0.1:
            if self.m_direction['left'] == True:
            #
            #si la touche gauche est appuyée physiquement la directionde la piece va dans
            #la direction gauche de a grille d'ou l'utilisation du signe (-) négatif
            #qui indique le sens contraire en considerant que sin on part de la gauche vers la droite
            #on part dans le sens positif sinon dans le sens négatif
            #
                self.m_PieceCourante.bouger(-TAILLE_BOITE, 0, self.m_GRILLE)

            elif self.m_direction['right'] == True:

                self.m_PieceCourante.bouger(TAILLE_BOITE, 0, self.m_GRILLE)

            elif self.m_direction['down'] == True:
            #
            #si la touche directiont haut est appuyée physiquement la piece suivante va dans le sens positif (+) de la grille
            #c'est a dire de la gauche vers la droite
            #
                self.m_PieceCourante.bouger(0, TAILLE_BOITE, self.m_GRILLE)

            self.m_DernierTempsMOuv = time.time()

        elif self.m_rotate:
            self.m_PieceCourante.rotation(self.m_GRILLE)
            self.m_rotate = False



    def logic2(self):


        if time.time() - self.m_DernierTempsMOuv2 > 0.1:
            if self.m_direction2['gauche'] == True:
            #
            #si la touche gauche est appuyée physiquement la directionde la piece va dans
            #la direction gauche de a grille d'ou l'utilisation du signe (-) négatif
            #qui indique le sens contraire en considerant que sin on part de la gauche vers la droite
            #on part dans le sens positif sinon dans le sens négatif
            #
                self.m_PieceCourante2.bouger2(-TAILLE_BOITE, 0, self.m_GRILLE2)

            elif self.m_direction2['droite'] == True:

                self.m_PieceCourante2.bouger2(TAILLE_BOITE, 0, self.m_GRILLE2)

            elif self.m_direction2['bas'] == True:
            #
            #si la touche directiont haut est appuyée physiquement la piece suivante va dans le sens positif (+) de la grille
            #c'est a dire de la gauche vers la droite
            #
                self.m_PieceCourante2.bouger2(0, TAILLE_BOITE, self.m_GRILLE2)

            self.m_DernierTempsMOuv2 = time.time()

        elif self.m_rotate2:
            self.m_PieceCourante2.rotation(self.m_GRILLE2)
            self.m_rotate2 = False





    def texte(self, text, font):
        texteSurface = font.render(text, True, VERT) # On affecte à la variable texteSurface la fonction pygame font.render avec laquelle on pourra
        # créer un nouvel objet à partir d'un fichier.
        return texteSurface, texteSurface.get_rect()    # On retourne ici la variable texteSurface et, on retourne aussi cette variable associée avec
        # la fonction pygame get_rect() qui retourne un nouveau rectangle couvrant toute la surface.

    def vainqueur(self):
        if self.m_score2 >self.m_score and self.m_score2!=self.m_score:
            self.Vic=self.JOUEUR2

        elif self.m_score2<self.m_score and self.m_score2!=self.m_score:
            self.Vic=self.JOUEUR1


        if self.m_score2==self.m_score:
            self.Vic="EGALITE"
           
     
    
        
    def afficheScore(self):
        self.vainqueur()
        font4 = pygame.font.Font('04B_30__.TTF', 17) # On affecte à la variable font la fonction pygame font.Font qui crée un nouvel objet Font
        # à partir d'un fichier. Ce fichier Font se constitue du nom de la police ainsi que de sa taille
        textSurf7, textRect7 = self.texte(str(self.JOUEUR2) +"  "+ str(self.m_score2), font4)
        textRect7.center = (BOITE_LARGEUR + 2.85* BOITE_LARGEUR , BOITE_LONGUEUR / 4)

        textSurf3, textRect3 = self.texte(str(self.JOUEUR1)+"  "  + str(self.m_score), font4)
        textRect3.center = (BOITE_LARGEUR + 1.2 * BOITE_LARGEUR , BOITE_LONGUEUR /4 )

        textSurf2, textRect2 = self.texte(' VAINQUEUR : '+ str(self.Vic), font4)
        textRect2.center = (BOITE_LARGEUR + 2 * BOITE_LARGEUR, BOITE_LONGUEUR / 1.2)
        self.boite.blit(textSurf7, textRect7)
        self.boite.blit(textSurf2, textRect2)
        self.boite.blit(textSurf3, textRect3)
        pygame.display.update()
    
    def dessinelements(self):
#Fonction dessin de la grille de la piece suivante de la grille et de l'interface graphique
        self.afficheScore()
        self.boite.fill((BLANC))
#Couleur de fond de la BOITE en noir
        self.plateau_score.fill((VERT))
#dessin des lignes  et des colone de la grille
        self.plateau1.fill((col))
        self.plateau2.fill((col))
        
        pygame.draw.rect(self.boite,VERT,[550,10,700,600],8)
  
        self.m_GRILLE.dessinergrille(self.plateau1)
        self.m_GRILLE2.dessinergrille(self.plateau2)
        self.m_PieceCourante.dessinerpiece(self.plateau1)
        self.m_SuivantePiece.dessinerpiece(self.boite)
#contour de la premiere grille 
        pygame.draw.line(self.boite,ROUGE,(4,12),(335,12),15)
        pygame.draw.line(self.boite,ROUGE,(4,580),(335,580),15)
        pygame.draw.line(self.boite,ROUGE,(11,12),(11,580),15)
        pygame.draw.line(self.boite,ROUGE,(328,12),(328,580),15)
        #
        pygame.draw.line(self.boite,ROUGE,(1435,12),(1757,12),15)
        pygame.draw.line(self.boite,ROUGE,(1435,580),(1757,580),15)
        pygame.draw.line(self.boite,ROUGE,(1442,14),(1442,584),15)
        pygame.draw.line(self.boite,ROUGE,(1758,5),(1758,588),15)        
        self.m_PieceCourante2.dessinerpiece2(self.plateau2)
        self.m_SuivantePiece2.dessinerpiece2(self.boite)
        #self.boite.blit(self.title_text,(1100,90))
        #self.boite.blit(self.title_text2,(600,90))
        #self.boite.blit(self.title_text3,(775,500))
        
        self.boite.blit(self.image,(770,210))
        self.boite.blit(self.plateau1, (20,20))
        self.boite.blit(self.plateau2, (1450,20))
        #self.afficheScore()
        #self.afficheScore()
#raffarichissement du score
        pygame.display.update()
#dessin de la grille piece suivante grille et score
#appel de la fonction MiseaJour qui permet de raffraichir la BOITE a chaque fois
    def entreeDonnees(self):

        for event in pygame.event.get():
#definition de l'evenenment defaite si la grille est remplie la ligne suivante ferme directement le programme
#ainsi game_over =true
            if event.type == pygame.QUIT:
                self.m_gameOver = True
#definition des evenement liés aux commandes du jeu
            #
            #lorsque l'utilisateur appuie sur le touche du bas il est possible pur lui de deplacer la piece avec les touches directionnelles
            #gauche droite bas et espace qui utilise la rotation du coup on assigena ces  vraiables la valeur True
            #
            if event.type == pygame.KEYDOWN:
#Detecte si la touche direction du bas est appuyée physiquement
                if event.key == pygame.K_LEFT:
                	self.m_direction2['gauche'] = True
                    
                elif event.key == pygame.K_RIGHT:
                	self.m_direction2['droite'] = True
                    
                elif event.key == pygame.K_DOWN:
                	self.m_direction2['bas'] = True
                    
                elif event.key == pygame.K_RCTRL:
                    self.m_rotate2 = True
                elif event.key == pygame.K_ESCAPE:
                    self.m_gameOver = True
            
            




            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:                   
                    self.m_direction['left'] = True
                elif event.key == pygame.K_d:
                	self.m_direction['right'] = True                    
                elif event.key == pygame.K_s:              
                    self.m_direction['down'] = True
                elif event.key == pygame.K_n:
                    self.m_rotate = True
                elif event.key == pygame.K_ESCAPE:
                    self.m_gameOver = True
            #la touche direction du haut n'a aucun role ici
            #
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.m_direction2['gauche'] = False
                elif event.key == pygame.K_RIGHT:
                    self.m_direction2['droite'] = False
                elif event.key == pygame.K_DOWN:
                    self.m_direction2['bas'] = False

            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_q:
                    self.m_direction['left'] = False
                elif event.key == pygame.K_d:
                    self.m_direction['right'] = False
                elif event.key == pygame.K_s:
                    self.m_direction['down'] = False
   

    def MiseaJour(self):
#le module time.time() permet de mesurer la durée entre deux evenement
#il represente aussi le "EPOCH" explication dans le rapport...

        if time.time() - self.m_DernierrechuteTime > .2:
#on verifie si le nombre de secondes ecoulées
#jusqu'a la chute dela derniere piece est superieure a 1
#
            if self.m_piecechutes:
                if self.m_PieceCourante.bouger(0, TAILLE_BOITE, self.m_GRILLE): # A revoir pygame doc !!!!!!!!!!!!!!!!
                    pass
#
#On teste si la piece est en pleine chute si oui on passe


                else:
                    self.m_piecechutes = False
                    self.m_GRILLE.AjoutELEMENT(self.m_PieceCourante) # On ajoute la pièce à la grille tant qu'elle n'est pas en mouvement
                    self.m_score += (self.m_GRILLE.effaceLigneComplete())*25  # On ajoute 10 au score à chaque fois qu'une ligne est effacée.

                self.m_DernierrechuteTime = time.time()

        if not self.m_piecechutes:
            self.m_PieceCourante = self.m_SuivantePiece # Si il n'y a aucune pièce en chute, on affiche dans la grille la prochaine pièce
            self.m_SuivantePiece = Piece()
            self.m_PieceCourante.setPos(int(BOITE_LARGEUR / 2) - 50, 0) # Centre la pièce dans la grille par rapport à sa largeur
            self.m_piecechutes = True
            if not self.m_PieceCourante.descenteValide(0, 0, self.m_GRILLE):
                self.m_gameOver = True

    def MiseaJour2(self):

#le module time.time() permet de mesurer la durée entre deux evenement
#il represente aussi le "EPOCH" explication dans le rapport...
        if time.time() - self.m_DernierrechuteTime2 > .2:
#on verifie si le nombre de secondes ecoulées
#jusqu'a la chute dela derniere piece est superieure a 1
#
            if self.m_piecechutes2:
                if self.m_PieceCourante2.bouger2(0, TAILLE_BOITE, self.m_GRILLE2): # A revoir pygame doc !!!!!!!!!!!!!!!!
                    pass#

#
#On teste si la piece est en pleine chute si oui on passe


                else:
                    self.m_piecechutes2 = False
                    self.m_GRILLE2.AjoutELEMENT(self.m_PieceCourante2) # On ajoute la pièce à la grille tant qu'elle n'est pas en mouvement
                    self.m_score2 += (self.m_GRILLE2.effaceLigneComplete())*25  # On ajoute 10 au score à chaque fois qu'une ligne est effacée.

                self.m_DernierrechuteTime2 = time.time()

        
       

        if not self.m_piecechutes2:
            self.m_PieceCourante2 = self.m_SuivantePiece2 # Si il n'y a aucune pièce en chute, on affiche dans la grille la prochaine pièce
            self.m_SuivantePiece2 = Piece2()
            self.m_PieceCourante2.setPos(int(BOITE_LARGEUR / 2) - 50, 0) # Centre la pièce dans la grille par rapport à sa largeur
            self.m_piecechutes2 = True
            if not self.m_PieceCourante2.descenteValide(0, 0, self.m_GRILLE2):
                self.m_gameOver = True
        

    def confrontation(self):
        if self.m_score>=75 and self.m_score2>=75:
            PIECES['OB']=OB3_FORME 
        if self.m_score>=150 and self.m_score2>=150:
            PIECES['LLC']=L_C

        if self.m_score>=200 and self.m_score2>=200:
            PIECES['G']=G_C 

    

    

    def Lancement(self):
        self.JOUEUR1 = input('Entrez votre nom : ')
        self.JOUEUR2= input('Nom du second joueur : ')         


        while not self.m_gameOver:
            self.MiseaJour()
            self.confrontation()
            self.entreeDonnees()
            self.logic()
            self.afficheScore()
            self.MiseaJour2()
            self.logic2()    
            self.dessinelements()
            

    
    		

class Solo(object):
    def __init__(self):
        self.m_GRILLE = GRILLE() # On fait appel ici à la classe GRILLE() créee auparavant qu'on affecte à la variable m_GRILLE()
        self.m_PieceCourante = None    # Initialisation de la variable m_PieceCourante à laquelle définie aucune valeur
        self.m_SuivantePiece = Piece()  # On fait appel ici à la classe Piece() créee auparavant qu'on affecte à la variable m_SuivantePiece()
        self.m_piecechutes = False      # Définition de la variable m_piecechutes contenant des valeurs fausses (false ou 0)
        self.m_gameOver = False         # Définition de la variable m_gameOver contenant des valeurs fausses (false ou 0)
        self.m_direction = {'left' : False, 'right' : False, 'down' : False} # Création d'un dictionnaire m_direction contenant des
        # clés avec des valeurs fausses
        self.m_rotate = False # Définition de la variable m_rotate contenant des valeurs fausses (false ou 0)
        self.m_DernierrechuteTime = time.time() # Définition de la variable m_DernierchuteTime contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors de la chute d'une pièce
        self.m_DernierTempsMOuv = time.time()   # Définition de la variable m_DernierTempsMouv contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors du mouvement de la d'une pièce
        self.plateau=pygame.Surface((300,553))
        self.m_score = 0    # Initialisation de la variable m_score à 0
        
        self.m_niveau = 1
        pygame.init()   # initialiser tous les modules pygame importés
        self.boite = pygame.display.set_mode((BOITE_LARGEUR * 6, BOITE_LONGUEUR*3)) # Initialisation de l'écran pour l'affichage
        # Cette fonction créera une surface d'affichage. Les arguments transmis sont des demandes pour un type d'affichage.
        # L’affichage créé sera la meilleure correspondance possible prise en charge par le système.
        pygame.display.set_caption('Turner Teen') # Obtenir la légende de la fenêtre en cours
       

    def logic(self):


        if time.time() - self.m_DernierTempsMOuv > 0.1:
            if self.m_direction['left'] == True:
            #
            #si la touche gauche est appuyée physiquement la directionde la piece va dans
            #la direction gauche de a grille d'ou l'utilisation du signe (-) négatif
            #qui indique le sens contraire en considerant que sin on part de la gauche vers la droite
            #on part dans le sens positif sinon dans le sens négatif
            #
                self.m_PieceCourante.bouger(-TAILLE_BOITE, 0, self.m_GRILLE)

            elif self.m_direction['right'] == True:

                self.m_PieceCourante.bouger(TAILLE_BOITE, 0, self.m_GRILLE)

            elif self.m_direction['down'] == True:
            #
            #si la touche directiont haut est appuyée physiquement la piece suivante va dans le sens positif (+) de la grille
            #c'est a dire de la gauche vers la droite
            #
                self.m_PieceCourante.bouger(0, TAILLE_BOITE, self.m_GRILLE)

            self.m_DernierTempsMOuv = time.time()

        elif self.m_rotate:
            self.m_PieceCourante.rotation(self.m_GRILLE)
            self.m_rotate = False

    def dessinerLignes(self):
        for i in range(LIGNES + 1): # Boucle dans la on parcours toutes nos lignes initialisées hors des fonctions
            pygame.draw.line(self.boite, NOIR, (i * TAILLE_BOITE, 0), (i * TAILLE_BOITE, BOITE_LONGUEUR))
        for j in range(COLONNES):    # Boucle dans la on parcours toutes nos colonnes initialisées hors des fonctions
            pygame.draw.line(self.boite, NOIR, (0 , j * TAILLE_BOITE), (BOITE_LARGEUR, j * TAILLE_BOITE))


    def texte(self, text, font):
        texteSurface = font.render(text, True, ROSE) # On affecte à la variable texteSurface la fonction pygame font.render avec laquelle on pourra
        # créer un nouvel objet à partir d'un fichier.
        return texteSurface, texteSurface.get_rect()    # On retourne ici la variable texteSurface et, on retourne aussi cette variable associée avec
        # la fonction pygame get_rect() qui retourne un nouveau rectangle couvrant toute la surface.


    def afficheScore(self):
        font = pygame.font.Font('upheavtt.ttf', 40) # On affecte à la variable font la fonction pygame font.Font qui crée un nouvel objet Font
        # à partir d'un fichier. Ce fichier Font se constitue du nom de la police ainsi que de sa taille
        textSurf, textRect = self.texte('SCORE : ' + str(self.m_score), font)
        textRect.center = (BOITE_LARGEUR + 0.5 * BOITE_LARGEUR , BOITE_LONGUEUR / 1.5)

        textSurf3, textRect3 = self.texte('NIVEAU : ' + str(self.m_niveau), font)
        textRect3.center = (BOITE_LARGEUR + 0.5 * BOITE_LARGEUR , BOITE_LONGUEUR - 85 )

        textSurf2, textRect2 = self.texte('Piece suivante :', font)
        textRect2.center = (BOITE_LARGEUR + 0.5 * BOITE_LARGEUR, BOITE_LONGUEUR / 6)
        textSurf10, textRect10 = self.texte('LIGNE EFFACÉE :'+str(int(self.m_score/25)), font)
        textRect10.center = (BOITE_LARGEUR + 0.5 * BOITE_LARGEUR, BOITE_LONGUEUR / 2)
        self.boite.blit(textSurf, textRect)
        self.boite.blit(textSurf2, textRect2)
        self.boite.blit(textSurf3, textRect3)
        self.boite.blit(textSurf10, textRect10)

 

    def dessinelements(self):
#Fonction dessin de la grille de la piece suivante de la grille et de l'interface graphique
        self.plateau.fill((col))
        
        self.boite.fill(BLANC)
#Couleur de fond de la BOITE en noir

#dessin des lignes  et des colone de la grille
        self.m_GRILLE.dessinergrille(self.plateau)
        self.m_PieceCourante.dessinerpiece(self.plateau)
        self.m_SuivantePiece.dessinerpiece(self.boite)
        self.afficheScore()
        self.boite.blit(self.plateau,(800,20))
        pygame.draw.line(self.boite,ROSE,((804-20),12),(1135-20,12),15)
        pygame.draw.line(self.boite,ROSE,(804-20,580),(1135-20,580),15)
        pygame.draw.line(self.boite,ROSE,(811-20,12),(811-20,580),15)
        pygame.draw.line(self.boite,ROSE,(1128-20,12),(1128-20,580),15)
#raffarichissement du score
        pygame.display.update()
#raffarichissement du score
        pygame.display.update()
#dessin de la grille piece suivante grille et score
#appel de la fonction MiseaJour qui permet de raffraichir la BOITE a chaque fois
    def entreeDonnees(self):
        for event in pygame.event.get():
#definition de l'evenenment defaite si la grille est remplie la ligne suivante ferme directement le programme
#ainsi game_over =true
            if event.type == pygame.QUIT:
                self.m_gameOver = True
#definition des evenement liés aux commandes du jeu
            #
            #lorsque l'utilisateur appuie sur le touche du bas il est possible pur lui de deplacer la piece avec les touches directionnelles
            #gauche droite bas et espace qui utilise la rotation du coup on assigena ces  vraiables la valeur True
            #
            if event.type == pygame.KEYDOWN:
#Detecte si la touche direction du bas est appuyée physiquement
                if event.key == pygame.K_LEFT:
                    self.m_direction['left'] = True
                elif event.key == pygame.K_RIGHT:
                    self.m_direction['right'] = True
                elif event.key == pygame.K_DOWN:
                    self.m_direction['down'] = True
                elif event.key == pygame.K_RCTRL:
                    self.m_rotate = True
                elif event.key == pygame.K_ESCAPE:
                    self.m_gameOver = True
             #
            #la touche direction du haut n'a aucun role ici
            #
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.m_direction['left'] = False
                elif event.key == pygame.K_RIGHT:
                    self.m_direction['right'] = False
                elif event.key == pygame.K_DOWN:
                    self.m_direction['down'] = False

    def MiseaJour(self):
#le module time.time() permet de mesurer la durée entre deux evenement
#il represente aussi le "EPOCH" explication dans le rapport...
        if time.time() - self.m_DernierrechuteTime > 1:
#on verifie si le nombre de secondes ecoulées
#jusqu'a la chute dela derniere piece est superieure a 1
#
            if self.m_piecechutes:
                if self.m_PieceCourante.bouger(0, TAILLE_BOITE, self.m_GRILLE): # A revoir pygame doc !!!!!!!!!!!!!!!!
                    pass
#
#On teste si la piece est en pleine chute si oui on passe


                else:
                    self.m_piecechutes = False
                    self.m_GRILLE.AjoutELEMENT(self.m_PieceCourante) # On ajoute la pièce à la grille tant qu'elle n'est pas en mouvement
                    self.m_score += (self.m_GRILLE.effaceLigneComplete())*25  # On ajoute 10 au score à chaque fois qu'une ligne est effacée.

                self.m_DernierrechuteTime = time.time()

        if not self.m_piecechutes:
            self.m_PieceCourante = self.m_SuivantePiece # Si il n'y a aucune pièce en chute, on affiche dans la grille la prochaine pièce
            self.m_SuivantePiece = Piece()
            self.m_PieceCourante.setPos(int(BOITE_LARGEUR / 2) - 50, 0) # Centre la pièce dans la grille par rapport à sa largeur
            self.m_piecechutes = True
            if not self.m_PieceCourante.descenteValide(0, 0, self.m_GRILLE):
                self.m_gameOver = True





    

    def niveau(self):                    # Niveau de jeu
        """
        NIVEAU
        """

        if self.m_score >= 50:

            self.m_niveau = 2
            
            pygame.display.update()
        if self.m_niveau == 2 and self.m_score >= 105:
            PIECES['OB']=OB3_FORME
            self.m_niveau = 3
            pygame.display.update()
        if self.m_niveau == 3 and self.m_score >= 180:
            PIECES['LLC']=L_C
            self.m_niveau = 4
            pygame.display.update()

        if self.m_niveau == 4 and self.m_score >= 225:
            PIECES['G']=G_C
            self.m_niveau = "BOSS"
            pygame.display.update()

    def changement(self):
        if self.m_niveau==2 and time.time() - self.m_DernierrechuteTime > 0.5 :
            if self.m_piecechutes:
                if self.m_PieceCourante.bouger(0, TAILLE_BOITE, self.m_GRILLE): # A revoir pygame doc !!!!!!!!!!!!!!!!
                    pass
#
#On teste si la piece est en pleine chute si oui on passe


                else:
                    self.m_piecechutes = False
                    self.m_GRILLE.AjoutELEMENT(self.m_PieceCourante) # On ajoute la pièce à la grille tant qu'elle n'est pas en mouvement
                    self.m_score += (self.m_GRILLE.effaceLigneComplete())*25  # On ajoute 10 au score à chaque fois qu'une ligne est effacée.

                self.m_DernierrechuteTime = time.time()

        if not self.m_piecechutes:
            self.m_PieceCourante = self.m_SuivantePiece # Si il n'y a aucune pièce en chute, on affiche dans la grille la prochaine pièce
            self.m_SuivantePiece = Piece()
            self.m_PieceCourante.setPos(int(BOITE_LARGEUR / 2) - 50, 0) # Centre la pièce dans la grille par rapport à sa largeur
            self.m_piecechutes = True
            if not self.m_PieceCourante.descenteValide(0, 0, self.m_GRILLE):
                self.m_gameOver = True

        if self.m_niveau==3 and time.time() - self.m_DernierrechuteTime > 0.4 :
            if self.m_piecechutes:
                if self.m_PieceCourante.bouger(0, TAILLE_BOITE, self.m_GRILLE): # A revoir pygame doc !!!!!!!!!!!!!!!!
                    pass
#
#On teste si la piece est en pleine chute si oui on passe


                else:
                    self.m_piecechutes = False
                    self.m_GRILLE.AjoutELEMENT(self.m_PieceCourante) # On ajoute la pièce à la grille tant qu'elle n'est pas en mouvement
                    self.m_score += (self.m_GRILLE.effaceLigneComplete())*25  # On ajoute 10 au score à chaque fois qu'une ligne est effacée.

                self.m_DernierrechuteTime = time.time()

        if not self.m_piecechutes:
            self.m_PieceCourante = self.m_SuivantePiece # Si il n'y a aucune pièce en chute, on affiche dans la grille la prochaine pièce
            self.m_SuivantePiece = Piece()
            self.m_PieceCourante.setPos(int(BOITE_LARGEUR / 2) - 50, 0) # Centre la pièce dans la grille par rapport à sa largeur
            self.m_piecechutes = True
            if not self.m_PieceCourante.descenteValide(0, 0, self.m_GRILLE):
                self.m_gameOver = True
    

        if self.m_niveau==4 and time.time() - self.m_DernierrechuteTime > 0.2 :
            if self.m_piecechutes:
                if self.m_PieceCourante.bouger(0, TAILLE_BOITE, self.m_GRILLE): # A revoir pygame doc !!!!!!!!!!!!!!!!
                    pass
#
#On teste si la piece est en pleine chute si oui on passe


                else:
                    self.m_piecechutes = False
                    self.m_GRILLE.AjoutELEMENT(self.m_PieceCourante) # On ajoute la pièce à la grille tant qu'elle n'est pas en mouvement
                    self.m_score += (self.m_GRILLE.effaceLigneComplete())*25  # On ajoute 10 au score à chaque fois qu'une ligne est effacée.

                self.m_DernierrechuteTime = time.time()

        if not self.m_piecechutes:
            self.m_PieceCourante = self.m_SuivantePiece # Si il n'y a aucune pièce en chute, on affiche dans la grille la prochaine pièce
            self.m_SuivantePiece = Piece()
            self.m_PieceCourante.setPos(int(BOITE_LARGEUR / 2) - 50, 0) # Centre la pièce dans la grille par rapport à sa largeur
            self.m_piecechutes = True
            if not self.m_PieceCourante.descenteValide(0, 0, self.m_GRILLE):
                self.m_gameOver = True

        if self.m_niveau=="BOSS" and time.time() - self.m_DernierrechuteTime > 0.2 :
            if self.m_piecechutes:
                if self.m_PieceCourante.bouger(0, TAILLE_BOITE, self.m_GRILLE): # A revoir pygame doc !!!!!!!!!!!!!!!!
                    pass
#
#On teste si la piece est en pleine chute si oui on passe


                else:
                    self.m_piecechutes = False
                    self.m_GRILLE.AjoutELEMENT(self.m_PieceCourante) # On ajoute la pièce à la grille tant qu'elle n'est pas en mouvement
                    self.m_score += (self.m_GRILLE.effaceLigneComplete())*25  # On ajoute 10 au score à chaque fois qu'une ligne est effacée.

                self.m_DernierrechuteTime = time.time()

        if not self.m_piecechutes:
            self.m_PieceCourante = self.m_SuivantePiece # Si il n'y a aucune pièce en chute, on affiche dans la grille la prochaine pièce
            self.m_SuivantePiece = Piece()
            self.m_PieceCourante.setPos(int(BOITE_LARGEUR / 2) - 50, 0) # Centre la pièce dans la grille par rapport à sa largeur
            self.m_piecechutes = True
            if not self.m_PieceCourante.descenteValide(0, 0, self.m_GRILLE):
                self.m_gameOver = True

    def Lancement(self):
        while not self.m_gameOver:
            self.MiseaJour()
            self.entreeDonnees()
            self.logic()
            self.dessinelements()
            self.niveau()
            self.changement()

#n = int(input("QUEL MODE VOULEZ VOUS JOUER MULTIJOUEUR TAPEZ :1 , SOLO TAPEZ :0  "))
#if n==0:
#c=Commande()
#c.Lancement()
#pygame.quit()
#else:
    #print("Ce mode n'est pas encore crée")
			
#n = int(input("QUEL MODE VOULEZ VOUS JOUER MULTIJOUEUR TAPEZ :1 , SOLO TAPEZ :0  "))
#if n==0:
#v=Multijoueur()
#v.Lancement()
#pygame.quit()
#else:
    #print("Ce mode n'est pas encore crée")


class Multijoueur(object):
    def __init__(self):
        self.m_GRILLE = GRILLE() # On fait appel ici à la classe GRILLE() créee auparavant qu'on affecte à la variable m_GRILLE()
        self.m_PieceCourante = None    # Initialisation de la variable m_PieceCourante à laquelle définie aucune valeur
        self.m_SuivantePiece = Piece()  # On fait appel ici à la classe Piece() créee auparavant qu'on affecte à la variable m_SuivantePiece()
        self.m_piecechutes = False      # Définition de la variable m_piecechutes contenant des valeurs fausses (false ou 0)
        self.m_gameOver = False         # Définition de la variable m_gameOver contenant des valeurs fausses (false ou 0)
        self.m_direction = {'left' : False, 'right' : False, 'down' : False} # Création d'un dictionnaire m_direction contenant des
        # clés avec des valeurs fausses
        self.image=pygame.image.load("index.jpeg").convert()
        self.m_rotate = False # Définition de la variable m_rotate contenant des valeurs fausses (false ou 0)
        self.m_DernierrechuteTime = time.time() # Définition de la variable m_DernierchuteTime contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors de la chute d'une pièce
        self.m_DernierTempsMOuv = time.time()   # Définition de la variable m_DernierTempsMouv contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors du mouvement de la d'une pièce
        self.Vic="  "
        self.m_score = 0    # Initialisation de la variable m_score à 0
        self.m_niveau = 1
        self.plateau1=pygame.Surface((300,553))
        self.plateau2=pygame.Surface((300,553))
        self.m_score2 = 0 
        self.bigText = pygame.font.SysFont('PLANK___.TTF', 36)
        self.title_text = self.bigText.render("J2: "+str(self.m_score2),
                                    True, VERT)
        self.bigText2 = pygame.font.SysFont('PLANK___.TTF', 36)
        self.title_text2 = self.bigText2.render("J1: "+str(self.m_score),
                                    True, VERT)
        self.bigText3 = pygame.font.SysFont('PLANK___.TTF', 36)
        self.title_text3 = self.bigText3.render("VAINQUEUR: "+str(self.Vic),
                                    True, VERT)
        self.plateau_score=pygame.Surface((800,600))

        self.JOUEUR1=" "
        self.JOUEUR2=" "
        self.m_GRILLE2 = GRILLE() # On fait appel ici à la classe GRILLE() créee auparavant qu'on affecte à la variable m_GRILLE()
        self.m_PieceCourante2 = None    # Initialisation de la variable m_PieceCourante à laquelle définie aucune valeur
        self.m_SuivantePiece2 = Piece2()  # On fait appel ici à la classe Piece() créee auparavant qu'on affecte à la variable m_SuivantePiece()
        self.m_piecechutes2 = False      # Définition de la variable m_piecechutes contenant des valeurs fausses (false ou 0)
        self.m_gameOver = False         # Définition de la variable m_gameOver contenant des valeurs fausses (false ou 0)
        self.m_direction2 = {'gauche' : False, 'droite' : False, 'bas' : False} # Création d'un dictionnaire m_direction contenant des
        # clés avec des valeurs fausses
        self.m_rotate2 = False # Définition de la variable m_rotate contenant des valeurs fausses (false ou 0)
        self.m_DernierrechuteTime2 = time.time() # Définition de la variable m_DernierchuteTime contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors de la chute d'une pièce
        self.m_DernierTempsMOuv2 = time.time()   # Définition de la variable m_DernierTempsMouv contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors du mouvement de la d'une pièce
           # Initialisation de la variable m_score à 0

        self.m_niveau2 = 1
        pygame.init()   # initialiser tous les modules pygame importés
        self.boite = pygame.display.set_mode((BOITE_LARGEUR * 6, BOITE_LONGUEUR*3)) # Initialisation de l'écran pour l'affichage
        # Cette fonction créera une surface d'affichage. Les arguments transmis sont des demandes pour un type d'affichage.
        # L’affichage créé sera la meilleure correspondance possible prise en charge par le système.
        pygame.display.set_caption('Turner Teen') # Obtenir la légende de la fenêtre en cours


            
    
    def logic(self):


        if time.time() - self.m_DernierTempsMOuv > 0.1:
            if self.m_direction['left'] == True:
            #
            #si la touche gauche est appuyée physiquement la directionde la piece va dans
            #la direction gauche de a grille d'ou l'utilisation du signe (-) négatif
            #qui indique le sens contraire en considerant que sin on part de la gauche vers la droite
            #on part dans le sens positif sinon dans le sens négatif
            #
                self.m_PieceCourante.bouger(-TAILLE_BOITE, 0, self.m_GRILLE)

            elif self.m_direction['right'] == True:

                self.m_PieceCourante.bouger(TAILLE_BOITE, 0, self.m_GRILLE)

            elif self.m_direction['down'] == True:
            #
            #si la touche directiont haut est appuyée physiquement la piece suivante va dans le sens positif (+) de la grille
            #c'est a dire de la gauche vers la droite
            #
                self.m_PieceCourante.bouger(0, TAILLE_BOITE, self.m_GRILLE)

            self.m_DernierTempsMOuv = time.time()

        elif self.m_rotate:
            self.m_PieceCourante.rotation(self.m_GRILLE)
            self.m_rotate = False



    def logic2(self):


        if time.time() - self.m_DernierTempsMOuv2 > 0.1:
            if self.m_direction2['gauche'] == True:
            #
            #si la touche gauche est appuyée physiquement la directionde la piece va dans
            #la direction gauche de a grille d'ou l'utilisation du signe (-) négatif
            #qui indique le sens contraire en considerant que sin on part de la gauche vers la droite
            #on part dans le sens positif sinon dans le sens négatif
            #
                self.m_PieceCourante2.bouger2(-TAILLE_BOITE, 0, self.m_GRILLE2)

            elif self.m_direction2['droite'] == True:

                self.m_PieceCourante2.bouger2(TAILLE_BOITE, 0, self.m_GRILLE2)

            elif self.m_direction2['bas'] == True:
            #
            #si la touche directiont haut est appuyée physiquement la piece suivante va dans le sens positif (+) de la grille
            #c'est a dire de la gauche vers la droite
            #
                self.m_PieceCourante2.bouger2(0, TAILLE_BOITE, self.m_GRILLE2)

            self.m_DernierTempsMOuv2 = time.time()

        elif self.m_rotate2:
            self.m_PieceCourante2.rotation(self.m_GRILLE2)
            self.m_rotate2 = False





    def texte(self, text, font):
        texteSurface = font.render(text, True, VERT) # On affecte à la variable texteSurface la fonction pygame font.render avec laquelle on pourra
        # créer un nouvel objet à partir d'un fichier.
        return texteSurface, texteSurface.get_rect()    # On retourne ici la variable texteSurface et, on retourne aussi cette variable associée avec
        # la fonction pygame get_rect() qui retourne un nouveau rectangle couvrant toute la surface.

    def vainqueur(self):
        if self.m_score2 >self.m_score and self.m_score2!=self.m_score:
            self.Vic=self.JOUEUR2

        elif self.m_score2<self.m_score and self.m_score2!=self.m_score:
            self.Vic=self.JOUEUR1


        if self.m_score2==self.m_score:
            self.Vic="EGALITE"
           
     
    
        
    def afficheScore(self):
        self.vainqueur()
        font4 = pygame.font.Font('04B_30__.TTF', 17) # On affecte à la variable font la fonction pygame font.Font qui crée un nouvel objet Font
        # à partir d'un fichier. Ce fichier Font se constitue du nom de la police ainsi que de sa taille
        textSurf7, textRect7 = self.texte(str(self.JOUEUR2) +"  "+ str(self.m_score2), font4)
        textRect7.center = (BOITE_LARGEUR + 2.85* BOITE_LARGEUR , BOITE_LONGUEUR / 4)

        textSurf3, textRect3 = self.texte(str(self.JOUEUR1)+"  "  + str(self.m_score), font4)
        textRect3.center = (BOITE_LARGEUR + 1.2 * BOITE_LARGEUR , BOITE_LONGUEUR /4 )

        textSurf2, textRect2 = self.texte(' VAINQUEUR : '+ str(self.Vic), font4)
        textRect2.center = (BOITE_LARGEUR + 2 * BOITE_LARGEUR, BOITE_LONGUEUR / 1.2)
        self.boite.blit(textSurf7, textRect7)
        self.boite.blit(textSurf2, textRect2)
        self.boite.blit(textSurf3, textRect3)
        pygame.display.update()
    
    def dessinelements(self):
#Fonction dessin de la grille de la piece suivante de la grille et de l'interface graphique
        self.afficheScore()
        self.boite.fill((BLANC))
#Couleur de fond de la BOITE en noir
        self.plateau_score.fill((VERT))
#dessin des lignes  et des colone de la grille
        self.plateau1.fill((col))
        self.plateau2.fill((col))
        
        pygame.draw.rect(self.boite,VERT,[550,10,700,600],8)
  
        self.m_GRILLE.dessinergrille(self.plateau1)
        self.m_GRILLE2.dessinergrille(self.plateau2)
        self.m_PieceCourante.dessinerpiece(self.plateau1)
        self.m_SuivantePiece.dessinerpiece(self.boite)
#contour de la premiere grille 
        pygame.draw.line(self.boite,ROUGE,(4,12),(335,12),15)
        pygame.draw.line(self.boite,ROUGE,(4,580),(335,580),15)
        pygame.draw.line(self.boite,ROUGE,(11,12),(11,580),15)
        pygame.draw.line(self.boite,ROUGE,(328,12),(328,580),15)
        #
        pygame.draw.line(self.boite,ROUGE,(1435,12),(1757,12),15)
        pygame.draw.line(self.boite,ROUGE,(1435,580),(1757,580),15)
        pygame.draw.line(self.boite,ROUGE,(1442,14),(1442,584),15)
        pygame.draw.line(self.boite,ROUGE,(1758,5),(1758,588),15)        
        self.m_PieceCourante2.dessinerpiece2(self.plateau2)
        self.m_SuivantePiece2.dessinerpiece2(self.boite)
        #self.boite.blit(self.title_text,(1100,90))
        #self.boite.blit(self.title_text2,(600,90))
        #self.boite.blit(self.title_text3,(775,500))
        
        self.boite.blit(self.image,(770,210))
        self.boite.blit(self.plateau1, (20,20))
        self.boite.blit(self.plateau2, (1450,20))
        #self.afficheScore()
        #self.afficheScore()
#raffarichissement du score
        pygame.display.update()
#dessin de la grille piece suivante grille et score
#appel de la fonction MiseaJour qui permet de raffraichir la BOITE a chaque fois
    def entreeDonnees(self):

        for event in pygame.event.get():
#definition de l'evenenment defaite si la grille est remplie la ligne suivante ferme directement le programme
#ainsi game_over =true
            if event.type == pygame.QUIT:
                self.m_gameOver = True
#definition des evenement liés aux commandes du jeu
            #
            #lorsque l'utilisateur appuie sur le touche du bas il est possible pur lui de deplacer la piece avec les touches directionnelles
            #gauche droite bas et espace qui utilise la rotation du coup on assigena ces  vraiables la valeur True
            #
            if event.type == pygame.KEYDOWN:
#Detecte si la touche direction du bas est appuyée physiquement
                if event.key == pygame.K_LEFT:
                    self.m_direction2['gauche'] = True
                    
                elif event.key == pygame.K_RIGHT:
                    self.m_direction2['droite'] = True
                    
                elif event.key == pygame.K_DOWN:
                    self.m_direction2['bas'] = True
                    
                elif event.key == pygame.K_RCTRL:
                    self.m_rotate2 = True
                elif event.key == pygame.K_ESCAPE:
                    self.m_gameOver = True
            
            




            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:                   
                    self.m_direction['left'] = True
                elif event.key == pygame.K_d:
                    self.m_direction['right'] = True                    
                elif event.key == pygame.K_s:              
                    self.m_direction['down'] = True
                elif event.key == pygame.K_n:
                    self.m_rotate = True
                elif event.key == pygame.K_ESCAPE:
                    self.m_gameOver = True
            #la touche direction du haut n'a aucun role ici
            #
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.m_direction2['gauche'] = False
                elif event.key == pygame.K_RIGHT:
                    self.m_direction2['droite'] = False
                elif event.key == pygame.K_DOWN:
                    self.m_direction2['bas'] = False

            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_q:
                    self.m_direction['left'] = False
                elif event.key == pygame.K_d:
                    self.m_direction['right'] = False
                elif event.key == pygame.K_s:
                    self.m_direction['down'] = False
   

    def MiseaJour(self):
#le module time.time() permet de mesurer la durée entre deux evenement
#il represente aussi le "EPOCH" explication dans le rapport...

        if time.time() - self.m_DernierrechuteTime > .2:
#on verifie si le nombre de secondes ecoulées
#jusqu'a la chute dela derniere piece est superieure a 1
#
            if self.m_piecechutes:
                if self.m_PieceCourante.bouger(0, TAILLE_BOITE, self.m_GRILLE): # A revoir pygame doc !!!!!!!!!!!!!!!!
                    pass
#
#On teste si la piece est en pleine chute si oui on passe


                else:
                    self.m_piecechutes = False
                    self.m_GRILLE.AjoutELEMENT(self.m_PieceCourante) # On ajoute la pièce à la grille tant qu'elle n'est pas en mouvement
                    self.m_score += (self.m_GRILLE.effaceLigneComplete())*25  # On ajoute 10 au score à chaque fois qu'une ligne est effacée.

                self.m_DernierrechuteTime = time.time()

        if not self.m_piecechutes:
            self.m_PieceCourante = self.m_SuivantePiece # Si il n'y a aucune pièce en chute, on affiche dans la grille la prochaine pièce
            self.m_SuivantePiece = Piece()
            self.m_PieceCourante.setPos(int(BOITE_LARGEUR / 2) - 50, 0) # Centre la pièce dans la grille par rapport à sa largeur
            self.m_piecechutes = True
            if not self.m_PieceCourante.descenteValide(0, 0, self.m_GRILLE):
                self.m_gameOver = True

    def MiseaJour2(self):

#le module time.time() permet de mesurer la durée entre deux evenement
#il represente aussi le "EPOCH" explication dans le rapport...
        if time.time() - self.m_DernierrechuteTime2 > .2:
#on verifie si le nombre de secondes ecoulées
#jusqu'a la chute dela derniere piece est superieure a 1
#
            if self.m_piecechutes2:
                if self.m_PieceCourante2.bouger2(0, TAILLE_BOITE, self.m_GRILLE2): # A revoir pygame doc !!!!!!!!!!!!!!!!
                    pass#

#
#On teste si la piece est en pleine chute si oui on passe


                else:
                    self.m_piecechutes2 = False
                    self.m_GRILLE2.AjoutELEMENT(self.m_PieceCourante2) # On ajoute la pièce à la grille tant qu'elle n'est pas en mouvement
                    self.m_score2 += (self.m_GRILLE2.effaceLigneComplete())*25  # On ajoute 10 au score à chaque fois qu'une ligne est effacée.

                self.m_DernierrechuteTime2 = time.time()

        
       

        if not self.m_piecechutes2:
            self.m_PieceCourante2 = self.m_SuivantePiece2 # Si il n'y a aucune pièce en chute, on affiche dans la grille la prochaine pièce
            self.m_SuivantePiece2 = Piece2()
            self.m_PieceCourante2.setPos(int(BOITE_LARGEUR / 2) - 50, 0) # Centre la pièce dans la grille par rapport à sa largeur
            self.m_piecechutes2 = True
            if not self.m_PieceCourante2.descenteValide(0, 0, self.m_GRILLE2):
                self.m_gameOver = True
        

    def confrontation(self):
        if self.m_score>=75 and self.m_score2>=75:
            PIECES['OB']=OB3_FORME 
        if self.m_score>=150 and self.m_score2>=150:
            PIECES['LLC']=L_C

        if self.m_score>=200 and self.m_score2>=200:
            PIECES['G']=G_C 

    

    

    def Lancement(self):
        self.JOUEUR1 = input('Entrez votre nom : ')
        self.JOUEUR2= input('Nom du second joueur : ')         


        while not self.m_gameOver:
            self.MiseaJour()
            self.confrontation()
            self.entreeDonnees()
            self.logic()
            self.afficheScore()
            self.MiseaJour2()
            self.logic2()    
            self.dessinelements()
