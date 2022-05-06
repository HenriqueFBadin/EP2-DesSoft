import random
import base_de_paises
def sorteia_pais(dicionario):
    lista_paises=[]
    for pais in dicionario:
        lista_paises.append(pais)
    pais=random.choice(lista_paises)
    return pais

pais_acerto=(sorteia_pais(base_de_paises.base_organizada))

#FIM