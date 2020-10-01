from GRILLE import *
from SOLO import *

from Pieces import *
from pygame.locals import *
import pygame
import sys
import pygame.mixer
pygame.init()

BLACK = 0, 0, 0
WHITE = 255, 255, 255
CIEL = 0, 200, 255
RED = 255, 0, 0
ORANGE = 255, 100, 0
GREEN = 0, 255, 0


class Button:
    '''Ajout d'un bouton avec un texte sur img
    Astuce: ajouter des espaces dans les textes pour avoir une même largeur
    de boutons
    dx, dy décalage du bouton par rapport au centre
    action si click
    Texte noir
    '''

    def __init__(self, fond, text, color, font, dx, dy):
        self.fond = fond
        self.text = text
        self.color = color
        self.font = font
        self.position = dx, dy
        self.action = False  # enable or not
        self.titre = self.font.render(self.text, True, BLACK)
        textpos = self.titre.get_rect()
        textpos.centerx = self.fond.get_rect().centerx + self.position[0]
        textpos.centery = self.position[1]
        self.textpos = [textpos[0], textpos[1], textpos[2], textpos[3]]
        self.rect = pygame.draw.rect(self.fond, self.color, self.textpos)
        self.fond.blit(self.titre, self.textpos)

    def update_button(self, fond, action=None):
        self.fond = fond
        mouse_xy = pygame.mouse.get_pos()
        over = self.rect.collidepoint(mouse_xy)
        if over:
            action()
            if self.color == RED:
                self.color = GREEN
                self.action = True
            elif self.color == GREEN:
                # sauf les + et -, pour que ce soit toujours vert
                if len(self.text) > 5:  # 5 char avec les espaces
                    self.color = RED
                self.action = False
        # à la bonne couleur
        self.rect = pygame.draw.rect(self.fond, self.color, self.textpos)
        self.fond.blit(self.titre, self.textpos)

    def dessiner_boutton(self, fond):
        self.fond = fond
        self.rect = pygame.draw.rect(self.fond, self.color, self.textpos)
        self.fond.blit(self.titre, self.textpos)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1400, 1000))
        self.m_gameOver = Multijoueur()
        self.loop = True

        # Définition de la police
        self.big = pygame.font.SysFont('baby_blocks.ttf', 150)
        self.small = pygame.font.SysFont('freesans', 36)
        self.normal = pygame.font.SysFont('upheavtt.ttf', 100)

        self.creer_fond()
        self.creer_boutton()
        pygame.display.update()
    def update_textes(self):
        self.textes = [["TETRIS", VERT, self.big, 0, 90]]

    def creer_fond(self):
        # Image de la taille de la fenêtre
        self.fond = pygame.Surface(self.screen.get_size())
        # En bleu
        self.fond.fill(CIEL)

    def creer_boutton(self):
        self.MULTIJOUEUR_button = Button(self.fond, "   MULTIJOUEUR   ", RED, self.normal, 0, 380)
        self.SOLO_button = Button(self.fond, "   SOLO   ", RED, self.normal, 0, 530)
        self.quit_button = Button(self.fond, "   QUITTER   ", RED, self.normal, 0, 680)

    def son(self):
        pygame.init()
        pygame.mixer.music.load("son_turner_teen.oga")        
        pygame.mixer.music.play(-1)
    def display_text(self, text, color, font, dx, dy):
        '''Ajout d'un texte sur fond. Décalage dx, dy par rapport au centre.
        '''
        mytext = font.render(text, True, color)  # True pour antialiasing
        textpos = mytext.get_rect()
        textpos.centerx = self.fond.get_rect().centerx + dx
        textpos.centery = dy
        self.fond.blit(mytext, textpos)

    def lancement_menu(self):
        while self.loop:
            self.creer_fond()
   
            # Boutons
            self.MULTIJOUEUR_button.dessiner_boutton(self.fond)
            self.SOLO_button.dessiner_boutton(self.fond)
            self.quit_button.dessiner_boutton(self.fond)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.MULTIJOUEUR_button.update_button(self.fond, action=MULTIJOUEUR)
                    self.SOLO_button.update_button(self.fond, action=SOLO)
                    self.quit_button.update_button(self.fond, action=gamequit)

            self.update_textes()
            for text in self.textes:
                self.display_text(text[0], text[1], text[2],
                                  text[3], text[4])

            # Ajout du fond dans la fenêtre
            self.screen.blit(self.fond, (0, 0))
            # Actualisation de l'affichage
            # self.fin_de_partie()
            pygame.display.update()
            # 10 fps


