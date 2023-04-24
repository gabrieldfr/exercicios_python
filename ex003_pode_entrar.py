cont = 0
for e in range(1, 21):
    idade = int(input('Digite a idade da {}ª pessoa: '.format(e)))
    if idade < 18:
        cont += 1
print('{} pessoas não podem entrar no pub'.format(cont))
