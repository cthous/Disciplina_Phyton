# Normaliza cada coluna da tabela
tab_normalizada = (tab - tab.min()) / (tab.max() - tab.min())

# Exibe a tabela normalizada
print(tab_norm)
