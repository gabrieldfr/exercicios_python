print('Digite números. Quando quiser parar digite "0"')
num = int(input('Digite um número: '))
lista = []
soma = 0
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0:
        lista.append(num)
        soma += num
print('A média de todos os números digitados é igual a {}'.format(soma / len(lista)))
