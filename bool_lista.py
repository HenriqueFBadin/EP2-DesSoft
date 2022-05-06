def esta_na_lista(nome,lista):
    for dados in lista:
        if nome == dados[0]:
            return True
    
    return False