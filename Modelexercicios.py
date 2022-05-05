import this

def Troca(a, b):

    a = 10
    b = 20
    a, b = b, a

    return 'A = {}  B = {}'.format(a, b)
    #print('Valor de A {} valor de B {}'.format(a, b))
    #a, b = b, a

    #return 'Novo valor de A é: {}, novo valor de B é: {}'.format(a, b)

def Sub(num1):
    return num1 -1
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
    return 'Você tem {}.\n' \
           'Você tem {} em meses.\n' \
           'Você tem {} em dias'.format(idade, meses, dias)
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
    eleitores = eleitores
    brancos = eleitores % 100
    nulos = (eleitores - brancos) % 100
    validos = (eleitores - brancos - nulos ) % 100

    return eleitores, brancos, nulos, validos