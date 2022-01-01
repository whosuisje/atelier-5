class Vecteur2D:
    #constructeur parametres
    def __init__(self, x0=0, y0=0):
        self.x =x0
        self.y= y0
        #tester le programe
x1=Vecteur2D()
print("x = %d y = %d" % (x1.x, x1.y))
x2=Vecteur2D(10,12)
print("x = %d y = %d" % (x2.x, x2.y))
