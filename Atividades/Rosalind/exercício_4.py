#Exercício 4

a = 4692
b = 9593

#Variável que vai ficar somando os ímpares
soma = 0

for i in range(a, b +1):
    if i % 2 == 1:
        soma += i

print(soma)