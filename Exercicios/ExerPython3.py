from datetime import date, datetime
print('<<< Bem vindo ao sistema de alistamento >>>')
nasc = int(input('Digite o ano do seu nascimento: '))
atual = date.today()
anoAtual = atual.year
idade = anoAtual - nasc
if idade == 17:
    print('Você precisa se alistar este ano {}'.format(anoAtual))
elif idade > 18:
    print('Você se alistou em >> {}'.format(nasc+17))
else:
    print('Voce ainda não esta na idade para se alistar somente em >> {}'.format(nasc+17))
