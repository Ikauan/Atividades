import Modelexercicios
import this

opcao = 0

bacalhau = 0

base = 0
altura = 0

def Menu():
    print('Exercicios em Python\n'
          '1. Troca de números\n'
          '2. Ver número antecessor\n'
          '3. Mostrar a área de um retângulo\n'
          '4. Ver idade convertida\n'
          '5.')
    this.opcao = int(input())


def Escolha():
    Menu() #Chamando o método menu, para mostra-lo
    if(this.opcao == 1):
        print(Modelexercicios.Troca())
    elif(this.opcao == 2):
        ColetarNum1()
        print(Modelexercicios.Sub(this.bacalhau))
    elif(this.opcao == 3):
        Base()
        Altura()
        print('A área do retângulo corresponde a: ')
        print( Modelexercicios.Retangulo(this.base, this.altura))
    elif(this.opco == 4):
        print(Modelexercicios.Idade())
    elif(this.opcao == 5):
        print(Modelexercicios.Votos())
    else:
        print('Número invalido')

def ColetarNum1():
        print('Digite um número: ')
        this.bacalhau = int(input())

def Base():
    print('Digite a base do triângulo: ')
    this.base = float(input())
def Altura():
    print('Digite a altura do triângulo: ')
    this.altura = float(input())