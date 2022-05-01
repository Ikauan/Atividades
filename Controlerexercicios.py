import Modelexercicios
import this

opcao = 0
this.idade = 0

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
        print(Modelexercicios.Sub())
    elif(this.opcao == 3):
        print(Modelexercicios.Retangulo())
    elif(this.opcao == 4):
        #Coletar()
        #print('Informe sua idade: ')
        print(Modelexercicios.Idade()) #(this.idade, this.meses, this.dias)
    elif(this.opcao == 5):
        print(Modelexercicios.Votos())
    else:
        print('Número invalido')

#def Coletar():
#    this.idade = print('Informe sua idade: ')
#    this.idade = int(input())
#    this.meses = this.idade
#    this.dias = this.idade

