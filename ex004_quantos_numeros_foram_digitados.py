cont = 0
for e in range(10):
    num = int(input('Digite o {}º número: '.format(e)))
    if 1 < num < 1000:
        cont += 1
print('Foram informados {} valores entre 1 e 1000'.format(cont))
