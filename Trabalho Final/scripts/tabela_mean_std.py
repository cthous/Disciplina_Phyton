import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fazer as médias e desvios primeiro
# Original
media_original = int(tab.sum().mean())
desvio_original = int(tab.sum().std())

# Rarefada
media_rarefada = int(tab.2().mean())
'desvio_rarefado'

# Normalizada
media_normalizada = int(tab_norm.sum().mean())
desvio_normalizado = int(tab_norm.sum().std())


# Tabela das médias
dados = [[media_original, desvio_original], [0, 0], [media_normalizada, desvio_normalizado]]
linhas = ['Original', 'Rarefada', 'Normalizada']
colunas = ['Média', 'Desvio Padrão']

tab_6 = pd.DataFrame(dados, index = linhas, columns = colunas)
tab_6
