class Conta:
    #método construtor
    def __init__(self, agencia, numero, titular, saldo, senha):
        #criando os atributos da classe 
        #atributo privado usa 2 underlines "_"
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha

    def extrato(self):
        return self.__saldo

    # criar um saque e o depósito na classe

    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False