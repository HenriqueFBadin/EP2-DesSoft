import random
def sorteia_letra(palavra, letras_r):
    lista_palavra=[]
    especiais=['.', ',', '-', ';', ' ']
    verifica=0
    i=0
    for letra in palavra:
        lista_palavra.append(letra)
    if palavra == '':
        return ''
    while i<(len(lista_palavra)):
        if lista_palavra[i].lower() in letras_r or lista_palavra[i].lower() in especiais:
            verifica+=1
        i+=1
    if verifica==len(lista_palavra):
        return ''
    r_palavra=random.choice(lista_palavra)
    while (r_palavra.lower() in letras_r) or (r_palavra.lower() in especiais):
        r_palavra=random.choice(lista_palavra)
    return r_palavra.lower()