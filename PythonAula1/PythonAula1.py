#encoding: latin-1
from random import randint
from random import sample

cidades="joinville","garuva","itapoá","curitiba","araquari"
cores='vermelho','azul', 'amarelo','rosa','preto'
times='flamengo','corinthias','vasco','palmeiras','fluminense'
paises='brasil','estados unidos', 'frança','portugal','itália'
animo=['Temos mais uma, não desista','Eu sei que consegue','Vamos, temos chance','vamos, não desista','De primeira e difícil, mais uma']
print("Embaralhando palavras!")
print("Escolha o número correspondente ao tema: cidades(1), cores(2), times(3), países(4)")
op = input()
if op=="1":
    print("Você escolheu o tema cidades!")
    nun=randint(0,4)
    palavra1=cidades[nun]
    palavra = sample(palavra1,len(palavra1))
    count=5
    for x in range(5):
        if count<5:
            print(animo[count])
        print("Você tem ",count," chances para adivinhar a palavra:",palavra)
        ent=input()
        count=count-1
        if palavra1==ent:
            tentativa=5-count
            print("Parabéns você acertou em ",tentativa," tentativas!")
            x=4
            break   
    else:
        print("Máximo de tentativas atingido! A palavra era:",palavra1) 
        
elif op=="2":
    print("Você escolheu o tema cores!")
    nun=randint(0,4)
    palavra1=cores[nun]
    palavra = sample(palavra1,len(palavra1))
    count=5
    for x in range(5):
        if count<5:
            print(animo[count])
        print("Você tem ",count," chances para adivinhar a palavra:",palavra)
        ent=input()
        count=count-1
        if palavra1==ent:
            tentativa=5-count
            print("Parabéns você acertou em ",tentativa," tentativas!")
            x=4
            break   
    else:
        print("Máximo de tentativas atingido! A palavra era:",palavra1) 
elif op=="3":
    print("Você escolheu o tema times!")
    nun=randint(0,4)
    palavra1=times[nun]
    palavra = sample(palavra1,len(palavra1))
    count=5
    for x in range(5):
        if count<5:
            print(animo[count])
        print("Você tem ",count," chances para adivinhar a palavra:",palavra)
        ent=input()
        count=count-1
        if palavra1==ent:
            tentativa=5-count
            print("Parabéns você acertou em ",tentativa," tentativas!")
            x=4
            break   
    else:
        print("Máximo de tentativas atingido! A palavra era:",palavra1) 
elif op=="4":
    print("Você escolheu o tema países!")
    nun=randint(0,4)
    palavra1=paises[nun]
    palavra = sample(palavra1,len(palavra1))
    count=5
    for x in range(5):
        if count<5:
            print(animo[count])
        print("Você tem ",count," chances para adivinhar a palavra:",palavra)
        ent=input()
        count=count-1
        if palavra1==ent:
            tentativa=5-count
            print("Parabéns você acertou em ",tentativa," tentativas!")
            x=4
            break   
    else:
        print("Máximo de tentativas atingido! A palavra era:",palavra1) 

