import random

#essa funcao verifica se o resultado esta certo ou nao
def compara(C,R):
    if C==R:
        print('Resposta certa!\n')
        return 1
    else:
        print('Resposta errada. A resposta certa:',C,'\n')
        return 0

#essa funcao gera 10 numeros aleatorios e faz a operacao
def questao(OP):
    CERTO=0
    if OP=='a': #soma
        for i in range(0,5):
            a=random.randint(1,100)
            b=random.randint(1,100)
            print(i+1,')Quanto é',a,'+',b,'?')
            c=a+b
            r=int(input('R='))
            v=compara(c,r)
            if v==1:
                CERTO+=10

    elif OP=='b': #subtracao
        for i in range(0,5):
            a,b=0,1
            while(a<b):
                a=random.randint(1,100)
                b=random.randint(1,100)
            print(i+1,')Quanto é',a,'-',b,'?')
            c=a-b
            r=int(input('R='))
            v=compara(c,r)
            if v==1:
                CERTO+=10

    elif OP=='c': #multiplicacao
        for i in range(0,5):

            a=random.randint(1,100)
            b=random.randint(1,100)
            print(i+1,')Quanto é',a,'*',b,'?')
            c=a*b
            r=int(input('R='))
            v=compara(c,r)
            if v==1:
                CERTO+=10

    elif OP=='d': #divisao
        for i in range(0,5):
            a,b=3,2
            while(a%b!=0):
                a=random.randint(1,100)
                b=random.randint(1,100)
            print(i+1,')Quanto é',a,'/',b,'?')
            c=a/b
            r=int(input('R='))
            v=compara(c,r)
            if v==1:
                CERTO+=10

    return CERTO

print('Operacoes possiveis:\na)Soma\nb)Subtracao\nc)Multiplicacao\nd)Divisao\nQual voce escolhe?')
op=input()
print('\n')
pontos=questao(op) #pontos feitos
print('Obrigada por utilizar o programa! Voce acertou','(',pontos,'/','50',')')