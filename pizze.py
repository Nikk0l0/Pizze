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

    

if __name__ == "__main__":
    prima = Pizza(4)
    print(prima.area())

    seconda = Patatosa(5, 12)
    print(seconda)