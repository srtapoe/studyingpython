numero = int(input("Digite o número: "))


def verificarNumeroPar(numero):
    if numero % 2 == 0:
        print(f'{numero} eh par')
    else:
        print(f'{numero} eh impar')


verificarNumeroPar(numero)
