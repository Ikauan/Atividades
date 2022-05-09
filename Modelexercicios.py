import this
this.final = 0
this.distribuidor = 0
this.imposto = 0
this.media = 0
this.duzia = 0

def Troca(a, b):

    a = 10
    b = 20
    a, b = b, a

    return 'A = {}  B = {}'.format(a, b)
    #print('Valor de A {} valor de B {}'.format(a, b))
    #a, b = b, a

    #return 'Novo valor de A é: {}, novo valor de B é: {}'.format(a, b)

def Sub(num1):
    return num1 - 1
    #result = num1 - 1
    #return 'O número antecessor de {} é {}'.format(num1, result)

def Retangulo(base, altura):
    return base * altura
    #altura = 0
    #base = 0
    #area = altura * base

    #base = int(input('Escreva a base do retângulo: '))
    #altura = int(input('Escreva a altura do retângulo: '))


    #return 'A área do retângulo corresponde a {}cm'.format(area)

def Idade(idade, meses, dias):
    meses = idade * 30
    dias = idade * 365
    return 'Você tem {} anos.\n Você tem {} em meses.\n Você tem {} em dias'.format(idade, meses, dias)
    #idade = int(input('Digite sua idade: '))
    #meses = idade * 12
    #dias = idade * 365
    #horas = idade * 8760
    #minutos = idade * 525600

    #return 'Você tem {} anos\n' \
           #'Você tem {} de vida\n' \
           #'Você tem {} dias de vida\n'.format(idade, meses, dias) \
           #'Você tem {} horas de vida\n' \
           #'Você tem {} minutos de vida'.format(idade, meses, dias, horas, minutos)

def Eleitores(eleitores, brancos, nulos, validos): # Ajuda
    brancos = 100 * (this.brancos / eleitores)
    nulos = 100 * (this.nulos / eleitores)
    validos = 100 * (this.validos / eleitores)


    return '{:.2f}% De eleitores votaram branco.\n{:.2f}% De eleitores votaram nulo.\n{:.2f}% São validos.'.format(brancos, nulos, validos)

def Salario(salario, reajustado):
    this.final = (this.salario * this.reajustado) + this.salario
    return 'O novo salário é: {} R$ e o reajuste foi {}%'.format(this.final, this.reajustado)

def Carro(carro, distribuidor, imposto):
    carro = 0
    distribuidor = this.carro * (28 / 100)
    imposto = carro - this.distribuidor * (45 / 100)

    return 'Este é o custo final do carro {}'.format(imposto + distribuidor + carro)

def Nota(nota1, nota2, nota3, media):
    nota1 = nota1
    nota2 = nota2
    nota3 = nota3
    media = (nota1 + nota2 + nota3) / 3

    if(media >= 6):
        print('O aluno teve a nota de {:.2f} e passou de ano.'.format(media))
    else:
        print('O aluno teve a nota de {:.2f} e repetiu de ano'.format(media))

def Fruta(duzia):
    duzia = this.duzia


    if(duzia >= 12):
        print('Você comprou {} maças e o valor ficou {} Reais.'.format(duzia, duzia * 1.00))
    elif(duzia <= 11):
        print('Você comprou {} maçãs e o valor ficou {} Reais.'.format(duzia, duzia * 1.30))