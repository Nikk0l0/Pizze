import math

class Pizza:
    def __init__(self, diametro):
        self.diametro = diametro
    
    def area(self):
        return  (r / 2 ) ** 2 * math.pi

prima = Pizza(4)
print(prima)