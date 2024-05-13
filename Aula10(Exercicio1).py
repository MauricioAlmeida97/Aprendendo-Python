"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

""" numero = input('Digite um número: ')

if numero.isdigit:
    numero_int = int(numero) 
    par_impar = numero_int % 2 == 0
    par_impar_texto = "ímpar"

    if par_impar:
        par_impar_texto = "par"

    print(f"O número {numero} é {par_impar_texto} ")        
else:
    print("Escreva um número inteiro!") """

#  Da pra colocar try e except, usando try sem o "numero.isdigit" e fechando dois pontos ":"
#  Fica o código mais limpinho.

numero = input('Digite um número: ')

try:
    numero_int = int(numero) 
    par_impar = numero_int % 2 == 0
    par_impar_texto = "ímpar"

    if par_impar:
        par_impar_texto = "par"

    print(f"O número {numero_int} é {par_impar_texto} ")        
except:
    print("Escreva um número inteiro!")