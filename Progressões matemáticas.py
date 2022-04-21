from time import sleep

def PA():
    #Valor de "an" em uma P.A
    k = int(input('Digite a posição do termo conhecido: '))
    ak = int(input('Digite o valor do termo conhecido: '))
    n = int(input('Digite a posição do termo a procura: '))
    r = int(input('Digite a razão da P.A: '))
    an = ak+(n-k)*r
    print('O valor de "An" é igual a: {}'.format(an))
    print('==='*20)
    sleep(1)

def PG():
    #Valor de "an" em uma P.G
    k = int(input('Digite a posição do termo conhecido: '))
    ak = int(input('Digite o valor do termo conhecido: '))
    n = int(input('Digite a posição do termo a procura: '))
    q = int(input('Digite a razão da P.G: '))
    an = ak*q**(n-k)
    print('O valor de "an" é igual a: {}'.format(an))
    print('==='*20)
    sleep(1)
    
def SPA():
    #Valor de "Sn" em uma soma de uma P.A
    a1 = int(input('Digite o valor do primeiro termo: '))
    an = int(input('Digite o valor de "an": '))
    n = int(input('Digite a posição do termo de "an": '))
    Sn = (a1+an)*n/2
    print('O valor da soma dessa P.A é igual a: {}'.format(Sn))
    print('==='*20)
    sleep(1)

def SPG():
    #Valor de "Sn" em uma soma de uma P.G
    a1 = int(input('Digite o valor do primeiro termo: '))
    n = int(input('Digite a posição do termo de "an": '))
    q = int(input('Digite a razão dessa P.G: '))
    Sn = a1*((q**n)-1)/(q-1)
    print('O valor da soma dessa P.G é igual a: {}'.format(Sn))
    print('==='*20)
    sleep(1)

op=1
print('==='*20)
print('Escolha uma das opções para calcular:')
print('==='*20)

while op:
    print("0. Sair")
    print("1. P. Aritmética")
    print("2. P. Geométrica")
    print("3. Soma de uma   P. Aritmética")
    print("4. Soma de uma P. Geométrica")
 
    op = int(input("Opção: "))
    print('==='*20)
    if (op==1):
        PA()
    elif (op==2):
        PG()
    elif op==3:
        SPA()
    elif (op==4):
        SPG()   
    elif (op==0):
        print('Saindo...')
        sleep(3)
        print('Programa fechou!')
        print('==='*20)
    else:
        print('Opção invalida, tente novamente.')
        print('==='*20)
        sleep(2)
