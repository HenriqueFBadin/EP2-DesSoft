import sorteando_paises
import base_de_paises

def dados_sorteados(pais_sorteado, base_organizada):
    dados_ps = base_organizada[pais_sorteado]
    return dados_ps

dados_ps = (dados_sorteados(sorteando_paises.pais_acerto, base_de_paises.base_organizada))

#FIM