def MULTIJOUEUR():
    print("MULTIJOUEUR")
    v=Multijoueur()
    v.Lancement()

def SOLO():
    print("SOLO")
    c = Solo()
    c.Lancement()


def gamequit():
    print("Quit")
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    game = Game()
    game.lancement_menu()
class Multijoueur(object):
    def __init__(self):
        self.pieceS=pygame.Surface((150,500))
        self.m_GRILLE = GRILLE() 
        # On fait appel ici à la classe GRILLE() créee auparavant qu'on affecte à la variable m_GRILLE()
        self.m_PieceCourante = None    
        # Initialisation de la variable m_PieceCourante à laquelle définie aucune valeur
        self.m_SuivantePiece = Piece()  
        # On fait appel ici à la classe Piece() créee auparavant qu'on affecte à la variable m_SuivantePiece()
        self.m_piecechutes = False      
        # Définition de la variable m_piecechutes contenant des valeurs fausses (false ou 0)
        self.m_gameOver = False        
         # Définition de la variable m_gameOver contenant des valeurs fausses (false ou 0)
        self.m_direction = {'left' : False, 'right' : False, 'down' : False} 
        # Création d'un dictionnaire m_direction contenant des
        # clés avec des valeurs fausses
        self.image=pygame.image.load("index.jpeg").convert()
        self.m_rotate = False
         # Définition de la variable m_rotate contenant des valeurs fausses (false ou 0)
        self.m_DernierrechuteTime = time.time() 
        # Définition de la variable m_DernierchuteTime contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors de la chute d'une pièce
        self.m_DernierTempsMOuv = time.time()   
        # Définition de la variable m_DernierTempsMouv contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors du mouvement de la d'une pièce
        self.Vic="  "
        self.m_score = 0    
        # Initialisation de la variable m_score à 0
        self.m_niveau = 1
        self.plateau1=pygame.Surface((300,553))
        self.plateau2=pygame.Surface((300,553))
        self.m_score2 = 0 
        self.bigText = pygame.font.SysFont('04B_30__.TTF', 36)
        self.title_text = self.bigText.render("J2: "+str(self.m_score2),
                                    True, VERT)
        self.bigText2 = pygame.font.SysFont('04B_30__.TTF', 36)
        self.title_text2 = self.bigText2.render("J1: "+str(self.m_score),
                                    True, VERT)
        self.bigText3 = pygame.font.SysFont('04B_30__.TTF', 36)
        self.title_text3 = self.bigText3.render("VAINQUEUR: "+str(self.Vic),
                                    True, VERT)
        self.plateau_score=pygame.Surface((800,600))
       
        self.m_GRILLE2 = GRILLE() 
        # On fait appel ici à la classe GRILLE() créee auparavant qu'on affecte à la variable m_GRILLE()
        self.m_PieceCourante2 = None    
        # Initialisation de la variable m_PieceCourante à laquelle définie aucune valeur
        self.m_SuivantePiece2 = Piece2()  
        # On fait appel ici à la classe Piece() créee auparavant qu'on affecte à la variable m_SuivantePiece()
        self.m_piecechutes2 = False      
        # Définition de la variable m_piecechutes contenant des valeurs fausses (false ou 0)
        self.m_gameOver2 = False        
         # Définition de la variable m_gameOver contenant des valeurs fausses (false ou 0)
        self.m_direction2 = {'gauche' : False, 'droite' : False, 'bas' : False}
         # Création d'un dictionnaire m_direction contenant des
        # clés avec des valeurs fausses
        self.m_rotate2 = False 
        # Définition de la variable m_rotate contenant des valeurs fausses (false ou 0)
        self.m_DernierrechuteTime2 = time.time() 
        # Définition de la variable m_DernierchuteTime contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors de la chute d'une pièce
        self.m_DernierTempsMOuv2 = time.time()   
        # Définition de la variable m_DernierTempsMouv contenant la fonction time du module time
        # qui nous permettra de récupérer le temps actuel écoulé (en seconde) lors du mouvement de la d'une pièce
           # Initialisation de la variable m_score à 0
        self.J1=" JOUEUR 1 "
        self.J2=" JOUEUR 2 "
        self.m_niveau2 = 1
        self.imageW=pygame.image.load("win.png").convert()
        self.imageL=pygame.image.load("lose.png").convert()
        pygame.init()   
        # initialiser tous les modules pygame importés
        self.boite = pygame.display.set_mode((GRILLE_LARGEUR * 6, GRILLE_LONGUEUR*3)) 
        # Initialisation de l'écran pour l'affichage
        # Cette fonction créera une surface d'affichage. Les arguments transmis sont des demandes pour un type d'affichage.
        # L’affichage créé sera la meilleure correspondance possible prise en charge par le système.
        pygame.display.set_caption('Turner Teen') 
        # Obtenir la légende de la fenêtre en cours


            
    
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
      
        texteSurface = font.render(text, True, VERT) 
        return texteSurface, texteSurface.get_rect()    
        # On retourne ici la variable texteSurface et, on retourne aussi cette variable associée avec
       

    def victoire(self):
        if self.m_score2 >self.m_score and self.m_score2!=self.m_score:
            self.Vic=self.J2

        elif self.m_score2<self.m_score and self.m_score2!=self.m_score:
            self.Vic=self.J1

        if self.m_score2==self.m_score:
            self.Vic="EGALITE"
            
        while self.m_score2 >self.m_score and self.m_score2!=self.m_score and self.m_gameOver2==True and self.m_gameOver==False:
            self.Vic=self.J2
        while self.m_score2 <self.m_score and self.m_score2!=self.m_score and self.m_gameOver2==False and self.m_gameOver==True:
            self.Vic=self.J1
        if self.m_gameOver ==True and self.m_gameOver2==True:
            if self.m_gameOver ==True and self.m_gameOver2==True and self.m_score2 >self.m_score and self.m_score2!=self.m_score:
                print("VICTOIRE DU",self.J2)

            elif self.m_gameOver ==True and self.m_gameOver2==True and self.m_score2<self.m_score and self.m_score2!=self.m_score:
                print("VICTOIRE DU",self.J1)
            
            elif self.m_gameOver ==True and self.m_gameOver2==True and self.m_score2==self.m_score:
                print("EGALITE")
        return self.Vic
           
     

        
    def afficheScore(self):
        
        
        self.victoire()
        font4 = pygame.font.Font('04B_30__.TTF', 18) 
        # On affecte à la variable font la fonction pygame font.Font qui crée un nouvel objet Font
        # à partir d'un fichier. Ce fichier Font se constitue du nom de la police ainsi que de sa taille
        textSurf7, textRect7 = self.texte(str(self.J1) + str(self.m_score2), font4)
        textRect7.center = (GRILLE_LARGEUR + 2.85* GRILLE_LARGEUR , GRILLE_LONGUEUR / 4)

        textSurf3, textRect3 = self.texte(str(self.J2) + str(self.m_score), font4)
        textRect3.center = (GRILLE_LARGEUR + 1.2 * GRILLE_LARGEUR , GRILLE_LONGUEUR /4 )

        textSurf2, textRect2 = self.texte(' VAINQUEUR : '+ str(self.Vic), font4)
        textRect2.center = (GRILLE_LARGEUR + 2 * GRILLE_LARGEUR, GRILLE_LONGUEUR / 1.2)
        self.boite.blit(textSurf7, textRect7)
        self.boite.blit(textSurf2, textRect2)
        self.boite.blit(textSurf3, textRect3)
        pygame.display.update()
    def dessinelements(self):

