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
print("    dica       - entra no mercado de dicas")
print("    desisto    - desiste da rodada")
print("    inventario - exibe sua posição")
print("\nUm país foi escolhido, tente adivinhar!")

#Definindo a lista de cores da bandeira
lista_cores=[]
cor_bandeira=(base_organizada[pais_acerto]["bandeira"])
for cor in cor_bandeira:
    if cor_bandeira[cor]!=0:
        lista_cores.append(cor)
if "outras" in lista_cores:
    lista_cores.remove("outras")


distancias = {}
colores = []
mensagem = ''
i = 20
j = 0

#Dicionário para colocar todas as dicas
inventario = {'1':mensagem} #'2':letra_capital, '3': area, '4': populacao, '5':continente}
mensagem=''
while i>0:
    print('Você tem {0} tentativa(s)' .format(i))
    palpite = input('Qual o seu palpite? ')

    if palpite == 'desisto':
        if input('Tem certeza que deseja desistir da rodada? [s/n]') == 's':
            print('>>> Que deselegante desistir, o país era: {}'.format(pais_acerto))
            break
    
    if palpite.lower() == 'inventario':
        print('Distâncias: ') #essas distâncias precisarão se tornar listas para encaixar na função e serem colocadas em ordem
        for elemento in distancias.keys():
            print('    {0:.3f} km -> {1}' .format(distancias[elemento],elemento))
        
        print('Dicas: ' )#.format(inventario))


    if palpite in base_organizada.keys():
        pd_escolhido=(pais_escolhido(palpite, base_organizada))

        #Distância entre os dois países, o escolhido e o sorteado:
        distancia = (distancia_de_haversine.haversine(base_de_dados.EARTH_RADIUS, pd_escolhido['geo']['latitude'], pd_escolhido['geo']['longitude'], dados_ps['geo']['latitude'], dados_ps['geo']['longitude']))
                
        if dados_ps==pd_escolhido:
            print("Parabéns! Você acertou o país em {} tentativas!".format(20-i))
            if input("Quer jogar novamente? [s/n] ")=="s":
                i=20
            else:
                i=-1
        else:
            distancias[palpite] = distancia
            print('Distâncias: ')
            for elemento in distancias.keys():
                print('    {0:.3f} km -> {1}' .format(distancias[elemento],elemento))
                
            print('Dicas: {}'.format(mensagem))
            i-=1

        #Sistema de dicas para cor da bandeira funciona apenas para a 1a tentativa(resolver posteriormente):
    if palpite.lower()=="dica" or palpite.lower()=="dicas":

        print("Mercado de Dicas")
        print("----------------------------------------")
        if i>= 4:
            print('1. Cor da bandeira  - custa 4 tentativas')
        if i>=3:
            print('2. Letra da capital - custa 3 tentativas')
        if i>=6:
            print('3. Área             - custa 6 tentativas')
        if i>=5:
            print('4. População        - custa 5 tentativas')
        if i>=7:
            print('5. Continente       - custa 7 tentativas')
        print('0. Sem dica')
        print("----------------------------------------")
                    
        #opcao = input("\nEscolha sua opção [0|1|2|3|4|5]: ") As opções devem sumir com o tempo 

        if input("\nEscolha sua opção [0|1|2|3|4|5]: ") == "1":
            
            if lista_cores!=[]:
                cor_escolhida=random.choice(lista_cores)
                
                colores.append(cor_escolhida)
                lista_cores.remove(cor_escolhida)

                for tom in colores:
                    if len(colores) == 1:
                        mensagem = tom
                        cor_antiga = mensagem
                    
                    else:
                        mensagem = cor_antiga + ',' + ' ' + tom

                inventario['1']=colores    
                print('  - Cores da bandeira: {0}' .format(mensagem))

                        #for elemento in distancias.keys():
                         #   print('    {0:.3f} km -> {1}' .format(distancias[elemento],elemento))
                    
                #elif j>0:
                    
                   # for elemento in distancias.keys():
                     #   print('    {0:.3f} km -> {1}' .format(distancias[elemento],elemento))
                    #print(mensagem + ',' + ' ' + cor_escolhida)
                    #mensagem = mensagem + ',' + ' ' + cor_escolhida 
                    #print(inventario)   

                i-=4
            
            else:
                for elemento in distancias.keys():
                        print('    {0:.3f} km -> {1}' .format(distancias[elemento],elemento))
                #print(mensagem)
                print('A bandeira não tem mais cores')

   # elif palpite not in base_organizada.keys():
    #    palpite = print('Esse país não existe! Tente de novo.')

  #  if i==0:
   #     print("Você perdeu! Seu país era: {}".format(pais_acerto))
        #if input("Quer jogar novamente? [s/n] ")=="s":
         #   i=20
   # else:
    #    i-=0
print('Até a próxima!')