class Fraction:
    def __init__(self,a,b):

        nwd=Fraction.findNWD([a,b])
        if (a%nwd==0 and b%nwd==0):
            a=int(a/nwd)
            b=int(b/nwd)
            self.frac=[a,"/",b]
        else:
            self.frac=[a,"/",b]
        
    def __str__(other): # DRUKOWANIE 
        other=other.printFraction()
        wyraz=""
        for i in range(3):
            a=str(other[i])
            wyraz=wyraz+a
        return wyraz

    def __add__(self,other): # DODAWANIE
        other=other.printFraction()
        n_frac=[0,"/",0]

        if self.frac[2]==other[2]:
            n_frac[0]=self.frac[0]+other[0]
            n_frac[2]=other[2]
        else:
            
            n_frac[2]=self.frac[2]*other[2]
            n_frac[0]=self.frac[0]*other[2]+other[0]*self.frac[2]

        return Fraction(n_frac[0],n_frac[2])
                
    def __sub__(self,other): # ODEJMOWANIE 
        other=other.printFraction()
        n_frac=[0,"/",0]
        
        if self.frac[2]==other[2]:
            n_frac[0]=self.frac[0]-other[0]
            n_frac[2]=other[2]
        else:
            n_frac[2]=self.frac[2]*other[2]
            n_frac[0]=self.frac[0]*other[2]-other[0]*self.frac[2]
        return Fraction(n_frac[0],n_frac[2])

    
    def __mul__(self,other): # MNOŻENIE
        other=other.printFraction()
        n_frac=[0,"/",0]
        for i in range(3):
            if i!=1:
                n_frac[i]=self.frac[i]*other[i]
        return Fraction(n_frac[0],n_frac[2])


    def __truediv__(self,other): # DZIELENIE
        other=other.printFraction()
        n_frac=[0,"/",0]
        n_frac[0]=self.frac[0]*other[2]
        n_frac[2]=self.frac[2]*other[0]
        return Fraction(n_frac[0],n_frac[2])

        
    def printFraction(self): 
        return self.frac

    def compare(self,y):
        x = self.frac
        y=y.printFraction()
        a=[0,'/',0]
        b=[0,'/',0]


        if x[2]*(-1)>0:
            x[2]=x[2]*(-1)
            x[0]=x[0]*(-1)
        elif y[2]*(-1)>0:
            y[2]=y[2]*(-1)
            y[0]=y[0]*(-1)

        if x[2]==y[2]:
            if x[0]==y[0]:
                return('Ułamki są równe')
            elif x[0]>y[0]:
                return('Pierwszy ułamek jest większy')
            else:
                return('Drugi ułamek jest większy')
        else:
            a[2]=x[2]*y[2]
            b[2]=a[2]
            a[0]=x[0]*y[2]
            b[0]=y[0]*x[2]

            
            if a[0]==b[0]:
                return('Ułamki są równe')
            elif a[0]>b[0]:
                return('Pierwszy ułamek jest większy')
            else:
                return('Drugi ułamek jest większy')

    def getNum(self): # WYPISZ LICZNIK
        return self.frac[0]

    def getDem(self): # WYPISZ MIANOWNIK
        return self.frac[2]

    def findNWD(a):
        def nwd(a, b):
            while b:
                a, b = b, a%b
            return a
        dl=len(a)
        i=1
        nw=a[0]
        while i<dl:
            nw=nwd(nw,a[i])
            i+=1
        return nw
