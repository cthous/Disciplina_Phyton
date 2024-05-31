import numpy as np

def indice_shannon(values):
    # Calcula a soma total das leituras
    total = np.sum(values)
    
    # Calcula as proporções de cada espécie
    proportions = values / total
    
    # Calcula o índice de Shannon
    shannon = -np.sum(proportions * np.log(proportions))
    
    return shannon
