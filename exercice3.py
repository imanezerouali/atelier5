
class Rectangle:
        #classe des rectangles

        def __init__(self, longueur=30, largeur=15): #creation de constructeur
                #Initialisation avec valeurs par defaut
                self.lon = longueur
                self.lar = largeur
                self.nom = "rectangle"
        def surface(self):
                return self.lon*self.lar  #Retourne la surface d'un rectangle
        def show(self):
                print("\nLe %s de cotes %d et %d a une surface de %d" %(self.nom, self.lon, self.lar, self.surface()))
class Carre(Rectangle): #classe des carres qui herite de la classe Rectangle

        def __init__(self, cote=9): #Constructeur avec valeur par defaut
                Rectangle.__init__(self, cote, cote)
                self.nom = "carre" # surchage d'attribut d'instance

        def show(self):
                print("\nLe %s de cote %d a une surface de %d" % (self.nom, self.lar, self.surface()))
        # Auto-test
r = Rectangle(7, 4)
r.show()
c = Carre()
c.show()