import math

class Pizza:
    def __init__(self, diametro):
        self.diametro = diametro
    
    def area(self):
        return  (self.diametro / 2 ) ** 2 * math.pi

    def __str__(self):
        return f"Pizza {self.diametro} di diametro"

class Patatosa(Pizza):
    def __init__(self, diametro, patate):
        super().__init__(diametro)
        self.patate = patate

    def __str__(self):
        return (super().__str__ + f", patate ")

    

class Diavola(Pizza):
    def __init__(self,diametro,salame):
        super().__init__(self, diametro)
        self.salame=salame

    def __str__(self):
        return f"La pizza ha {self.salame} fette di salame con un diametro di {self.diametro}"

if __name__ == "__main__":
    prima = Pizza(4)
    print(prima.area())

    seconda = Patatosa(5, 12)
    print(seconda)