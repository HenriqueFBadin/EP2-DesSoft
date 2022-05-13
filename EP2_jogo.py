import random
import base_de_dados
import distancia_de_haversine
import lista_ordenada
import sorteia_letra

#Função que cria uma base de dados organizada:
def normaliza(dicio):
    dicio_final = {}
    for continente, conteudo in dicio.items():
      for pais, dados in conteudo.items():
        dicio_final[pais] = dados
        dados['continente'] = continente
    
    return(dicio_final)

base_organizada=(normaliza(base_de_dados.DADOS))

#Função que separa os dados do país escolhido pelo usuário:
def pais_escolhido(palpite, base_organizada):
    escolha=palpite.lower()
    dados_palpite=base_organizada[escolha]
    return dados_palpite

#Funções para o sorteio:
def dados_sorteados(pais_sorteado, base):
    dados_ps = base_organizada[pais_sorteado]
    return dados_ps

def sorteia_pais(dicionario):
    lista_paises=[]
    for pais in dicionario:
        lista_paises.append(pais)
    pais=random.choice(lista_paises)
    return pais

#Prints iniciais do jogo:
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

i = 20 #Tentativas
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
RESET   = '\033[39m'

#Função para a mensagem do inventário
def mensagem_inventario(lista_distancias,dicio_dicas):
    l = 0
    print('Distâncias:')
    for elemento in distancias:
        if elemento[1]>=10000:
            print(RED +'    {0:.3f} km -> {1}'.format(elemento[1], elemento[0]) + RESET + '')
        elif elemento[1]>=5000:
            print(GREEN + '    {0:.3f} km -> {1}'.format(elemento[1], elemento[0]) + RESET + '')
        elif elemento[1]>=1000:
            print(YELLOW + '    {0:.3f} km -> {1}'.format(elemento[1], elemento[0]) + RESET + '')
        elif elemento[1]<1000:
            print(MAGENTA + '    {0:.3f} km -> {1}'.format(elemento[1], elemento[0]) + RESET + '')
        
    print('Dicas:')
    for k, v in dicio_dicas.items():

        if k == '  - Cores da bandeira':
            print('  {}: {}'.format(k, v))
        
        if k == '  - Letras da capital':
            for letra in v:
                if l != 0:
                    value = v + ', ' + letra
                    v = value

                if l == 0:
                    v = letra
                    l+=1

            print('  {}: {}'.format(k, v))
        
        if k == '  - Área' or k == '  - População' or  k == '  - Continente':
            print('  {}: {}'.format(k, v))
        

    return()


