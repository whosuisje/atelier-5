class Vecteur2D:

 def __init__(self, x1=0, y1=0):
  #constructeur parametres
    self.x = x1 
    self.y = y1
    #methode definition :addition 
 def __add__(self, other):

    return Vecteur2D(self.x+other.x, self.y+other.y)
        #methode definition :str il retourne a string pour afficher avec print
 def __str__(self):
    return "Vecteur(%d, %d)" %(self.x, self.y)
# tester notre programme
x1= Vecteur2D(1.2, 2.3)
x2 =Vecteur2D(12,10)
print(x1 + x2)
print(x1)
print(x2)
