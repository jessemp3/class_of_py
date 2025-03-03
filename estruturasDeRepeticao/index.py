while True:
    numero = int(input('Digite um número: '))

    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

    if input('Deseja continuar? (s/n) ') == 'n':
        break
