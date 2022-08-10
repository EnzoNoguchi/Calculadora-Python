from Model import Model

class Control:

    #Metodo Construtor

    def __init__(self):
        self.opcao = -1
        self.num1 = 0
        self.num2 = 0
        self.modelo = Model()




    #Metodo Get e Set

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao



    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2

    def setNum1(self, num1):
        self.num1 = num1

    def setNum2(self, num2):
        self.num2 = num2




    #Metodo Coletar

    def Coletar(self):
        print("Informe um numero: ")
        self.setNum1(float(input()))

        print("Informe outro numero: ")
        self.setNum2(float(input()))





    #Menu

    def menu(self):
        print("\nEscolha uma das opções abaixo: "+
              "\n0. Sair"                       +
              "\n1. Soma"                       +
              "\n2. Subtrair"                   +
              "\n3. Multiplicar"                +
              "\n4. Dividir"                    +
              "\n5. Potencia"                   +
              "\n6. Raiz"                       +
              "\n7. Tabuada")
        self.setOpcao(int(input()))#Coletando a escolha do usuario






    #Operações

    def operacao(self):
        while(self.getOpcao != 0):
            self.menu()#Mostrar a lista de dados na tela
            if self.getOpcao() == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                self.Coletar()
                print("A soma dos 2 numeros é: {}".format(self.modelo.soma(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 2:
                self.Coletar()
                print("O resultado da subtração dos 2 numeros é: {}".format(self.modelo.subtracao(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 3:
                self.Coletar()
                print("O resultado da multiplicação de 2 numeros é: {}".format(self.modelo.multiplicacao(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 4:
                self.Coletar()
                resultado = self.modelo.divisao(self.getNum1(), self.getNum2())
                if resultado == -1:
                    print("Impossivel dividir por zero!")
                else:
                     print("O resultado da divisão de 2 numeros é: {}".format(resultado))
            elif self.getOpcao() == 5:
                self.Coletar()
                print("O resultado da potencia é: {}".format(self.modelo.potencia(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 6:
                print("Informe um numero para calcular a raiz: ")
                resultado = self.modelo.raiz(float(input()))
                if resultado == -1:
                    print("Impossivel calcular a raiz!")
                else:
                    print("O resultado é {}".format(resultado))
            elif self.getOpcao() == 7:
                print("informe um numero: ")
                print(self.modelo.tabuada(float(input())))
            else:
                print("Opção inválida")