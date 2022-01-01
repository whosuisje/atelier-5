class Point :
    #constructeur parametres
    def __init__(self, x=0.0,y=0.0):
        self.ptx =float(x)
        self.pty=float(y)
class Segment :
    #constructeur parametres
     def __init__(self,a,b,c,d):
         self.orig = Point(a,b)
         self.extrem = Point(c,d)
         #methode d'affichage
     def __str__(self) :
         return ("segment : [({0},{1}),({2},{3}))]".format(self.orig.ptx,self.orig.pty,self.extrem.ptx,self.extrem.pty))
#tester le programme
s=Segment(1,5,2,6)
print(s)