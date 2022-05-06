import inicio_jogo
import base_de_paises
def pais_escolhido(palpite, base_organizada):
    escolha=palpite.lower()
    dados_palpite=base_organizada[escolha]
    return dados_palpite

pd_escolhido=(pais_escolhido(inicio_jogo.palpite, base_de_paises.base_organizada))