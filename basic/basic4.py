notas = []

contador = 0

while contador < 4:
    nota = int(input('Digite a nota: '))
    notas.append(nota)
    contador += 1

menorNota = min(notas)
maiorNota = max(notas)

media = sum(notas) / 4


def statusAluno(media):
    if media >= 7:
        print('Aluno(a) aprovado(a)')
    else:
        print('Aluno(a) reprovado(a)')


print(f'A média final do aluno {media}\n'
      f'A menor nota foi: {menorNota}\n'
      f'A maior nota foi: {maiorNota}\n')

statusAluno(media)
