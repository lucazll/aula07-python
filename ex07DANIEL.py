contador = 0 
soma = 0 

for i in range(0, 100):
    if i % 2 != 0:
        print(i)
        contador = contador + 1
        soma = soma + i

print(f'Foram exibidos {contador} números ímpares nesse intervalo')
print(f'A soma dos números ímpares é {soma}')