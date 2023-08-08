#encoding: latin-1
from distutils import core
from random import randint
from random import sample

cidadesF="bahia","par�","kansas"
cidadesM="joinville","garuva","itapo�","curitiba","araquari"
cidadesD="washington","rio de janeiro","vaticano","guatemala","m�xico","nova gu�ne","salvador"

coresF='azul','rosa','preto'
coresM='vermelho','laranja','amarelo','esmeralda','preto'
coresD='vermelho','laranja','carmesim','esmeralda','preto','turquesa','�gua-marinha'

timesF='jec','vasco','palmeiras'
timesM='fluminense','avai','gremio','sport','bahia'
timesD='chelsea','flamengo','barcelona','internacional','corinthians','s�o paulo','palmeiras'

paisesF='brasil','estados unidos', 'fran�a'
paisesM='portugal','it�lia','cingapura','vaticano','iraque'
paisesD='espanha','m�xico','r�ssia','ucr�nia','eslov�quia','cingapura','brasil'

animo=['Temos mais uma, n�o desista','Eu sei que consegue','Vamos, temos chance','vamos, n�o desista','De primeira e dif�cil, mais uma']
print("Embaralhando palavras!")
tema=int(input("Escolha o n�mero correspondente ao tema: cidades(1), cores(2), times(3), pa�ses(4): "))
dificulade= int (input("Escola um n�vel de dificuldade: Fac�l(1), M�dio(2), D�ficio(3): "))
if tema==1:
    print("Voc� escolheu o tema cidades!")
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
       raise Exception("Dificuldade est� fora do intervalo!")

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
        
elif tema==2:
    print("Voc� escolheu o tema cores!")
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
       raise Exception("Dificuldade est� fora do intervalo!")
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
elif tema==3:
    print("Voc� escolheu o tema times!")
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
       raise Exception("Dificuldade est� fora do intervalo!")

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
elif tema==4:
    print("Voc� escolheu o tema pa�ses!")
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
       raise Exception("Dificuldade est� fora do intervalo!")
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

