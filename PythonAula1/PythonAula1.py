#encoding: latin-1
from random import randint
from random import sample

cidades="joinville","garuva","itapo�","curitiba","araquari"
cores='vermelho','azul', 'amarelo','rosa','preto'
times='flamengo','corinthias','vasco','palmeiras','fluminense'
paises='brasil','estados unidos', 'fran�a','portugal','it�lia'
animo=['Temos mais uma, n�o desista','Eu sei que consegue','Vamos, temos chance','vamos, n�o desista','De primeira e dif�cil, mais uma']
print("Embaralhando palavras!")
print("Escolha o n�mero correspondente ao tema: cidades(1), cores(2), times(3), pa�ses(4)")
op = input()
if op=="1":
    print("Voc� escolheu o tema cidades!")
    nun=randint(0,4)
    palavra1=cidades[nun]
    palavra = sample(palavra1,len(palavra1))
    count=5
    for x in range(5):
        if count<5:
            print(animo[count])
        print("Voc� tem ",count," chances para adivinhar a palavra:",palavra)
        ent=input()
        count=count-1
        if palavra1==ent:
            tentativa=5-count
            print("Parab�ns voc� acertou em ",tentativa," tentativas!")
            x=4
            break   
    else:
        print("M�ximo de tentativas atingido! A palavra era:",palavra1) 
        
elif op=="2":
    print("Voc� escolheu o tema cores!")
    nun=randint(0,4)
    palavra1=cores[nun]
    palavra = sample(palavra1,len(palavra1))
    count=5
    for x in range(5):
        if count<5:
            print(animo[count])
        print("Voc� tem ",count," chances para adivinhar a palavra:",palavra)
        ent=input()
        count=count-1
        if palavra1==ent:
            tentativa=5-count
            print("Parab�ns voc� acertou em ",tentativa," tentativas!")
            x=4
            break   
    else:
        print("M�ximo de tentativas atingido! A palavra era:",palavra1) 
elif op=="3":
    print("Voc� escolheu o tema times!")
    nun=randint(0,4)
    palavra1=times[nun]
    palavra = sample(palavra1,len(palavra1))
    count=5
    for x in range(5):
        if count<5:
            print(animo[count])
        print("Voc� tem ",count," chances para adivinhar a palavra:",palavra)
        ent=input()
        count=count-1
        if palavra1==ent:
            tentativa=5-count
            print("Parab�ns voc� acertou em ",tentativa," tentativas!")
            x=4
            break   
    else:
        print("M�ximo de tentativas atingido! A palavra era:",palavra1) 
elif op=="4":
    print("Voc� escolheu o tema pa�ses!")
    nun=randint(0,4)
    palavra1=paises[nun]
    palavra = sample(palavra1,len(palavra1))
    count=5
    for x in range(5):
        if count<5:
            print(animo[count])
        print("Voc� tem ",count," chances para adivinhar a palavra:",palavra)
        ent=input()
        count=count-1
        if palavra1==ent:
            tentativa=5-count
            print("Parab�ns voc� acertou em ",tentativa," tentativas!")
            x=4
            break   
    else:
        print("M�ximo de tentativas atingido! A palavra era:",palavra1) 

