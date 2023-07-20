frase = "Exercícios de Java"

palavraSubstituta = str(input("Digite a palavra que irá substituir Java na frase acima: "))

frase = frase.replace("Java", palavraSubstituta)

print(f'Frase após o replace: {frase}')
