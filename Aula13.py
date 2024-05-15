"""
Repetições
while (enquanto)
Executa um ação enquanto uma condição for verdadeira
"""
"""EXEMPLO_1"""
condicao = True

while condicao:
    nome = input("Digite seu nome: ")
    print(f"Seu nome é {nome}")

    if nome == 'sair':
              break
    
print('acabou')

""" EXEMPLO 2 """

contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1
    
print("acabou")

 
""" EXEMPLO 3"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print ("Não vou mostrar o 6.")
        continue

    if contador >= 10 and contador <= 27:
        print("Não vou mostrar o", contador)
        continue    # continua o código, depois da condição estabelecida, 
        # neste caso.
    
    print(contador)

    if contador == 40:
        break

print ("Acabou!")
