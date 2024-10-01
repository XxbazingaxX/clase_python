import Numerito_funcion

b= Numerito_funcion.aleatorio()
a= int(input("Introduce el numero entre 1 y 100: "))

while (Numerito_funcion.correcto(b,a)!=0):
    Numerito_funcion.cercano(b,a)
    a=int(input("Introduce el numero entre 1 y 100: "))