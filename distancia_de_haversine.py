import math
import base_de_dados
import sorteando_paises
import inicio_jogo
import dados_pais_escolhido
import dados_pais_sorteado

def haversine(r, fi1, lamb1, fi2, lamb2):
    f1=math.radians(fi1)
    f2=math.radians(fi2)
    l1=math.radians(lamb1)
    l2=math.radians(lamb2)
    a1=((f2-f1)/2)
    a2=(math.sin(a1))**2
    a3=((l2-l1)/2)
    a4=(math.sin(a3))**2
    a5=math.cos(f1)*math.cos(f2)*a4
    a6=math.sqrt(a2+a5)
    d=2*r*math.asin(a6)
    return d

distancia = (haversine(base_de_dados.EARTH_RADIUS, dados_pais_escolhido.pd_escolhido['geo']['latitude'], dados_pais_escolhido.pd_escolhido['geo']['longitude'], dados_pais_sorteado.dados_ps['geo']['latitude'], dados_pais_sorteado.dados_ps['geo']['longitude']))