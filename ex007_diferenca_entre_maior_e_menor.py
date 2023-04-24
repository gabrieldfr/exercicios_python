print('Digite dois números diferentes e maiores que 0')
num1 = 0
num2 = 0
maior = 0
menor = 0
while num1 <= 1 or num2 <= 0 or num1 == num2:
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))

    if num1 <= 0 or num2 <= 0:
        print('Os números devem ser diferentes de 0')
    elif num1 == num2:
        print('Os números precisam ser diferentes')
    elif num1 > num2:
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1

print('A diferença entre {} e {} é igual a {}'.format(maior, menor, maior - menor))

