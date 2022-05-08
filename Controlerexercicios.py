import Modelexercicios
import this

opcao = 0

a = 10
b = 20
c = 0

num1 = 0

base = 0
altura = 0


def Menu():
    print('Exercicios em Python\n'
          '1. Troca de números\n'
          '2. Ver número antecessor\n'
          '3. Mostrar a área de um retângulo\n'
          '4. Ver idade convertida\n'
          '5. Ver os eleitores\n'
          '6. Ler o salário reajustado\n'
          '7. Valor do carro\n'
          '8. ')
    this.opcao = int(input())


def Escolha():
    Menu()  # Chamando o método menu, para mostra-lo
    if (this.opcao == 1):
        print(Modelexercicios.Troca(a, b))
    elif (this.opcao == 2):
        ColetarNum1()
        print(Modelexercicios.Sub(this.bacalhau))
    elif (this.opcao == 3):
        Base()
        Altura()
        print('A área do retângulo corresponde a: ')
        print(Modelexercicios.Retangulo(this.base, this.altura))
    elif (this.opcao == 4):
        Idade()
        print(Modelexercicios.Idade(this.idade, this.meses, this.dias))
    elif (this.opcao == 5):
        Eleitores()
        print(Modelexercicios.Eleitores(this.eleitores, this.brancos, this.nulos, this.validos))
    elif (this.opcao == 6):
        Salario()
        print(Modelexercicios.Salario(this.salario, this.final))
    elif (this.opcao == 7):
        Carro()
        print(Modelexercicios.Carro(this.carro, this.distribuidor, this.imposto))
    else:
        print('Número invalido')


def ColetarNum1():
    print('Digite um número: ')
    this.num1 = int(input())


def Base():
    print('Digite a base do triângulo: ')
    this.base = float(input())


def Altura():
    print('Digite a altura do triângulo: ')
    this.altura = float(input())


def Idade():
    print('Digite sua idade: ')
    this.idade = int(input())
    this.meses = 30
    this.dias = 365


def Eleitores():
    print('Vamos ver quantas pessoas votam no seu estado.')
    print('Quantas pessoas no seu estado votaram em branco?')
    this.brancos = int(input())
    print('Quantas pessoas no seu estado votaram nulo?')
    this.nulos = int(input())
    print('Quantas pessoas no seu estado votaram valido?')
    this.validos = int(input())
    print('Esses são o total de eleitores no seu estado:')
    this.eleitores = this.brancos + this.nulos


def Salario():
    print('Qual seu salário mensal atual? ')
    this.salario = int(input())
    print('Quanto a mais você rescebeu nesse mês? ')
    this.reajustado = int(input())
    this.reajustado = this.reajustado / 100

def Carro():
    print('O valor do carro é')
    this.carro = int(input())