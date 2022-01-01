class Etudiant:
    #constructeur 
   def __init__(self, nom="", prenom="", age=0, cne="", moyenne=0):
        self.nom=nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
        #retourne string 
   def __str__(self) :
       return ("nom={0},prenom={1},age={2},cne={3},moyenne={4}".format(self.nom, self.prenom,self.age,self.cne,self.moyenne))
       #creer objets
e1 = Etudiant("ahmad", "ahmad", 20, "p10224", 15)
e2 = Etudiant("hajar", "hajar", 12, "p54161", 15)
e3 = Etudiant("yacin", "yacin", 7, "p57144", 5)
e4 = Etudiant("ghas", "ghas 4", 17, "p26849", 16)
e5 = Etudiant("imad", "iamd", 17, "p23102", 16)
#creer list et ajouter les objet
ListEtudiants = []
ListEtudiants.append(e1)
ListEtudiants.append(e2)
ListEtudiants.append(e3)
ListEtudiants.append(e4)
ListEtudiants.append(e5)
#sort les elements
def MySort1(etudiant):
    return -etudiant.moyenne - etudiant.age
    #affichage
ListEtudiants.sort(key=MySort1)
for i in ListEtudiants:
    print(i)