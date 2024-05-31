somas = tab.sum(axis=0)
total_menor = somas.min()

def rarefar_amostra(amostra_original, total_menor):
    somas = tab.sum(axis=0)
    total_menor = somas.min()
    amostra = amostra_original.copy()
    while total_menor < sum(amostra):
        
        otus_relevantes = amostra[amostra > 0]
        
        proporcao = (max(amostra) - amostra) + 1
        proporcao[proporcao == (max(amostra)+1)] = 0
        proporcao = proporcao / sum(proporcao)
        
        sorteado = np.random.choice(otus_relevantes.index, p = proporcao[otus_relevantes.index])
        amostra[sorteado] -= 1

        tab_rarefada = tab.copy()
        tab_rarefada.loc[:,:] = 0 
        
        tab_rarefada
        for coluna in tab.columns:
            print(coluna)
            novos_valores = rarefar_amostra(tab[coluna], total_menor)
            tab_rarefada[coluna] = novos_valores
    return amostra

tab_rarefada = tab.copy()
tab_rarefada.loc[:,:] = 0 
tab_rarefada

for coluna in tab.columns:
    print(coluna)
    novos_valores = rarefar_amostra(tab[coluna], total_menor)
    tab_rarefada[coluna] = novos_valores
