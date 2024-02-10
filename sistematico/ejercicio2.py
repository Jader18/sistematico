#Crea una clase base llamada `FiguraGeometrica` que tenga un método `calcular_area`. 
#Luego, crea subclases para representar diferentes figuras geométricas como `Triangulo`, `Cuadrado`, etc. 
#Cada subclase debe implementar el método `calcular_area` según la fórmula correspondiente.


class FiguraGeometrica: 
    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        print("Calcular el area")



class Triangulo(FiguraGeometrica): 
    def __init__(self, base, altura): 
        super().__init__(base, altura)


    def areaTriangulo(self): 
        print("La base del triangulo es: ", ((self.base * self.altura)/2))


class Cuadrado(FiguraGeometrica): 
    def __init__(self, base, altura): 
        super().__init__(base, altura)


    def areaCuadrado(self): 
        print("La base del cuadrado es: ", (self.base * self.altura))

figura1 = FiguraGeometrica(1, 2)


Triangulo = Triangulo(2, 4)

Cuadrado = Cuadrado(5, 5)

Triangulo.areaTriangulo()
Cuadrado.areaCuadrado()
