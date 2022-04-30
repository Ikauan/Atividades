
def troca():
    a = 10
    b = 20
    print('Valor de A {} valor de B {}'.format(a, b))
    a, b = b, a

    return 'Novo valor de A é: {}, novo valor de B é: {}'.format(a, b)

def sub():
    num1 = int(input('Digite um número: '))
    result = num1 - 1
    return 'O número antecessor de {} é {}'.format(num1, result)

def retangulo():
    base = int(input('Escreva a base do retângulo: '))
    altura = int(input('Escreva a altura do retângulo: '))
    area = base * altura

    return 'A área do retângulo corresponde a {}cm'.format(area)

def idade():
    idade = int(input('Digite sua idade: '))
    meses = idade * 12
    dias = idade * 365
    horas = idade * 8760
    minutos = idade * 525600

    return 'Você tem {} anos\n' \
           'Você tem {} de vida\n' \
           'Você tem {} dias de vida\n' \
           'Você tem {} horas de vida\n' \
           'Você tem {} minutos de vida'.format(idade, meses, dias, horas, minutos)
