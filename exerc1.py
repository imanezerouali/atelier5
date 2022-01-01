# classe
class Vecteur2D:
        #Les Vecteurs plans
        def __init__(self, x0=0, y0=0): #Constructeur avec parametres par defaut."""
                self.x = x0 # initialisation de x et y, attributs d'instance
                self.y = y0
                self.nom = " "
        def affiche(self):
                print(self.nom)   #Utilisation du print
        def __str__(self):
               return "x = %d, y = %d" % (self.x,self.y)

# Auto-test
if __name__ == '__main__':
        print("une instance par defaut ".center(30))
        print(Vecteur2D())
        print("une instance initialisee ".center(10))
        print(Vecteur2D(9, 3))
        Vecteur2D().affiche()