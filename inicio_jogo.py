import random
import base_de_dados

import distancia_de_haversine

def normaliza(dicio):
    dicio_final = {}
    for continente, conteudo in dicio.items():
      for pais, dados in conteudo.items():
        dicio_final[pais] = dados
        dados['continente'] = continente
    
    return(dicio_final)

base_organizada=(normaliza(base_de_dados.DADOS))

#País escolhido
def pais_escolhido(palpite, base_organizada):
    escolha=palpite.lower()
    dados_palpite=base_organizada[escolha]
    return dados_palpite

#Funções para o sorteio
def dados_sorteados(pais_sorteado, base):
    dados_ps = base_organizada[pais_sorteado]
    return dados_ps

def sorteia_pais(dicionario):
    lista_paises=[]
    for pais in dicionario:
        lista_paises.append(pais)
    pais=random.choice(lista_paises)
    return pais

#País sorteado para o acerto e suas informações:
pais_acerto=(sorteia_pais(base_organizada))
dados_ps = (dados_sorteados(pais_acerto, base_organizada))

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

distancias = {}
i = 20
while i>-1:
    print('Você tem {0} tentativa(s)' .format(i))
    palpite = input('Qual o seu palpite? ')
    
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
                cor_bandeira=(base_organizada[pais_acerto]["bandeira"])
                for cor in cor_bandeira:
                    if cor_bandeira[cor]!=0:
                        lista_cores.append(cor)
                cor_bandeira=random.choice(lista_cores)
                while cor_bandeira=="outras":
                    cor_bandeira=random.choice(lista_cores)
                i-=4
            elif input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="0" or input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="1"or input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="2"or input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="3"or input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="4"or input("\nEscolha sua opção [0|1|2|3|4|5]: ")!="5":
                print("Opção inválida, tente novamente!")

    if palpite not in base_organizada.keys():
        palpite = input('Esse país não existe! Tente de novo.\n Qual o seu palpite? ')

    #Inventario e desistencia:
        #palpite.lower() == "desisto" or palpite.lower() == "inventário":
      
    pd_escolhido=(pais_escolhido(palpite, base_organizada))

    #Distância entre os dois países, o escolhido e o sorteado:
    distancia = (distancia_de_haversine.haversine(base_de_dados.EARTH_RADIUS, pd_escolhido['geo']['latitude'], pd_escolhido['geo']['longitude'], dados_ps['geo']['latitude'], dados_ps['geo']['longitude']))

    #Início do sistema do jogo. Com esse código podemos jogar o jogo normalmente, porém, ainda não possui dicas:
    if dados_ps==pd_escolhido:
        print("Parabéns! Você acertou o país em {} tentativas!".format((i)))
        if input("Quer jogar novamente? [s/n]") =="s":
            i=20
        else:
            i=0

    if i==0:
        print("Você perdeu! Seu país era: {}".format(pais_acerto))
        if input("Quer jogar novamente? [s/n] ")=="s":
            i=20
        else:
            i=-1
    
    else:
        distancias[palpite] = distancia
        print('Distâncias: ')
        for elemento in distancias.items():
            print('    {0:.3f} km -> {1}' .format(elemento[1],elemento[0]))
        
        i-=1


    