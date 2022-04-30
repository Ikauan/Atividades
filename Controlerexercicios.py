import Modelexercicios
import this

opcao = 0

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
        print(Modelexercicios.troca())
    elif(this.opcao == 2):
        print(Modelexercicios.sub())
    elif(this.opcao == 3):
        print(Modelexercicios.retangulo())
    elif(this.opcao == 4):
        print(Modelexercicios.idade())
    else:
        print('Número invalido')
