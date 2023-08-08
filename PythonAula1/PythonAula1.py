#encoding: latin-1
from distutils import core
from random import randint
from random import sample

cidadesF="bahia","pará","kansas"
cidadesM="joinville","garuva","itapoá","curitiba","araquari"
cidadesD="washington","rio de janeiro","vaticano","guatemala","méxico","nova guíne","salvador"

coresF='azul','rosa','preto'
coresM='vermelho','laranja','amarelo','esmeralda','preto'
coresD='vermelho','laranja','carmesim','esmeralda','preto','turquesa','água-marinha'

timesF='jec','vasco','palmeiras'
timesM='fluminense','avai','gremio','sport','bahia'
timesD='chelsea','flamengo','barcelona','internacional','corinthians','são paulo','palmeiras'

paisesF='brasil','estados unidos', 'frança'
paisesM='portugal','itália','cingapura','vaticano','iraque'
paisesD='espanha','méxico','rússia','ucrânia','eslováquia','cingapura','brasil'

animo=['Temos mais uma, não desista','Eu sei que consegue','Vamos, temos chance','vamos, não desista','De primeira e difícil, mais uma']
print("Embaralhando palavras!")
tema=int(input("Escolha o número correspondente ao tema: cidades(1), cores(2), times(3), países(4): "))
dificulade= int (input("Escola um nível de dificuldade: Facíl(1), Médio(2), Díficio(3): "))
if tema==1:
    print("Você escolheu o tema cidades!")
    if dificulade==1:
        nun=randint(0,2)
        palavra1=cidadesF[nun]
    elif dificulade==2:
        nun=randint(0,4)
        palavra1=cidadesM[nun]
    elif dificulade==3:
        nun=randint(0,6)
        palavra1=cidadesD[nun]
    else:
       raise Exception("Dificuldade está fora do intervalo!")

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
        
elif tema==2:
    print("Você escolheu o tema cores!")
    if dificulade==1:
        nun=randint(0,2)
        palavra1=coresF[nun]
    elif dificulade==2:
        nun=randint(0,4)
        palavra1=coresM[nun]
    elif dificulade==3:
        nun=randint(0,6)
        palavra1=coresD[nun]
    else:
       raise Exception("Dificuldade está fora do intervalo!")
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
elif tema==3:
    print("Você escolheu o tema times!")
    if dificulade==1:
        nun=randint(0,2)
        palavra1=timesF[nun]
    elif dificulade==2:
        nun=randint(0,4)
        palavra1=timesM[nun]
    elif dificulade==3:
        nun=randint(0,6)
        palavra1=timesD[nun]
    else:
       raise Exception("Dificuldade está fora do intervalo!")

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
elif tema==4:
    print("Você escolheu o tema países!")
    if dificulade==1:
        nun=randint(0,2)
        palavra1=paisesF[nun]
    elif dificulade==2:
        nun=randint(0,4)
        palavra1=paisesM[nun]
    elif dificulade==3:
        nun=randint(0,6)
        palavra1=paisesD[nun]
    else:
       raise Exception("Dificuldade está fora do intervalo!")
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

