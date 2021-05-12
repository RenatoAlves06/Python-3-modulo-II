nome = str(input("Qual seu nome ? "))
if nome == 'Renato':
    print('Belo nome você tem !!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia jessica Juliana':
    print('Seu nome é bem normal.')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia,{}!'.format(nome))
