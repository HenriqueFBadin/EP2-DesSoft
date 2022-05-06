def normaliza(dicio):
    dicio_final = {}
    for continente, conteudo in dicio.items():
      for pais, dados in conteudo.items():
        dicio_final[pais] = dados
        dados['continente'] = continente
    
    return(dicio_final)