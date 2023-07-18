numero = int(input("Digite um número: "))

antecessor = numero - 1
sucessor = numero + 1


def verificarZero(numero):
    if numero == 0:
        print(f'O antecessor de ZERO será um número negativo {antecessor}')
    else:
        print(f'Antecessor de {numero} = {antecessor}\n'
              f'Sucessor de {numero} = {sucessor}')


verificarZero(numero)
