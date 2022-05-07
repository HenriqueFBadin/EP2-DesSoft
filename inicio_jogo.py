import base_de_dados
import base_de_paises
import sorteando_paises
import dados_pais_sorteado
import dados_pais_escolhido
import distancia_de_haversine

i = 20
while i>-1:
    print('Você tem {0} tentativa(s)' .format(i))
    palpite = input('Qual o seu palpite? ')

    #País sorteado para o acerto e suas informações:
    pais_acerto=(sorteando_paises.sorteia_pais(base_de_paises.base_organizada))
    dados_ps = (dados_pais_sorteado.dados_sorteados(sorteando_paises.pais_acerto, base_de_paises.base_organizada))

    #Dados do país escolhido pelo usuário:
    while palpite.lower() not in base_de_paises.base_organizada:
      palpite = input('Esse país não existe! Tente de novo.\n Qual o seu palpite? ')
      
    pd_escolhido=(dados_pais_escolhido.pais_escolhido(palpite, base_de_paises.base_organizada))

    #Distância entre os dois países, o escolhido e o sorteado:
    distancia = (distancia_de_haversine.haversine(base_de_dados.EARTH_RADIUS, pd_escolhido['geo']['latitude'], pd_escolhido['geo']['longitude'], dados_ps['geo']['latitude'], dados_ps['geo']['longitude']))

    #Início do sistema do jogo. Com esse código podemos jogar o jogo normalmente, porém, ainda não possui dicas:
    if dados_ps==pd_escolhido:
        print("Parabéns! Você acertou o país em {} tentativas!".format((21-i)))
        if input("Quer jogar novamente? [s/n]")=="s":
            i=20
        else:
            i=0
    else:
        print("Seu país está a {0:.2f} km de distância".format(distancia))
        i-=1
    
    if i==0:
        print("Você perdeu! Seu país era: {}".format(pais_acerto))
        if input("Quer jogar novamente? [s/n] ")=="s":
            i=20
        else:
            i-=1