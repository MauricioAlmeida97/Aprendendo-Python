"""
Exercio de IMC
"""
nome = "José Mauricio"
altura = 1.74
peso = 115
imc = peso / (altura ** 2)
print(nome, 'tem', altura, 'de altura, e pesa', peso,'kg', 'e tem', imc,'de IMC')
print (f'{nome} tem {altura:.2f}m de altura,')  # isso também pode ser uma variável descrita


a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)
#  "nome1=a" - parâmetro nomeado, que nao permite que vc execute um codigo se nao nomear 
#  todos os argumentos
print(formato)


###########################################################
""" TESTE DE ESTRUTURA CONDICIONAL """
"""
Comparativo de dois valores,procedural, if/elif/else
"""
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}.')

elif segundo_valor > primeiro_valor:
    print (f'{segundo_valor} é maior que {primeiro_valor}.')

else:
    print(f'{primeiro_valor} e {segundo_valor} são iguais.')
######################################################################



"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])
###########################################################

""" TESTE DE PRINT"""
"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

if nome and idade:
    print (f'Seu nome é {nome}')
    print (f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome tem espaços vazios')
    else:
        print(f'Seu nome NÃO tem espaços vazios')
    
    print (f'Seu nome tem {len(nome)} letras.')
    print (f'A primeira letra do seu nome é {nome[0]}')
    print (f'A última letra do seu nome é {nome[-1]}')


else:
    print("Desculpe, você deixou campos vazios.")
################################################################
"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

