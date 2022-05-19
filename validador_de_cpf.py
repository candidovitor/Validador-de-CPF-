cpf = list()
atual = list()

for cont in range (0, 11):
    cpf.append(int(input(f'Digite o numero da {cont + 1} posição do seu cpf: ')))

atual.append(cpf[:]) 

n0 = cpf[0] * 10
n1 = cpf[1] * 9
n2 = cpf[2] * 8
n3 = cpf[3] * 7
n4 = cpf[4] * 6
n5 = cpf[5] * 5
n6 = cpf[6] * 4
n7 = cpf[7] * 3
n8 = cpf[8] * 2
n9 = cpf[9]
n10 = cpf[10] 

print('-=' * 40)

primeiro_numero = 11 - ((n0  + n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8) % 11)

print(f'Seu CPF é: {atual}')

print('-=' * 40)

if primeiro_numero >= 10:
    primeiro_numero = 0

if primeiro_numero == n9:
    print(F'PRIMERIO NÚMERO DE CPF VALIDADO: {primeiro_numero}')
else:
    print('PRIMERIO NÚMERO DE CPF INVÁLIDO')


x0 = cpf[0] * 11
x1 = cpf[1] * 10
x2 = cpf[2] * 9
x3 = cpf[3] * 8
x4 = cpf[4] * 7
x5 = cpf[5] * 6
x6 = cpf[6] * 5
x7 = cpf[7] * 4
x8 = cpf[8] * 3
x9 = primeiro_numero * 2

segundo_numero = 11 - ((x0  + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9) % 11)

print('-=' * 40)

if segundo_numero >= 10:
    segundo_numero = 0

if segundo_numero == n10:
    print(f'SEGUNDO NÚMERO DE CPF VALIDADO: {segundo_numero}')
else:
    print('SEGUNDO NÚMERO DE CPF INVÁLIDO')

print('-=' * 40)

if primeiro_numero == n9 and segundo_numero == n10:
    print('CPF VALIDADO')
else:
    print('CPF INVÁLIDO')



 