#Fonction dessin de la grille de la piece suivante de la grille et de l'interface graphique
        self.afficheScore()
        self.boite.fill((BLANC))
#Couleur de fond de la GRILLE en noir
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
        if self.m_gameOver2==True:
                
                self.boite.blit(self.imageL,(1450,100))  
         
                self.pieceS.fill((BLANC))
                self.boite.blit(self.pieceS,(1280,10))
        if self.m_gameOver==True:
                self.boite.blit(self.imageL,(30,100))  
                           
                self.pieceS.fill((BLANC))
                self.boite.blit(self.pieceS,(365,10))
        #self.afficheScore()
        #self.afficheScore()
#raffarichissement du score
        pygame.display.update()
#dessin de la grille piece suivante grille et score
#appel de la fonction MiseaJour qui permet de raffraichir la GRILLE a chaque fois
    def entreeDonnees(self):

        for event in pygame.event.get():
#definition de l'evenenment defaite si la grille est remplie la ligne suivante ferme directement le programme
#ainsi game_over =true
            if event.type == pygame.QUIT:
                self.m_gameOver = True
                self.m_gameOver2 = True
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
                    self.m_gameOver2 = True
            
            




            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:                   
                    self.m_direction['left'] = True
                elif event.key == pygame.K_d:
                    self.m_direction['right'] = True                    
                elif event.key == pygame.K_s:              
                    self.m_direction['down'] = True
                elif event.key == pygame.K_z:
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
                if self.m_PieceCourante.bouger(0, TAILLE_BOITE, self.m_GRILLE):
                    pass 
