class Etudiant :
    def __init__(self, nom, age, cne,moyenne):
        self.nom = nom
        self.age = age
        self.cne= cne
        self.moyenne=moyenne
Etudiant1 = Etudiant('imane', 22, 'k13556838',15)
Etudiant2 = Etudiant('salma', 34,'lb5568356',13)
Etudiant3= Etudiant('basma', 18,'m78643679',16)
Etudiant4= Etudiant('mariam', 77,'j08564631',18)
liste = [Etudiant1, Etudiant2, Etudiant3, Etudiant4]
#liste.sort(key=lambda x: x.nom)
#print([item.nom for item in liste])
print('voici la liste triee selon l age:')
liste.sort(key=lambda x: x.age)
print([item.nom  for item in liste])

liste.sort(key=lambda x: x.moyenne)
print("voici la liste triee selon la moyenne:")
print([item.nom  for item in liste])