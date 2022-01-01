class Rectangle:
    #parametre constructeur
     def __init__(self,l=10,a=3):
         self.lon=l
         self.lar=a
         self.val="rectangle"
    #methode de surface 
     def surface(self):
         return self.lon*self.lar
    #methode affichafe
     def __str__(self):
         return ("nom : {0} ,longeur={1} ,largeur={2},surface={3}".format(self.val,self.lon,self.lar,self.surface()))
         #class herite 
class Carre(Rectangle):
    def __init__(self,b=10):
        Rectangle.__init__(self,b, b)
        self.val="Carre"#surcharge 
        #tester le programme
r1=Rectangle(10,12)
print (r1)
c1=Carre(10)
print(c1)