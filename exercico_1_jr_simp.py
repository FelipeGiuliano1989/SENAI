#1 - Crie um programa capaz de calcular juros simples conforme o escopo do projeto proposto.


# Apresentação

print('\n\t\t\t -- CALCULO DE JUROS SIMPLES --\n')


# Entrada
c = float(input('Informe o CAPITAL: '))
t = float(input('Informe a TAXA: '))
p = float(input('Informe o PRAZO: '))

# Processamento

j = (c * t * p) / 100

m = j + c

# Saída

print(f'\n O valor de juros é R${j}')


print(f'\n O valor do montante é R$ {m}')


