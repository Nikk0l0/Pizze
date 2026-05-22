import math

class Pizza:
    def __init__(self, diametro):
        self.diametro = diametro
    
    def area(self):
        return  (self.diametro / 2 ) ** 2 * math.pi

    def __str__(self):
        return f"Pizza {self.diametro} di diametro"

    def __repr__(self):
        return f"Pizza {self.diametro} di diametro"

class Patatosa(Pizza):
    def __init__(self, diametro, patate):
        super().__init__(diametro)
        self.patate = patate

    def __str__(self):
        #return f"{super().__str__} + , patate {self.patate}"
        return f"Pizza {self.diametro} di diametro, patate {self.patate}"

class Diavola(Pizza):
    def __init__(self,diametro,salame):
        super().__init__(diametro)
        self.salame=salame

    def __str__(self):
        #return f"{super().__str__} + , salame {self.salame}"
        return f"Pizza {self.diametro} di diametro, salame {self.salame}"

if __name__ == "__main__":
    prima = Pizza(4)
    print(prima.area())

    seconda = Patatosa(5, 12)
    #print(seconda)
    terza = Diavola(4, 5)

    lista = [prima, seconda, terza]
    
    for p in lista:
        print(p)
