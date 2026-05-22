import math

class Pizza:
    def __init__(self, diametro):
        self.diametro = diametro
    
    def area(self):
        return  (self.diametro / 2 ) ** 2 * math.pi

if __name__ == "__main__":
    prima = Pizza(4)
    print(prima.area())