# Criando os conjuntos
a1 = {2,3,4,5,6}
a2 = {1,2,4,5}
a3 = {0,1,2,4,5,7}

# Nomeando as regiões e seu conteúdo
regiao1 = a1 - (a2|a3)    #para saber a1
regiao3 = a2 - (a1|a3)    #para saber a2
regiao4 = a3 - (a1|a2)    #para saber a3
regiao2 = a1.intersection(a2) - a3    #comum a a1 e a2
regiao5 = a2.intersection(a3) - a1    #comum a a2 e a3
regiao6 = a3.intersection(a1) - a2    #comum a a1 e a3
regiao7 = a1.intersection(a2,a3)    #comum a todos

#Separando os conteúdos de cada um dos 3 conjuntos (a1;a2;a3)
conj_a1 = a1 - regiao2 - regiao6 - regiao7
conj_a2 = a2 - regiao2 - regiao5 - regiao7
conj_a3 = a3 - regiao5 - regiao6 - regiao7

#Por fim as frases com os resultados
print('Oi, temos os seguintes resultados: ')
print('Região 1 =', regiao1, '\nRegião 2 =', regiao2, '\nRegião 3 =',
       regiao3, '\nRegião 4 =', regiao4, '\nRegião 5 =', regiao5, 
       '\nRegião 6 =', regiao6, '\nRegião 7 =', regiao7)