#On teste si la piece est en pleine chute si oui on passe
                else:
                    self.m_piecechutes = False
                    self.m_GRILLE.AjoutELEMENT(self.m_PieceCourante) 
                    # On ajoute la pièce à la grille tant qu'elle n'est pas en mouvement
                    self.m_score += (self.m_GRILLE.effaceLigneComplete())*25  
                    # On ajoute 10 au score à chaque fois qu'une ligne est effacée.

                self.m_DernierrechuteTime = time.time()

        if not self.m_piecechutes:
            self.m_PieceCourante = self.m_SuivantePiece 
            # Si il n'y a aucune pièce en chute, on affiche dans la grille la prochaine pièce
            self.m_SuivantePiece = Piece()
            self.m_PieceCourante.setPos(int(GRILLE_LARGEUR / 2) - 50, 0) 
            # Centre la pièce dans la grille par rapport à sa largeur
            self.m_piecechutes = True
            if not self.m_PieceCourante.descenteValide(0, 0, self.m_GRILLE):
                self.m_gameOver = True
            if self.m_gameOver==True:
                self.plateau1=pygame.Surface((1,1))
                

    def MiseaJour2(self):

#le module time.time() permet de mesurer la durée entre deux evenement
#il represente aussi le "EPOCH" explication dans le rapport...
        if time.time() - self.m_DernierrechuteTime2 > .2:
#on verifie si le nombre de secondes ecoulées
#jusqu'a la chute dela derniere piece est superieure a 1
#
            if self.m_piecechutes2:
                if self.m_PieceCourante2.bouger2(0, TAILLE_BOITE, self.m_GRILLE2): 
             
                    pass
            #On teste si la piece est en pleine chute si oui on passe


                else:
                    self.m_piecechutes2 = False
                    self.m_GRILLE2.AjoutELEMENT(self.m_PieceCourante2) 
                    # On ajoute la pièce à la grille tant qu'elle n'est pas en mouvement
                    self.m_score2 += (self.m_GRILLE2.effaceLigneComplete())*25 
                     # On ajoute 10 au score à chaque fois qu'une ligne est effacée.

                self.m_DernierrechuteTime2 = time.time()

        
       

        if not self.m_piecechutes2:
            self.m_PieceCourante2 = self.m_SuivantePiece2 
            # Si il n'y a aucune pièce en chute, on affiche dans la grille la prochaine pièce
            self.m_SuivantePiece2 = Piece2()
            self.m_PieceCourante2.setPos(int(GRILLE_LARGEUR / 2) - 50, 0) 
            # Centre la pièce dans la grille par rapport à sa largeur
            self.m_piecechutes2 = True
            if not self.m_PieceCourante2.descenteValide(0, 0, self.m_GRILLE2):
                self.m_gameOver2 = True
                
            if self.m_gameOver2==True:
                self.plateau2=pygame.Surface((1,1))
                  



        

    def confrontation(self):
        if self.m_score>=75 and self.m_score2>=75:
            PIECES['OB']=OB3_FORME 
        if self.m_score>=150 and self.m_score2>=150:
            PIECES['LLC']=L_C

        if self.m_score>=200 and self.m_score2>=200:
            PIECES['G']=G_C 

    def gameOver(self):

        while self.m_gameOver:

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #pygame.quit()
                    self.m_gameOver = True
                    game = Game()
                    game.lancement_menu()
            
            
        
            self.boite.blit(self.imageL,(200,450))
            
            pygame.display.update()

        


  



    def Lancement(self):
    
        #self.J1=input("NOM DU PREMIER JOUEUR ")
        #self.J2=input("NOM DU SECOND JOUEUR ")
        #print("QUE LE MEILLEUR GAGNE ")
        

        while not self.m_gameOver:
            

            self.MiseaJour()
            self.confrontation()
            self.entreeDonnees()
            self.logic()
            self.afficheScore()
            self.MiseaJour2()
            self.logic2()    
            self.dessinelements()
            #self.gameOver()
        while not self.m_gameOver2:
            


            self.confrontation()
            self.entreeDonnees()

            self.afficheScore()
            self.MiseaJour2()
            self.logic2()    
            self.dessinelements()
            #self.gameOver()
        
            
