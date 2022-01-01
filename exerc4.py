class Point:
    #creer la classe point

    def __init__(self, x=0.0, y=0.0): #creer le constructeur parametre

        self.px = float(x) #initialisation de ses valeurs par defaut
        self.py = float(y)
class Segment: #creer la classe segment
    def __init__(self, x1, y1, x2, y2):

        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)
    #creer une methode pour l'affichage
    def show(self):
        print("\nSegment : [(%d, %d), (%d, %d)]" % (self.orig.px, self.orig.py, self.extrem.px, self.extrem.py))

# Auto-test ---------------------------------------------------------
s = Segment(1, 2, 3, 4)
s.show();