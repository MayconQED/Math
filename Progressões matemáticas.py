def PA():
    #Valor de "an" em uma P.A
    a1=int(input('Digite o valor do primeiro termo:'))
    n=int(input('Digite a posição do termo a procura:'))
    r=int(input('Digite a razão da P.A:'))
    an = a1+(n-1)*r
    print('O valor de "An" é igual a:', an)

def PG():
    #Valor de "an" em uma P.G
    a1=int(input('Digite o valor do primeiro termo:'))
    n=int(input('Digite a posição do termo a procura:'))
    q=int(input('Digite a razão da P.G:'))
    an=a1*q**(n-1)
    print('O valor de "An" é igual a:', an)

def SPA():
    #Valor de "Sn" em uma soma de uma P.A
    a1=int(input('Digite o valor do primeiro termo:'))
    an=int(input('Digite o valor de "An" encontrado com auxílio do código acima:'))
    n=int(input('Digite a posição do termo de "An":'))
    Sn=(a1+an)*n/2
    print('O valor da soma dessa P.A é igual a:', Sn)

def SPG():
    #Valor de "Sn" em uma soma de uma P.G
    a1=int(input('Digite o valor do primeiro termo:'))
    an=int(input('Digite o valor de "An" encontrado com auxílio do código acima:'))
    n=int(input('Digite a posição do termo de "An":'))
    q=int(input('Digite a razão dessa P.G:'))
    Sn=a1*((q**n)-1)/(q-1)
    print('O valor da soma dessa P.A é igual a:', Sn)

opcao=1

while opcao:
    print("0. Sair")
    print("1. PA")
    print("2. PG")
    print("3. SPA")
    print("4. SPG")

    opcao = int(input("Opção: "))

    if(opcao==1):
        PA()
    if(opcao==2):
        PG()
    if(opcao==3):
        SPA()
    if(opcao==4):
        SPG()

