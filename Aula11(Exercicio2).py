"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input("Digite uma hora em numeros inteiro: ")

try:
    hora = int(entrada)
    if hora >=0 and hora <= 11:
        print("Bom dia!")
    elif hora <= 17 and entrada >= 12:
        print("Boa tarde!")
    elif hora <= 18 and entrada >= 23:
        print("Boa noite!")
    else:
        print("Não conheço essa hora!")
except:
    print("Favor escrever número inteiro (1,2,3,4...)")

# essa foi a solução do professor, mas como eu queria brincar e aprender, fiz isso:

entrada = input("Digite uma hora em numeros inteiro: ")

try:
    hora = int(entrada)
    if hora >=0 and hora <= 4:
        print("Boa madrugada!")
    elif hora >= 5 and hora <= 11:
        print("Boa dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite!")
    else:
        print("Não conheço essa hora!")
except:
    print("Favor escrever número inteiro: 1,2,3,4...")

# ficou mais "sujo", o meu código??... Sim. Mas eu só queria brincar e entender mais sobre a estrutura. Valeu a pena
#  XD :)