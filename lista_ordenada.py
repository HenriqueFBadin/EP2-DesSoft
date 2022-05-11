def adiciona_em_ordem(nome,dist,lista):
    i = 0
    for dados in lista:
        if nome in dados:
            return lista
        
        dlista = dados[1]
        if dist>dlista:
            i+=1
        
    lista.insert(i,[nome,dist])

    return lista