while i>0:

    if i==20:
        #País que deve ser descoberto:
        pais_acerto=(sorteia_pais(base_organizada))

        #Dados do país que deve ser descoberto:
        dados_ps = (dados_sorteados(pais_acerto, base_organizada))

        #Criação de uma lista com as cores da bandeira do país alvo. Usado posteriormente para o sorteio:
        lista_cores=[]
        cor_bandeira=(base_organizada[pais_acerto]["bandeira"])
        for cor in cor_bandeira:
            if cor_bandeira[cor]!=0:
                lista_cores.append(cor)
        if "outras" in lista_cores:
            lista_cores.remove("outras")

        tamanho_cores = len(lista_cores) #Utilizado como parametro para as cores esgotadas

        distancias = [] #Lista onde adiciona-se as distâncias
        letras=[] #Lista de letras restritas para o sorteio
        dicas={} #Dicionário onde as keys são as dicas e os valores são as respostas
        colores = '' #Serve para acrescentar as cores pedidas nas dicas no terminal
        mensagem='' #Print das cores da bandeira
        j = 0

    #Palpite do usuário que da início ao jogo:
    print('Você tem' + CYAN + ' {0} '.format(i) + RESET + 'tentativa(s)')
    palpite = input('Qual o seu palpite? ')

    #Inventário:
    if palpite=='inventario' or palpite== 'inventário':
        print('Distâncias:')
        for elemento in distancias:
            if elemento[1]>=10000:
                print(RED +'    {0:.3f} km -> {1}'.format(elemento[1], elemento[0]) + RESET + '')
            elif elemento[1]>=5000:
                print(GREEN + '    {0:.3f} km -> {1}'.format(elemento[1], elemento[0]) + RESET + '')
            elif elemento[1]>=1000:
                print(YELLOW + '    {0:.3f} km -> {1}'.format(elemento[1], elemento[0]) + RESET + '')
            elif elemento[1]<1000:
                print(MAGENTA + '    {0:.3f} km -> {1}'.format(elemento[1], elemento[0]) + RESET + '')

        print('Dicas:')
        for k, v in dicas.items():
            print('  {}: {}'.format(k, v))
    #Desistencia:
    elif palpite == 'desisto':
        if input('Tem certeza que deseja desistir da rodada? [s/n]') == 's':
            print('>>> Que deselegante desistir, o país era: {}'.format(pais_acerto))
            if input("Quer jogar novamente? [s/n] ")=="s":
                i=20
            else:
                break
    
    #Dados país escolhido:
    elif palpite in base_organizada.keys():
        pd_escolhido=(pais_escolhido(palpite, base_organizada))

        #Distância entre os dois países, o escolhido e o sorteado:
        distancia = (distancia_de_haversine.haversine(base_de_dados.EARTH_RADIUS, pd_escolhido['geo']['latitude'], pd_escolhido['geo']['longitude'], dados_ps['geo']['latitude'], dados_ps['geo']['longitude']))

        #Se o País escolhido = País sorteado:
        if dados_ps==pd_escolhido:
            print("Parabéns! Você acertou o país em {} tentativas!".format(20-i))
            i=0
        
        #Caso o país escolhido não seja o mesmo que o sorteado:
        else:
            distancias = lista_ordenada.adiciona_em_ordem(palpite,distancia,distancias)

            mensagem_inventario(distancias,dicas)
            i-=1

    #Sistema de dicas para cor da bandeira funciona apenas para a 1a tentativa(resolver posteriormente):
    elif palpite.lower()=="dica" or palpite.lower()=="dicas":

        print("Mercado de Dicas")
        print("----------------------------------------")
        if i<3:
            print('>>> Infelizmente, acabou seu estoque de dicas! <<<')
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

        opcao = input("\nEscolha sua opção [0|1|2|3|4|5]: ")

        #Sistema dica 1:
        if opcao == "1":

            if lista_cores!=[]:
                cor_escolhida=random.choice(lista_cores)

                lista_cores.remove(cor_escolhida)

                if j == 0:
                    colores += cor_escolhida
                    dicas['  - Cores da bandeira']=colores
                    j += 1

                        
                elif j>0:

                    colores+=', ' + cor_escolhida
                    dicas['  - Cores da bandeira']=colores
                    j += 1
                
            if j>=tamanho_cores:
                print('Cores esgotadas!\n')

            mensagem_inventario(distancias,dicas)
            i-=4

        #Dica 2: sorteio de letra para a escolha dessa opção e adicionamento dessa dica em um dicionário
        if opcao== "2":
            i-=3
            letra_sorteada=sorteia_letra.sorteia_letra(pais_acerto, letras)
            #Falta verificar se todas as letras da capital já entraram na lista de letras restritas
            letras.append(letra_sorteada)
            dicas['  - Letras da capital']=letras
            l = 0

            mensagem_inventario(distancias,dicas)
            l = 0

        #Sistema dica 3:
        if opcao == "3":
            area=(base_organizada[pais_acerto]['area'])
            i -= 6
            dicas['  - Área']=str(area) + ' km2'
            mensagem_inventario(distancias,dicas)

        #Sistema dica 4:
        if opcao == "4":
            população=(base_organizada[pais_acerto]['populacao'])
            i -= 5
            dicas['  - População']=('{} habitantes'.format(população))
            mensagem_inventario(distancias,dicas)

        #Sistema dica 5:
        if opcao == "5":
            continente=(base_organizada[pais_acerto]['continente'])
            i -= 7
            dicas['  - Continente']=continente
            mensagem_inventario(distancias,dicas)
            
        if opcao=='0':
            print('Você saiu do mercado.')


    #Se o input não corresponder a um país ou a uma dica:
    elif palpite not in base_organizada.keys():
        print('Esse país não existe! Tente de novo.')

    #Derrota/Pergunta se quer jogar novamente:
    if i==0:
        print("Você perdeu! Seu país era: {}".format(pais_acerto))
        if input("Quer jogar novamente? [s/n] ")=="s":
            i=20
        else:
            i-=0 