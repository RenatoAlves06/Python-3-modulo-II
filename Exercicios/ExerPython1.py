print('Bem vindo ao sistema de financiamento')

VCasa = float(input('Digite o valor da do imovel: '))
Tfinan = int(input('Digite o tempo em que vai pagar: '))
Sal = float(input('Digite sua renda: '))

prest = (VCasa/Tfinan)
vmaximo = Sal * 0.30

if prest > vmaximo:
    print('Renda Imcompativel valor da prestação é :{}'.format(prest))
    print('Valor maximo da prestacão será de: {}'.format(vmaximo))
else:
    print('Financiamento aprovado o valor de sua prestação será de : {}'.format(prest))
print('Obrigado...')
