import time, random, pygame

from GRILLE import *
class Piece(object):
    def __init__(self): # Constructeur
        self.m_FORMEIndex = random.choice(list(PIECES.keys()))
        # self.m_FORMEIndex permet de sélectionner les pièces du jeu crées dans le dictionnaire formé à
        # l'aide de la méthode random.choice totu en sélectionnant les clés qui correspondent aux pièces du jeu.
        self.m_position = {'x' : int(GRILLE_LARGEUR+0.5*GRILLE_LARGEUR)-35, 'y' : GRILLE_LONGUEUR/3.5}
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
        en X dans l'affichage de la pièce suivante dans la GRILLE.
        """
        return self.m_position['x']


    def getPosY(self):
        """
        Retourne la variable (m_position['y']) définie dans le constructeur retourne ici les coordonnées
        en Y dans l'affichage de la pièce suivante dans la GRILLE.
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

        if (self.m_position['x'] + LARGEUR * TAILLE_BOITE) <= GRILLE_LARGEUR and self.descenteValide(0, 0, GRILLE):
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
        self.m_position = {'x' : int(GRILLE_LARGEUR+3.5*GRILLE_LARGEUR)-35, 'y' : GRILLE_LONGUEUR/3.5}
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
        en X dans l'affichage de la pièce suivante dans la GRILLE.
        """
        return self.m_position['x']


    def getPosY(self):
        """
        Retourne la variable (m_position['y']) définie dans le constructeur retourne ici les coordonnées
        en Y dans l'affichage de la pièce suivante dans la GRILLE.
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

        if (self.m_position['x'] + LARGEUR * TAILLE_BOITE) <= GRILLE_LARGEUR and self.descenteValide(0, 0, GRILLE):
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


