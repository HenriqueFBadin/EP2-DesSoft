from email import message
import random
import base_de_dados
import distancia_de_haversine
import lista_ordenada

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

#Nova funcao para a mensagem do inventário
def mensagem_inventario(lista_de_distancias, n_pedidos_cores, mensagem_das_cores, dicionario_de_dicas): #n_pedido_cores é o pedido_cores
    message = ''
    print('Distâncias:')
    for elemento in lista_de_distancias:
        print('    {0:.3f} km -> {1}' .format(elemento[1], elemento[0]))

    print('\nDicas: ')

    for dica in dicionario_de_dicas.values():
        if n_pedidos_cores != 0: #criterio caso não tenha sido pedido dica
            if dica[0] == mensagem: 
                print('  - Cores da bandeira: {0}' .format(mensagem_das_cores))

    return ''

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


distancias = []
colores = []
opcoes =  ['0', '1', '2', '3', '4', '5']
mensagem = '' #Referente as cores da bandeira
pedidos_cores = 0 #Contador das vezes que as cores são pedidas, utilizado na função do inventario
mensagem_opcao = ''
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
    
    if palpite.lower() == 'inventario': #Chamar função / 
        print(mensagem_inventario(distancias,pedidos_cores, mensagem,inventario))


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
            print('Distâncias: ')
            distancias = lista_ordenada.adiciona_em_ordem(palpite,distancia,distancias)
        
            for elemento in distancias:
                print('    {0:.3f} km -> {1}' .format(elemento[1], elemento[0]))
                
            print('Dicas: {}'.format(mensagem))
            i-=1

    if palpite.lower()=="dica" or palpite.lower()=="dicas":

        print("Mercado de Dicas")
        print("----------------------------------------")
        if i>= 4:
            print('1. Cor da bandeira  - custa 4 tentativas')
        elif i<4:
            del opcoes[1]

        if i>=3:
            print('2. Letra da capital - custa 3 tentativas')
        elif i<3:
            del opcoes[2]

        if i>=6:
            print('3. Área             - custa 6 tentativas')
        elif i<6:
            del opcoes[3]

        if i>=5:
            print('4. População        - custa 5 tentativas')
        elif i<5:
            del opcoes[4]

        if i>=7:
            print('5. Continente       - custa 7 tentativas')
        elif i<7:
            print(opcoes)
            del opcoes[5]
            print(opcoes)

        print('0. Sem dica')
        print("----------------------------------------")

        for opcao_disponivel in opcoes:
            mensagem_opcao = mensagem_opcao + opcao_disponivel

        contador = 0
        mensagem_opcoes = ''
        for numero in opcoes:
            if contador == 5:
                mensagem_opcoes = mensagem_opcoes + numero
            
            else:
                mensagem_opcoes = mensagem_opcoes + numero + '|' #Estou aqui
            contador += 1

        opcao = input("\nEscolha sua opção [{}]: ".format(mensagem_opcoes)) #As opções somem com o tempo 
        opcoes = [] #Zerar opções para que elas não acumulem

        if opcao == "1":
            pedidos_cores += 1
            
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
                print(mensagem_inventario(distancias,pedidos_cores, mensagem,inventario))

                i-=4
            
            else:
                for elemento in distancias:
                    print('    {0:.3f} km -> {1}' .format(elemento[1], elemento[0]))
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