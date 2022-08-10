import math


class Model:
    #Criar um metodo Construtor
    def __init__(self):
        pass



    #Metodo Soma

    def soma(self, num1, num2):
        return num1 + num2



    #Metodo Subtração

    def subtracao(self, num1,  num2):
        return num1 - num2



    # Metodo Divisão

    def divisao(self, num1, num2):
        if num2 <= 0:
            return -1
        else:
            return num1 / num2



    # Metodo Multiplicação

    def multiplicacao(self, num1, num2):
        return num1 * num2



    # Metodo Potencia

    def potencia(self, base, expoente):
        if expoente == 0:
            return -1
        elif expoente == 1:
            return base
        else:
            return math.pow(base, expoente)



    # Metodo Raiz

    def raiz(self, num):
        if float(num) < float(0):
            return -1
        else:
            return math.sqrt(num)

    # Metodo Tabuada

    def tabuada(self, num):
        msg = ""
        for i in range(10):
            msg = msg + "\n{} * {} = {}".format(num, i, num * i)
        return msg