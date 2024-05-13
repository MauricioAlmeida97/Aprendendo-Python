"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input("Escreva o seu primeiro nome: ")
nome = len(entrada)

if nome <=4:
    print("Seu nome é curto")
elif nome >= 5 and nome <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")

#  Essa foi a minha solução ,tem a falha de que um usuário obterá uma resposta para qualquer tamanha de str no input
#  acredito que o professor demonstrou uma solução otimizada para a questão. Segue abaixo a solução do professor:

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
