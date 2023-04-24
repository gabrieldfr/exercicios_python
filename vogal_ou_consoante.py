letra = str(input('Digite uma letra: ')).strip() .upper()
match letra:
    case 'A' | 'E' | 'I' | 'O' | 'U':
        print('É vogal')
    case _:
        print('É consoante')
