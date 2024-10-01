import math

# metodo comprobar primero si es un punto para no introducir un caracter incorrecto y que falle la aplicación
def es_numero(numero):
    """ Indica si un valor es numérico o no. """
    return isinstance(numero, (int, float, complex))

# Clase punto
class Punto(object):
    def __init__(self, x=0, y=0):
        if es_numero(x) and es_numero(y):
            self.x = x
            self.y = y
        else:
            print("#### Error ####")
            raise TypeError("x e y deben ser valores numéricos")

    # Metodo str Para mostrar informacion del objeto
    def __str__(self):

        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # Metodo distancia
    def distancia(self, current):
        """ Devuelve la distancia entre ambos puntos. """
        # primero obtenemos la diferencia de x y luego en el return lo elevamos al cuadrado lo mismo con y
        dx = self.x - current.x
        dy = self.y - current.y
        return round(((dx ** 2 + dy ** 2) ** 0.5), 2)

    """
	Metodo suma 
	El método __add__ es el que se utiliza para el operador +

	"""

    def __add__(self, other):

        return Punto(self.x + other.x, self.y + other.y)

    # Metodo resta
    def __sub__(self, other):

        return Punto(self.x - other.x, self.y - other.y)


p = Punto(1, 3)
r = Punto(2, 5)

print(r - p)
print(p)
