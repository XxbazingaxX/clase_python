import random

def aleatorio():
    valor = random.randint(1, 100)
    return (valor)
def correcto(num_oculto,num_import):
    if (num_oculto==num_import):
        print ("Correcto, has Ganado!!")
        return (0)
    else:
        return(1)
def cercano(num_oculto,num_import):
    if (num_oculto<num_import):
        print("El numero correcto es menor")
    else:
        print("El numero correcto es mayor")