cont = []
soma = 0
for e in range(10):
    num = int(input('Digite o {}º número: '.format(e)))
    if num % 2 == 0:
        soma += num
print('A soma de todos os números pares digitados é igual a {}'.format(soma))
