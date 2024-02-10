#Define una clase llamada `Rectangulo` que tenga dos atributos: `base` y `altura`.
#La clase debe tener un método para calcular el área del rectángulo.
class rectangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def calculo(self):
        area=self.base*self.altura
        print(f"El rectangulo mide {self.base}cm de base y {self.altura}cm de altura y el area de este es de", area,"cm2")



#creando objeto rectangulo
rectangulo1= rectangulo(6, 4)
rectangulo1.calculo()