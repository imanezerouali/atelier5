class module:
    def __init__(self,string,volume,):
        self.nom=nom
        self.volume_horarire=volume_horaire
        self.semestre=semestre
    def getnom(self):
        return self.nom
    def getvolume_horaire(self):
        return self.volume_horaire
    def getsemestre(self):
        return self.ksemestre
class utilisateur:
    def __init__(self,nom,email,mot_de_passse,genre,age):
        self._nom=nom
        self._email=email
        self._mot_de_passe=mot_de_passe
        self._genre=genre
        self._age=age
class etudiant(utilisateur):
    def __init__(self,code_massar):
        self.code_massar=code_massar

class professeur(utilisateur):
    def __init__(self,ppr,grade):
        self.ppr=ppr
        slef.grade=grade
    def getppr(self):
        return self.ppr
    def getgrade(self):
        return self.grade
class matiere:
    def __init__(self,nom,pourcentage):
        self.nom=nom
        self.pourcentage=pourcentage
    def getnom(self):
        return self.nom
    def getpourcentage(self):
        return self.pourcentage
class evaluation:
    def __init__(self,note):
        slef.note=note
    def getnote(self):
        return self.note