import random
import base_de_paises
def sorteia_pais(dicio_final):
    lista_paises=[]
    for pais in dicio_final:
        lista_paises.append(pais)
    pais=random.choice(lista_paises)
    return pais