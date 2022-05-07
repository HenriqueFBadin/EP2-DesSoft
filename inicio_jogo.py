import random
import base_de_dados
import base_de_paises
import sorteando_paises
import dados_pais_sorteado
import dados_pais_escolhido
import distancia_de_haversine

print(" ============================ ")
print("|"+" "*28+ "|")
print("| Bem-vindo ao Insper Países |")
print("|"+" "*28+ "|")
print(" ==== Design de Software ====\n")
print("Comandos:")
print("     dica       - entra no mercado de dicas")
print("    desisto    - desiste da rodada")
print("    inventario - exibe sua posição")
print("\nUm país foi escolhido, tente adivinhar!")

i = 20
while i>-1:
    print('Você tem {0} tentativa(s)' .format(i))
    palpite = input('Qual o seu palpite? ')

    #País sorteado para o acerto e suas informações:
    pais_acerto=(sorteando_paises.sorteia_pais(base_de_paises.base_organizada))
    dados_ps = (dados_pais_sorteado.dados_sorteados(sorteando_paises.pais_acerto, base_de_paises.base_organizada))
    
    #Sistema de dicas para cor da bandeira funciona apenas para a 1a tentativa(resolver posteriormente):
    if palpite.lower()=="dica" or palpite.lower()=="dicas":
            print("Mercado de Dicas")
            print("----------------------------------------")
            print('1. Cor da bandeira  - custa 4 tentativas')
            print('2. Letra da capital - custa 3 tentativas')
            print('3. Área             - custa 6 tentativas')
            print('4. População        - custa 5 tentativas')
            print('5. Continente       - custa 7 tentativas')
            print('0. Sem dica')
            print("----------------------------------------")
            
            if input("\nEscolha sua opção [0|1|2|3|4|5]: ")=="1":
                lista_cores=[]
                cor_bandeira=(base_de_paises.base_organizada[pais_acerto]["bandeira"])
                for cor in cor_bandeira:
                    if cor_bandeira[cor]!=0:
                        lista_cores.append(cor)
                cor_bandeira=random.choice(lista_cores)
                while cor_bandeira=="outras":
                    cor_bandeira=random.choice(lista_cores)
                i-=4
            elif input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="0" or input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="1"or input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="2"or input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="3"or input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="4"or input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="5":
                print("Opção inválida, tente novamente!")
    palpite = input('Qual o seu palpite? ')

    #Dados do país escolhido pelo usuário:
    while (palpite.lower() not in base_de_paises.base_organizada):
        #if palpite.lower() == "dicas" or palpite.lower() == "dica" or palpite.lower() == "desisto" or palpite.lower() == "inventário" or palpite.lower() == "inventario":
            #Adicionar o sistema de dicas/inventário/desistência:
        
        #else:
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
        print("\nSeu país está a {0:.2f} km de distância".format(distancia))
        i-=1
    
    if i==0:
        print("Você perdeu! Seu país era: {}".format(pais_acerto))
        if input("Quer jogar novamente? [s/n] ")=="s":
            i=20
        else:
            i-=1