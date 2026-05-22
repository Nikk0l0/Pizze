import math

class Pizza:
    def __init__(self, diametro):
        self.diametro = diametro
    
    def area(self):
        return  (self.diametro / 2 ) ** 2 * math.pi


class Diavola(Pizza):
    def __init__(self,diametro,salame):
        super().__init__(self, diametro)
        self.salame=salame

    def __str__(self):
        return f"La pizza ha {self.salame} fette di salame con un diametro di {self.diametro}"

if __name__ == "__main__":
    prima = Pizza(4)
    print(prima.area())