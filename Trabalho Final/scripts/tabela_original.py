# Importar os pacotes
import pandas as pd
import numpy as np

# Definindo as colunas
def gerador_col():

    # Primeiramente: Definir a quantidade de zeros por coluna
    # nz é a quantidade de zeros por coluna
    nz = np.random.randint(low= 40, high=75, size=1)
    
    # Criando uma coluna com as especificações pedidas
    col = np.zeros(100)
    
    # Indicar as posições da coluna que não serão zeros
    indice = np.random.choice(range(100), 100-nz, replace = False)

    #
    sorteados = np.random.randint(1, 100, 100-nz)
    
    # Pra definir a quantidade de reads
    # Defini 50000 como o mínimo de reads que uma amostra vai ter
    reads = np.random.randint(low= 50000, high= 100000, size=1)
   
    # Somando pra conferir se a soma das células não vai ultrapassar a quantidade de reads
    num = (sorteados / sum(sorteados)) * reads
    num = num.astype(int)

    dic = {}
    for i in 'abcdefghijklmnopqrstuvwxyz':
        dic['amostra_'+ i] = gerador_col()


    tab = pd.DataFrame(dic)
    tab

# Gerando a lista de novos índices para nomear as linhas
    novo_indice = [f'OTU_{i}' for i in range(1, 101)]

# Colocando o novo_indice para nomear as linhas da tabela
    tab.index = novo_indice

    
    
    # Definindo a coluna e chamando-a
    col[indice] =  num
    return col

# Para chamar a tabela
tab
